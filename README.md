# ITSM Playbook

A system for turning a service desk's ticket history into deterministic issue models: the same issue gets the same questions, the same steps, the same documentation, and the same escalation rule every time.

I built this on my own to map a service desk role that had no documentation. Everything client-specific has been removed. The schemas, method and code are mine; the examples here are generic.

## The method

**1. Find out what actually comes in.** `scripts/coverage_analysis.py` reads an incident export, sets aside automated monitoring alerts (disk space, offline devices, UPS alarms), groups the remaining tickets by their short description, and finds how many issue types it takes to cover:

- 80% of troubleshooting tickets (core)
- 90% (comprehensive)
- 95% (exhaustive)

Models get written in that order, so the first handful cover most of the day.

**2. Write each issue as a model, not a note.** Every model follows the same schema (`TEMPLATES/INCIDENT_TEMPLATE_SCHEMA.md`):

1. Purpose: what the issue is at system level
2. Incident template: fields, short description format, customer-visible description, internal work notes, closure notes
3. When not to use: explicit exclusions
4. Escalation rule: exact criteria
5. Work-note patterns observed in real tickets
6. Data basis: ticket count, share of volume, sample validated, date

**3. Route by exact wording.** A router model (`MODELS/APP_ROUTER.md`) maps the words users actually submit to the right model. No guessing.

**4. Reuse it.** Each model doubles as a knowledge base article (`TEMPLATES/KB_TEMPLATE_SCHEMA.md`) and as structured data. I built an AI call-guidance assistant on top of the playbook that prompts the analyst on what to ask and what to capture during live calls.

## Layout

```
TEMPLATES/   incident and KB schemas every model must follow
MODELS/      example models (generic)
INDEX.md     models grouped by layer
scripts/     coverage analysis and a synthetic sample generator
data/        synthetic sample export
```

## Run the coverage analysis

No dependencies beyond the Python standard library.

```bash
python3 scripts/make_sample_incidents.py            # writes data/sample_incidents.csv (synthetic)
python3 scripts/coverage_analysis.py data/sample_incidents.csv
```

Point it at your own export with `--column` if the description field has a different name.
