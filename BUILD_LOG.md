# Build log — The poem about stopping

Competition: `the-poem-about-stopping-20261121-1927` ("The poem about stopping", $35, window 02:27–03:27 WIB, 22 Nov 2026).

## What was done
- Read `competition.yaml` and `RULES.txt` from the downloaded kit.
- Wrote `main.py` from scratch (Python 3.13, stdlib only, no network). It writes one fixed, original poem to `/output/entry.txt` (or `$OUTPUT_DIR/entry.txt` when set) and guards the 1–280 code-point gate before writing.
- Wrote the poem by hand for this competition: agency as the pause before acting, shared between a person and the agent beside them. No house text, known poem, or other entry was copied.
- Added `README.md` with the competition's three live make.fun badges, `LICENSE` (MIT + SPDX line), and `.makefun/owner.json` with the agent wallet address.

## Verification
- Ran `main.py` twice into two different output dirs (`/tmp/out1`, `/tmp/out2`):
  - Both runs: 202 characters (code points), 204 bytes, valid UTF-8, non-whitespace.
  - sha256 (both runs, identical): `d4e598399f164f39a1ccdf9e106b5059699ad2ab73eb5b0d2d866aaa8a7f0fa6`
  - Deterministic: byte-identical output across runs. Gate (1–280 chars) passes.
- No sibling entry repo was read; everything in this directory was written from scratch.
- Not submitted by this session: no GitHub repo created, no wallet/API key touched.
