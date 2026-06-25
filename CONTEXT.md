# Interview Context: Test Results

This document gives you the lay of the land before we start. Read through it
ahead of time so you're not orienting during the session — we'd rather spend
that time working through problems together.

---

## The product context

Evvy ships at-home vaginal health and STI tests. A customer takes a sample,
mails in the kit, and later sees their results in our app.

The current codebase has a single, deliberately oversimplified `TestResult`
model: one row holds a patient name, one test type, and one `is_positive`
boolean. That worked when every kit returned a single yes/no answer.

**It no longer reflects reality:**

- A single kit screens for **many markers at once**. An STI kit reports on
  chlamydia, gonorrhea, syphilis, HIV, and more — each with its own result. A
  vaginal-health kit reports a panel of microbes, each with a *graded* level
  (`high` / `moderate` / `low` / `not-detected`), not a simple positive/negative.
- A **patient takes multiple kits over time** and will want to see their history.
- The data also carries context we want to keep, like the ordering **clinic**.

You can see all of this in `backend/data/legacy_test_results.csv` (one row per
marker result) and its `backend/data/README.md`.

We're also rolling out a richer **microbiome composition** readout for
vaginal-health kits: instead of a coarse high/moderate/low bucket, the lab now
reports the **relative abundance (a percentage)** of each detected organism, and
those percentages sum to ~100% per kit. That data lives in
`backend/data/microbiome_composition.csv`.

---

## What we'll work on together

During the interview we'll explore some or all of the following areas. You
don't need to have built anything ahead of time — just come familiar with the
codebase and the domain problem described above.

### Relational schema redesign

The single `TestResult` model needs to be replaced with a schema that
faithfully represents the world above. We'll talk through how to model it and
may write some of it live. Things worth thinking about going in:

- How you identify a unique patient given the messy source data.
- How you model the fact that one kit has many marker results, and that
  different test types screen different markers.
- How you represent results that are sometimes a boolean and sometimes a graded
  level.
- Keys, constraints, uniqueness, nullability, and any indexes you'd add (and why).

### Microbiome composition model

The `microbiome_composition.csv` data doesn't fit the marker schema — it's a
per-kit, per-organism relative abundance percentage. We'll talk through how to
model it:

- How an organism (taxon) relates to a kit — is it shared reference data with
  the marker schema?
- The type and precision to store a percentage, and whether/how to enforce that
  values for a kit sum to ~100%.

### API

The existing `TestResultsView` has some notable issues. We may dig into how
you'd rework the API under `backend/api/v1/` to serve a new schema —
endpoint design, filtering, pagination, serialization.

### Frontend — per-patient comparison view

There's a natural end-to-end slice here: pick a patient, show how their
microbiome composition changed across their kits over time. Several patients in
the data have multiple completed vaginal-health kits (e.g. Priya Patel and
Grace Adams) with noticeable shifts between them. We may sketch or build some
of this together.

---

## Notes

- The repo runs on Django + Django REST Framework + Postgres on the backend and
  React + TypeScript on the frontend. See the main `README.md` for setup.
- The stack is fixed, but you're free to suggest libraries — just be ready to
  justify them.
- Think out loud and name trade-offs as you go. That's what we're most
  interested in.
