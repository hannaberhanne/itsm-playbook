"""How many issue types does it take to cover most of the service desk's work?

Reads an incident export (CSV), sets aside automated monitoring alerts, groups
the remaining tickets by normalized short description, and reports how many
issue types cover 80%, 90% and 95% of troubleshooting volume.

Usage:
    python3 scripts/coverage_analysis.py data/sample_incidents.csv
    python3 scripts/coverage_analysis.py my_export.csv --column short_description --top 25
"""

import argparse
import csv
import re
from collections import Counter

THRESHOLDS = {"core": 0.80, "comprehensive": 0.90, "exhaustive": 0.95}

# Automated alerts are not troubleshooting work, so they are counted separately.
MONITORING_PATTERNS = {
    "LOW_DISK_SPACE": ["low disk space"],
    "DEVICE_OFFLINE": ["device offline"],
    "UPS_ALERT_OR_RESET": ["ups is alarming", "ups reset"],
}


def normalize(text):
    return re.sub(r"\s+", " ", (text or "").strip().lower())


def monitoring_category(label):
    for category, patterns in MONITORING_PATTERNS.items():
        if any(p in label for p in patterns):
            return category
    return None


def read_rows(path):
    for encoding in ("utf-8-sig", "cp1252"):
        try:
            with open(path, newline="", encoding=encoding) as f:
                return list(csv.DictReader(f)), encoding
        except UnicodeDecodeError:
            continue
    raise RuntimeError(f"Could not decode {path}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("--column", default="short_description")
    parser.add_argument("--top", type=int, default=15)
    args = parser.parse_args()

    rows, encoding = read_rows(args.path)
    if not rows:
        raise SystemExit("No tickets found")
    if args.column not in rows[0]:
        raise SystemExit(f"Column '{args.column}' not found. Columns: {', '.join(rows[0])}")

    issues, monitoring = Counter(), Counter()
    for row in rows:
        label = normalize(row.get(args.column)) or "<blank>"
        category = monitoring_category(label)
        if category:
            monitoring[category] += 1
        else:
            issues[label] += 1

    primary_total = sum(issues.values())
    if primary_total == 0:
        raise SystemExit("No tickets left after removing monitoring alerts")

    coverage, running = [], 0
    for label, count in issues.most_common():
        running += count
        coverage.append((label, count, running, running / primary_total))

    print(f"encoding: {encoding}")
    print(f"total tickets: {len(rows)}")
    print(f"monitoring alerts set aside: {sum(monitoring.values())}")
    for category in MONITORING_PATTERNS:
        print(f"  - {category}: {monitoring[category]}")
    print(f"troubleshooting tickets: {primary_total}")
    print(f"unique issue descriptions: {len(issues)}")
    print()
    print("Issue types needed to reach each coverage level:")
    for name, target in THRESHOLDS.items():
        for i, (_, _, cum_count, cum_pct) in enumerate(coverage, start=1):
            if cum_pct >= target:
                print(f"  - {name} ({target:.0%}): {i} issue types, {cum_count} tickets, {cum_pct:.1%}")
                break
    print()
    print(f"Top {args.top} issues with cumulative coverage:")
    for label, count, _, cum_pct in coverage[: args.top]:
        print(f"  {count:5d} | {cum_pct:6.1%} | {label}")


if __name__ == "__main__":
    main()
