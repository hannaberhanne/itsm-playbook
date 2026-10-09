"""Write a synthetic incident export so coverage_analysis.py has something to run on.

Every ticket here is made up. Volumes follow a long-tail shape like a real
service desk: a few issue types make up most of the work.

Usage:
    python3 scripts/make_sample_incidents.py
"""

import csv
import random
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "data" / "sample_incidents.csv"

# (short description, relative weight)
ISSUES = [
    ("AD account locked", 120), ("Password reset", 95), ("MFA not working", 70),
    ("Unable to log into EHR", 55), ("Printer not printing", 48), ("EHR not opening", 40),
    ("Badge reader not working", 32), ("VPN not connecting", 30), ("Email not syncing", 26),
    ("Scanner not working in EHR", 22), ("New user setup", 20), ("Software install request", 18),
    ("Monitor not displaying", 15), ("EHR not responding", 14), ("Shared drive access", 12),
    ("Phone not working", 10), ("Record locked by another user", 8), ("Wi-Fi not connecting", 8),
    ("Keyboard not working", 6), ("Teams audio issue", 5), ("Label printer offline", 4),
    ("Low disk space", 60), ("Device offline for 30 days", 45), ("UPS is alarming", 12),
]
EXTRA_TAIL = [f"Other issue {i}" for i in range(1, 61)]


def main():
    rng = random.Random(3)
    labels = [i[0] for i in ISSUES] + EXTRA_TAIL
    weights = [i[1] for i in ISSUES] + [1] * len(EXTRA_TAIL)
    OUT.parent.mkdir(exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["number", "priority", "short_description", "category", "state"])
        for n in range(1, 2001):
            label = rng.choices(labels, weights)[0]
            w.writerow([f"INC{100000 + n}", rng.choice(["3 - Moderate", "4 - Low", "2 - High"]),
                        label, "Inquiry / Help", "Resolved"])
    print(f"Wrote 2000 synthetic incidents to {OUT}")


if __name__ == "__main__":
    main()
