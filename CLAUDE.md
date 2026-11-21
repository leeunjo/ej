# Project context for Claude

This repo holds a business analysis of the UN system's operating model: where efficiency is lost, why fragmentation persists, which leverage points would fix it, and who has the authority to make each change. A website / collaborative wiki comes later.

Start every session by reading `docs/00-project-brief.md`, especially the decision log.

## Rules
- Public sources only. Cite every claim (document symbol / dataset / URL + access date) and give it a confidence level.
- The author is a current UN staff member. Name positions and bodies, not individuals. Keep the framing on system design, not blame.
- Do not state figures from memory. Verify them against sources, or mark them "to verify".
- Store structured data under `data/` (raw downloads in `data/raw/`, untouched) and keep diagrams as text (Mermaid) under `models/`, so the website can be generated from them.
