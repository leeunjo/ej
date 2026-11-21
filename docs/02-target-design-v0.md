# Target Design v0: How the UN System Should Decide

_Status: hypothesis-driven draft for stress-testing · 2026-11-21_
_Every design choice lists the evidence for it, the evidence still needed, and how to test it. This is the discipline the current reform lacks._

---

## 0. Diagnosis in one paragraph

The UN system keeps **adding coordination where it should be changing rules**. When reformers cannot change who decides, who pays and which rules apply, they add a coordination layer (OMT, BOS, CBO, UNCT, UNSDG, HLCM) and a reporting layer (UN INFO, BOS/CBA reporting, Funding Compact reviews) on top of ~40 sets of rules, ~13 entities per country and dozens of ERPs. Each layer has real costs and voluntary benefits. Result: **coordination substitutes for authority**, and every reform raises transaction costs before it lowers them. UN80 so far follows the same pattern.

### Evidence so far (public data)
| Claim | Evidence | Confidence |
|---|---|---|
| Money is fragmented and controlled outside the system | 2025 revenue $63.2bn: **55% earmarked, 8.7% core** (CEB) | High |
| A few capitals control most earmarked money | Top 10 government donors = **64%** of government earmarked revenue in 2025 (75% in 2024); US earmarked fell $10.6bn → $3.8bn 2024→25 (CEB) | High |
| Field presence has a long fixed-cost tail | 2,819 entity-country presences; **66% spend < $5m/yr yet hold 5% of country spend**; unchanged since 2021 (CEB) | High on counts; Medium on implied overhead |
| UN80 relies on voluntary uptake | 48 of 68 UN80 decision pathways need no intergovernmental decision; 38 end at the SG; only 1 names entity governing bodies (UN80 Apr 2026) | High (facts), Medium (inference) |
| UN80 tracks outputs, not outcomes | 0 of 90 dashboard actions state a quantified savings/cost/time target; 38 milestones are papers "for the SG's consideration"; WP14 all 5 actions still "ongoing" Nov 2026; support-cost harmonisation has no milestone (UN80 dashboard data) | High (dashboard); budget cuts in WS1 *are* quantified in budget documents |
| CBO/BOS without rule alignment adds work | Author's field observation; needs measurement (staff-hours in BOS/UN INFO reporting vs realised savings) | **Low until measured** → priority evidence gap |

---

## 1. Start from purpose: what only the UN can do

Design follows function. Split everything the system does into two kinds of work:

| A. Irreplaceable (needs universality, legitimacy, neutrality) | B. Replaceable (others can do it as well or better) |
|---|---|
| Universal norm and treaty making; technical standards (aviation, telecoms, post, health regulations, statistics) | Generic project implementation that governments, MDBs or NGOs already do |
| Authorising collective security; mediation; neutral convening | Back-office transactions (payments, payroll, travel, procurement execution) |
| Protection mandates where states fail (refugees, humanitarian access) | ICT, premises, fleet, logistics as commodities |
| Global public-goods coordination (pandemics, climate science, data standards) | Consulting-type advisory services available on the market |
| Last-resort operations in fragile and contested settings | |

**Design rule:** A-functions are judged on **legitimacy, reach and reliability** and funded predictably (assessed or core). B-functions are judged on **unit cost and quality against the market** and run as one shared utility or bought in. This is where "Goldman-level" efficiency belongs. Most of today's fragmentation sits in B, but it is defended in the language of A ("our mandate requires our own system").

---

## 2. Design principles (each one a test against today)

| # | Principle | Today | Why it is the leverage |
|---|---|---|---|
| P1 | **Separate what from how.** Member states set purpose, mandates, budget envelope, risk appetite and leaders' accountability. Management decides how. | Boards and the Fifth Committee approve posts and operational rules; management cannot change rules without N intergovernmental decisions | Removes the main source of slow decisions; standard in every high-performing governance model |
| P2 | **One decision, one owner.** Every recurring decision type has a single accountable decider and a defined route (RAPID/RACI). | Diffuse: OMT, UNCT, HQ, board, auditors each partly decide | Makes decision time measurable and blame-free escalation possible |
| P3 | **Decide once, apply everywhere** (the key operational lever). Each governing body adopts one identical "enabling-services delegation" decision: the entity follows system-wide operating rules for finance, procurement, HR, ICT and data unless that body grants a time-limited exception. | Each harmonisation needs ~40 separate decisions, each time | Converts recurring N-decision negotiations into a one-time N decisions; mirrors EU mutual recognition and minimum harmonisation |
| P4 | **Rules before structures; data before reporting.** Sequence: (1) common or mutually recognised rules → (2) one data standard → (3) consolidate services → (4) reconfigure presence. | CBOs and mergers launched before rules and systems align | Your field point: consolidation without rule alignment adds a layer. Sequencing is the fix |
| P5 | **Shared by default, comply or explain.** B-functions use the certified common provider unless an exception is justified publicly with a cost case. | Opt-in, voluntary | Defaults drive behaviour more than exhortation |
| P6 | **Money follows decisions.** Whoever decides holds the budget. Earmarking allowed only at full, harmonised cost recovery with reporting through the common standard, so it costs more than core. | Earmarking is cheaper for donors and carries bespoke reporting | Root incentive behind competition, branding and parallel systems |
| P7 | **Report once, from systems; every report names its decision.** No manual report unless a named decision-maker uses it; reports are generated from transactional data; unused reports sunset automatically. | BOS, UN INFO and donor reporting hand-compiled yearly, little traceable use | Cuts burden fast; turns reporting into a management tool |
| P8 | **Mandates and structures expire by default.** Sunset and full costing at creation; renewal requires evidence of use or results. | Mandates accumulate (UN80 Mandate Implementation Review) | Entropy control: the only reliable way old structures shrink |
| P9 | **Publish unit costs and decision times.** Comparable by entity and country; independent validation. | Not published (Tier C) | Creates pressure without a vote; prerequisite for P5 and P6 |
| P10 | **Design for average leaders.** Rules and data must work without a heroic SG or ED. | Reforms depend on individual champions and fade with turnover | Durability |

---

## 3. Target decision architecture

```
L1  LEGITIMACY (universal, slow, rare)
    GA · Security Council · specialised-agency assemblies
    Decide: purposes, norms, mandates (with sunset + cost), resource envelope, leader selection & evaluation
        │  delegates "how" once (P1, P3)
L2  SYSTEM STEWARDSHIP (few bodies, binding on B-functions)
    One operational board for funds & programmes (or joint board with binding joint decisions)
    CEB/HLCM converted from coordination forum to standard-setter for B-functions (P3, P5)
    Decide: common operating rules, data standard, cost-recovery rate, certified service providers
        │
L3  MANAGEMENT (clear owners, compacts)
    SG / EDs / USGs: compacts with entity KPIs + system KPIs (unit cost, decision time, shared-service uptake)
        │
L4  SHARED OPERATING PLATFORM (B-functions as a utility)
    One rulebook · interoperable systems on one data standard · providers with published prices and SLAs
        │
L5  COUNTRY (one presence, many mandates)
    One accountable country leader for the platform; entities as programme units;
    long-tail presences (< $5m) served from hubs or as non-resident
    ─────────────────────────────────────────────
    INFORMATION SPINE: report once from systems (P7) · public unit costs & decision times (P9)
    OVERSIGHT: single audit / mutual reliance across entities
```

---

## 4. Leverage points ranked (impact × feasibility × who can act)

| Lever | Leverage level | Who can act (no Charter change needed) | Feasibility | Time to effect |
|---|---|---|---|---|
| **Donor coalition compact**: top ~10 capitals (64–75% of government earmarked money) shift to pooled/core funding with one common reporting standard | Incentives / rules | ~10 governments; no UN vote required | Medium (politically hard, but a small group) | 1–2 years |
| **"Decide once" enabling-services delegation** (P3) by each executive board and assembly | Decision rights | Boards (whose members overlap heavily with the donor coalition) | Medium | 2–3 years |
| **Report-once / sunset rule** (P7) | Information flows | SG + CEB for system reporting; boards for their own | High | < 1 year (quick, visible win) |
| **Public unit costs and decision times** (P9) | Information flows | CEB / HLCM; can start independently from public data | High | < 1 year |
| **Mutual reliance in audit** | Rules | Board of Auditors / OIOS / entity audit committees + boards | Medium | 1–2 years |
| **Single operational board for funds and programmes** | Structure / decision rights | GA + ECOSOC | Low–Medium | 3–5 years |
| **Mandate sunset by default** (P8) | Rules | GA (A/RES/80/251 is a start) | Medium | Ongoing |
| Mergers / CBO rollout without the above | Parameters / structure | SG + boards | Medium | High cost, low leverage unless sequenced after the rules |

**Main reframing for decision-makers:** the fastest high-leverage actor is not inside the UN. It is the ~10 capitals that provide most earmarked money and also sit on the boards that set the rules.

---

## 5. Stress tests: does the design survive the long run?

| Scenario | Today's system | Target design | Lesson from long-lived institutions |
|---|---|---|---|
| Major funder withdraws (happened 2025) | Earmarked-dependent entities shrink chaotically; each cuts separately | Core and assessed floor for A-functions; shared B-platform scales down once, not 40 times | Diversified, rule-based funding outlasts patronage |
| Great-power deadlock (Security Council paralysis) | Political crisis bleeds into everything | Technical A-functions and the B-platform are insulated from political organs | UPU (1874) and ITU (1865) survived world wars and the Cold War: narrow, mutually beneficial technical mandates |
| Technology shift (AI automating back office) | 40 separate upgrades, 40 procurement cycles | One platform upgrade benefits all | Common standards compound; fragmentation multiplies cost |
| Pandemic / climate shock | Ad hoc surge, competing appeals | Pre-delegated emergency authority and pooled surge (as CERF and IHR emergency declarations do) | Pre-agreed rules beat negotiation in crisis |
| Leadership quality varies | Reforms fade with champions | P10: rules and published data carry the reform | Durable institutions are rule-based, not person-based |
| Mandate creep over decades | Accumulation, never pruned | P8 sunset by default | Institutions that can shed functions survive longer |
| Membership and power shifts | Legitimacy contested | A-functions stay universal; B-platform is neutral infrastructure | League of Nations: lost legitimacy when great powers exited and enforcement failed |

---

## 6. What we must still prove (evidence agenda)

1. **Coordination tax:** staff-hours per year spent on BOS, CBO, OMT and UN INFO reporting, set against realised (not projected) savings. Method: structured survey of OMT chairs and BOS focal points plus existing BOS cost-benefit analyses. _Highest-value evidence gap; also your strongest insider contribution._
2. **Rule divergence matrix:** for the top 10 operational rules (procurement thresholds, contract committees, delegation of authority, cost recovery, HR contract types), how many distinct versions exist across entities. Source: public financial regulations and procurement manuals.
3. **Decision-time baseline:** days from need to decision for 3–4 tracer processes (procure, hire, approve a joint programme, change a common service).
4. **Long-tail overhead:** CEB expenses × HR duty-station data to estimate fixed cost per presence.
5. **Reform post-mortem:** Delivering as One, the 2018 reform (efficiency target vs realised), mutual recognition uptake, BOS 2.0 results.
6. **Counter-evidence:** where the voluntary model *did* work (e.g., common premises in some countries, global service centres), and why.

---

## 7. How to communicate it (for an internal and expert audience)

- Not "UN80 failed". Instead: **"UN80's direction is largely right; its mechanism is missing. Without rules, money and decision rights moving first, consolidation adds work on the ground."** This is harder to dismiss, harder to resent, and backed by UN80's own data.
- Lead with one number (the coordination tax or the long tail), one diagram (L1–L5) and one ask per decision-maker (the decision-rights map).
