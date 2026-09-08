# Outreach Compliance Note — 2026-09-08

A prior failed cron attempt sent Adobe, Caira, Fetra, and InVideo messages with ad-hoc scripts before the centralized standing-policy sender was fully used. Provider read-back records are preserved as historical evidence. The reusable ad-hoc scripts were removed. Adobe message e1122fc6-6ee3-41d4-b1e4-19914d5ef0ed was rechecked as delivered and backfilled into the authoritative vendor-outreach history so the 30-day cooldown applies. The Caira, Fetra, original InVideo bounce, and one permitted InVideo fallback were already present in centralized history.

All later Runway and Synthesia messages were validated and sent through aivp_bulk_vendor_outreach.py under policy aivp-qualified-launch-outreach-v1.
