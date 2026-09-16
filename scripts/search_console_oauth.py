#!/usr/bin/env python3
"""Authorize read-only Google Search Console access for AI Video Picks."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

DEFAULT_CLIENT = Path("/home/tom/wealth-ruin/secrets/youtube-client-secret.json")
HERMES_HOME = Path(
    os.environ.get("HERMES_HOME", "/home/tom/.hermes/profiles/aivideopicks")
)
DEFAULT_TOKEN = HERMES_HOME / "secrets" / "search-console-token.json"
REQUIRED_SCOPES = ("https://www.googleapis.com/auth/webmasters.readonly",)


def validate_client_config(data: dict) -> None:
    if "installed" not in data:
        raise ValueError("OAuth JSON must contain an installed Desktop client")
    required = {"client_id", "client_secret", "auth_uri", "token_uri", "redirect_uris"}
    missing = sorted(required.difference(data["installed"]))
    if missing:
        raise ValueError("OAuth client is missing: " + ", ".join(missing))


def load_client_config(path: Path) -> None:
    with path.open(encoding="utf-8") as handle:
        validate_client_config(json.load(handle))


def save_token(credentials: Credentials, path: Path) -> None:
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    path.write_text(credentials.to_json(), encoding="utf-8")
    os.chmod(path, 0o600)


def authorize(client_path: Path, token_path: Path, port: int) -> Credentials:
    load_client_config(client_path)
    credentials = None
    if token_path.exists():
        credentials = Credentials.from_authorized_user_file(token_path, REQUIRED_SCOPES)
    if credentials and credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())
    if not credentials or not credentials.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            str(client_path), REQUIRED_SCOPES
        )
        credentials = flow.run_local_server(
            host="localhost",
            port=port,
            open_browser=False,
            authorization_prompt_message=(
                "Open this Google authorization URL:\n{url}\n"
            ),
            success_message=(
                "AI Video Picks Search Console authorization completed. "
                "You may close this tab."
            ),
            access_type="offline",
            prompt="consent",
            include_granted_scopes="false",
        )
    save_token(credentials, token_path)
    return credentials


def list_sites(credentials: Credentials) -> list[dict]:
    service = build("searchconsole", "v1", credentials=credentials, cache_discovery=False)
    response = service.sites().list().execute()
    return response.get("siteEntry", [])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("auth", "verify"))
    parser.add_argument("--client", type=Path, default=DEFAULT_CLIENT)
    parser.add_argument("--token", type=Path, default=DEFAULT_TOKEN)
    parser.add_argument("--port", type=int, default=8766)
    args = parser.parse_args()

    credentials = authorize(args.client, args.token, args.port)
    print("Search Console OAuth token stored securely.")
    if args.command == "verify":
        sites = list_sites(credentials)
        print(f"Verified Search Console access: {len(sites)} properties visible.")
        for site in sites:
            print(f"- {site.get('siteUrl', '')} [{site.get('permissionLevel', 'unknown')}]")


if __name__ == "__main__":
    main()
