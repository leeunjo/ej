"""Tier-A fragmentation and funding indicators from CEB public financial statistics.

Inputs (downloaded unchanged from https://unsceb.org/data-download into data/raw/ceb/):
  revenue_contrib_type.csv, expenses_by_country_region_sub_agency.csv
Run: python3 scripts/ceb_fragmentation.py [year]
Notes:
  - expenses_type E06 = total expenses; E06A/B/C are its components (do not sum them with E06).
  - A "presence" here = an entity reporting expenses in a country (location_type COU). It is NOT
    proof of a physical office: non-resident entities can report spending without one.
"""
import csv
import statistics
import sys
from collections import defaultdict
from pathlib import Path

RAW = Path(__file__).resolve().parent.parent / "data" / "raw" / "ceb"
YEAR = sys.argv[1] if len(sys.argv) > 1 else "2025"


def rows(name):
    with open(RAW / name, encoding="utf-8-sig") as f:
        yield from csv.DictReader(f)


def revenue_mix(year):
    totals = defaultdict(float)
    for r in rows("revenue_contrib_type.csv"):
        if r["calendar_year"] == year:
            totals[r["rev_type_name"]] += float(r["amount"] or 0)
    grand = sum(totals.values())
    print(f"Revenue {year}: ${grand / 1e9:.1f}bn")
    for k, v in sorted(totals.items(), key=lambda x: -x[1]):
        print(f"  {k:<48} {v / grand:6.1%}  ${v / 1e9:.1f}bn")


def country_fragmentation(year):
    by_country = defaultdict(lambda: defaultdict(float))
    for r in rows("expenses_by_country_region_sub_agency.csv"):
        if r["calendar_year"] == year and r["expenses_type"] == "E06" and r["location_type"] == "COU":
            by_country[r["country/territory"]][r["agency"]] += float(r["amount"] or 0)
    pres = [v for d in by_country.values() for v in d.values() if v > 0]
    per_country = [sum(1 for v in d.values() if v > 0) for d in by_country.values()]
    total = sum(pres)
    print(f"\nCountry-level expenses {year}: ${total / 1e9:.1f}bn across {len(by_country)} countries/territories")
    print(f"  entities per country: median {statistics.median(per_country)}, max {max(per_country)}")
    print(f"  entity-country presences: {len(pres)}")
    for cut in (1e6, 5e6):
        small = [v for v in pres if v < cut]
        print(f"  presences < ${cut / 1e6:.0f}m: {len(small)} ({len(small) / len(pres):.0%}) "
              f"holding {sum(small) / total:.1%} of country-level spend")
    return by_country


if __name__ == "__main__":
    revenue_mix(YEAR)
    country_fragmentation(YEAR)
