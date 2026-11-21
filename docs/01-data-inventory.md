# Data Inventory & Existing Work (what to reuse, what is missing)

_Status: v1 · 2026-11-21 · All figures reproducible from `data/raw/` + `scripts/`_

## 1. Existing official work to build on (do not duplicate)

### UN80 Initiative (EOSG)
| Asset | What it gives us | Where |
|---|---|---|
| Action Plan + annex (24 Nov 2025) | 31 work packages, ~85 actions, leads (DSG/USG/ASG/ED level), source paragraphs | `data/raw/un80/un80-action-plan-2025-11.pdf` |
| Progress & Next Steps (27 Apr 2026) | Per-action progress, **"pathway to decision"** and intergovernmental body per action | `data/raw/un80/un80-progress-next-steps-2026-04.pdf` |
| Actions Dashboard (updated 2 Nov 2026) | Live status per action (33 "Decision taken", 57 "Further work ongoing") | un80actions.un.org; snapshot `data/raw/un80/un80-actions-dashboard-2026-11-02.txt` |
| GitHub UN-EOSG-Analytics (public, **no licence file**) | Structured JSON behind the dashboards: `un80-actions/public/data/actions.json`, `actions_progress.json` (incl. `summaryTable` decision pathways); `un-system-chart-navigator/public/un-entities.csv` (169 entities, category, principal organ, CEB membership, links to budgets/strategic plans/transparency portals); `reference-datasets/.../un_leaders.csv` (187 senior officials and titles); `mandate-housekeeping` (programme budget 2026 parsed by entity/mandate) | github.com/UN-EOSG-Analytics |
| Mandate Registry, Transparency Gateway, Programme Budget Results | Mandates by entity; Secretariat spend/results | mandates.un.org · open.un.org · results.un.org |

**Licence note:** the GitHub repos carry no licence. We **read and cite** their data (UN public information) and link to them; we do not copy their code into this repo.

**Relevant UN80 actions that overlap our flagships:**
- **WP14 Unified Services Roadmap**: A63/65 shared services, A66 common back offices, **A67 cost transparency (tools + public dashboard, country-team pilots)**, A67 also harmonised support costs.
- **WP18 Funding mechanisms**: A76–78 pooled/core funding, A91 Funding Compact review.
- **WP15 Technology**: A61 shared core ICT; **WP16 Data Commons**.
- WP5 UNCT reconfiguration, WP3/WP4 merger assessments.

→ **Our positioning:** not a parallel reform plan. Instead: (a) an **independent, entity- and country-comparable evidence layer** (unit costs, fragmentation); (b) the **decision-rights map** UN80 does not publish at entity-governing-body level; (c) a **root-cause / implementation-risk analysis**: why these actions may stall where earlier reforms stalled.

### First finding from UN80's own data (to verify and deepen)
In UN80's April 2026 decision-pathway table (68 action rows): **48 (~70%) envisage no intergovernmental decision; 38 end at the Secretary-General; only 1 names "entities / relevant governing bodies."** But the SG has no line authority over specialized agencies, and funds/programmes' cost-recovery, procurement and HR rules are set by their own executive boards. Hypothesis: system-wide operational actions (shared services, back offices, support-cost harmonisation) rely on **voluntary** entity uptake, the same mechanism that limited BOS and mutual recognition. The decision-rights map tests this action by action. _Caveat: UN80 says "at this stage"; later decisions may route to boards._

## 2. Quantitative sources

| Source | Granularity | Years | Access | Use |
|---|---|---|---|---|
| **CEB Financial Statistics** (CSV) | Entity × sub-entity × country × funding type | 2017–2025 | ✅ `data/raw/ceb/` | Revenue mix, expenses by country, fragmentation |
| **CEB HR Statistics** (CSV) | Entity × duty station × year | 2017–2025 | ✅ `data/raw/ceb/` | Staff per entity per country/duty station |
| UN INFO BOS status / Cooperation Framework status | Country × common service | current | ⚠️ Embedded Power BI (blocked/not exportable here) → **user exports Excel and uploads** | BOS services, cost avoidance, LTAs |
| UNGM Annual Statistical Report on UN Procurement | Entity × country × category | annual | ⚠️ site blocks scripts → browser or manual download | Procurement volume, vendor overlap |
| IATI (d-portal / API) | Activity & transaction level, for publishing entities | ongoing | ✅ | Transaction counts (partial) |
| MOPAN assessments | Entity | periodic | ✅ | Independent performance evidence |
| JIU reports & recommendation tracking | System-wide | ongoing | ⚠️ certificate issue → browser | Reform post-mortem |
| UNdata / UN Data Commons (data.un.org) | **Country statistics** (SDGs, prices, population) | — | not yet added | **Low priority**: only for normalising costs across countries (price levels, PPP). It describes countries, not UN operations |

## 3. Tier-A indicators already computable (CEB, `scripts/ceb_fragmentation.py`)

**Funding mix (system-wide revenue)**
| | 2024 | 2025 |
|---|---|---|
| Total revenue | $68.3bn | $63.2bn |
| Voluntary **earmarked** | 60.6% | 55.3% |
| Assessed | 20.2% | 21.0% |
| Voluntary **core** | 7.8% | 8.7% |
| Other activities | 11.4% | 15.0% |

**Country-level fragmentation (expenses, location type = country)**
| | 2021 | 2025 |
|---|---|---|
| Country-level expenses | $44.8bn | $45.4bn |
| Countries/territories | 245 | 241 |
| Entities per country (median / max) | 12 / 24 | 13 / 24 |
| Entity-country presences | 2,714 | 2,819 |
| Presences spending < $1m/yr | 41% (0.7% of spend) | 39% (0.8% of spend) |
| Presences spending < $5m/yr | 69% (4.8% of spend) | **66% (5.0% of spend)** |

Reading: two-thirds of the system's entity-country presences account for ~5% of country-level spending. Each can carry its own fixed costs (representation, back office, agreements, banking, reporting). Pattern is **stable 2021→2025**. _Caveat: a "presence" = reported country expenses, not necessarily a physical office (High confidence on counts; Medium on implied overhead until matched with HR duty-station data)._

**Türkiye example (2025):** $402m country-level expenses across 16 reporting entities; 1,348 staff across 13 organisations in 11 duty stations (CEB HR).

## 4. Unit-cost metrics: feasibility

| Metric | Numerator | Denominator | Tier | Notes |
|---|---|---|---|---|
| Support/management cost ratio by entity | CEB expense categories / entity financial statements | Total expenses | A/B | Definitions differ across entities; check harmonised cost classification |
| Spend per staff, staff per $m delivered, by entity × country | CEB expenses | CEB HR duty station | **A** | Proxy for operating intensity |
| Presence size distribution ("long tail") | CEB expenses | count of presences | **A** | Done above |
| Cost per procurement action | Procurement unit cost | # POs/contracts | B/C | UNGM volumes public; counts mostly not |
| Cost per payment / per hire | Finance/HR unit cost | # transactions / hires | **C** | Not public → itself a finding; UN80 A67 cost-transparency tools may change this |
| Cost per m² | Premises cost | m² | C | Common premises data partial (UN INFO) |
| BOS cost avoidance per country | UN INFO BOS | — | A (with user export) | Self-reported; treat as Medium confidence |

## 5. Next data actions
1. **User:** export UN INFO BOS status + Cooperation Framework status Excel files (all countries) and upload → `data/raw/uninfo/`.
2. Join CEB expenses × CEB HR by entity × country → Tier-A operating-intensity table (country-office level).
3. Build decision-rights dataset: UN80 actions × decision pathway × **entity governing bodies that must also act** × their membership.
4. Retrieve UN80 June 2026 Unified Services Roadmap info brief + cost-transparency dashboard; check what A67 already publishes.
