import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest

MODULE_PATH = Path(__file__).parents[1] / "scripts" / "search_console_oauth.py"


class SearchConsoleOAuthTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location("search_console_oauth", MODULE_PATH)
        cls.mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.mod)

    def test_requests_only_search_console_readonly_scope(self):
        self.assertEqual(
            self.mod.REQUIRED_SCOPES,
            ("https://www.googleapis.com/auth/webmasters.readonly",),
        )

    def test_save_token_uses_private_permissions(self):
        class FakeCredentials:
            def to_json(self):
                return json.dumps({"token": "placeholder"})

        with tempfile.TemporaryDirectory() as tmp:
            token = Path(tmp) / "nested" / "token.json"
            self.mod.save_token(FakeCredentials(), token)
            self.assertEqual(token.stat().st_mode & 0o777, 0o600)
            self.assertEqual(json.loads(token.read_text()), {"token": "placeholder"})


if __name__ == "__main__":
    unittest.main()
