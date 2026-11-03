#!/usr/bin/env python3
"""Report changes in the Amazon Ads API contracts this package is built on.

specs/contracts.json records, per contract, the URL, its sha256 and the
modules that use it. This script compares the remote sha256 against the
recorded one.

It never rewrites the hash by itself. A change is only recorded when someone
updates the contract file and its hash in a commit, so an alert means
"changed since we last looked" rather than "differs from an old file" and the
same warning does not repeat every day.

Usage:
    python scripts/check_spec_updates.py
    python scripts/check_spec_updates.py --json
"""

import argparse
import hashlib
import json
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SPECS_DIR = REPO_ROOT / "specs"
CONTRACTS = SPECS_DIR / "contracts.json"

TIMEOUT = 45


def load_catalog() -> dict:
    """The recorded contracts, or an empty dict when none is tracked yet."""

    if not CONTRACTS.exists():
        return {}

    with CONTRACTS.open(encoding="utf-8") as handle:
        return json.load(handle)


def remote_hash(url: str) -> tuple:
    """Download one contract and return (sha256, size, error)."""

    request = urllib.request.Request(
        url, headers={"User-Agent": "python-amazon-ad-api/spec-check"}
    )

    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            data = response.read()
            return hashlib.sha256(data).hexdigest(), len(data), None
    except Exception as error:  # noqa: BLE001 - any network failure is one case
        return "", 0, str(error)


def check(names: list, catalog: dict) -> list:
    """Compare every contract with the recorded hash, in parallel."""

    changes = []

    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {
            pool.submit(remote_hash, catalog[name]["url"]): name
            for name in names
        }

        for future in as_completed(futures):
            name = futures[future]
            digest, size, error = future.result()
            recorded = catalog[name]

            if error:
                changes.append({
                    "contract": name,
                    "status": "unreachable",
                    "detail": error,
                    "modules": recorded["modules"],
                })
                continue

            if digest != recorded["sha256"]:
                changes.append({
                    "contract": name,
                    "status": "content_changed",
                    "detail": "sha256 %s -> %s, remote_size=%d"
                              % (recorded["sha256"][:12], digest[:12], size),
                    "modules": recorded["modules"],
                })

    return sorted(changes, key=lambda c: c["contract"])


def main() -> int:

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="machine readable output")
    parser.add_argument("--only", nargs="*", help="limit to these contract names")
    args = parser.parse_args()

    catalog = load_catalog()

    if not catalog:
        print("specs/contracts.json is missing or empty; nothing to check")
        return 1

    names = args.only or sorted(catalog)
    missing = [n for n in names if n not in catalog]

    if missing:
        print("unknown contract(s): %s" % ", ".join(missing), file=sys.stderr)
        return 1

    changes = check(names, catalog)

    if args.json:
        json.dump({"has_updates": bool(changes), "checked": len(names),
                   "changes": changes}, sys.stdout, indent=2)
        print()
    else:
        print("checked %d contract(s)" % len(names))

        if not changes:
            print("no changes")
        else:
            print()
            for change in changes:
                print("[%s] %s" % (change["status"], change["contract"]))
                print("    %s" % change["detail"])
                print("    used by: %s" % ", ".join(change["modules"][:4]))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
