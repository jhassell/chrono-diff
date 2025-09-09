#!/usr/bin/env python3
"""
chronodiff (barebones skeleton)

Your assignment:
  - Read events from a CSV/TXT file (--input).
  - Normalize times to a single timezone (--tz or system local).
  - Compute differences with relativedelta (REQUIRED).
  - Show Status (PAST/FUTURE/TODAY), calendar breakdown (Y/M/D/H/M/S),
    TotalSeconds, and BestValue/BestUnit (largest sensible unit).
"""

import argparse
from datetime import datetime
from zoneinfo import ZoneInfo  # Python 3.9+
from dateutil import parser as dtparse
from dateutil.relativedelta import relativedelta  # REQUIRED: use RelativeDelta


def parse_args():
    p = argparse.ArgumentParser(description="chronodiff: two-way time distance utility")
    p.add_argument("--input", required=True, help="Path to events CSV/TXT")
    p.add_argument("--now", help='Override now: "YYYY-MM-DD" or "YYYY-MM-DD HH:MM"')
    p.add_argument("--tz", help='IANA zone like "America/Chicago" (default: system local)')
    p.add_argument("--output", choices=["table", "csv"], default="table")
    return p.parse_args()


def main():
    args = parse_args()

    # TODO: resolve 'now' (use dtparse + ZoneInfo)
    # TODO: read events from args.input
    # TODO: compute relativedelta differences
    # TODO: pick BestValue/BestUnit
    # TODO: print table or CSV with required columns

    print("chronodiff skeleton ready. Implement your logic here.")


if __name__ == "__main__":
    main()

