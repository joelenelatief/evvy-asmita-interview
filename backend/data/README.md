# Sample data

These are exports from Evvy's (fictional) legacy lab system. You will migrate
them into your new schema as part of the interview (see `CONTEXT.md` in the
repo root).

- `legacy_test_results.csv` — per-marker test results (Part 1).
- `microbiome_composition.csv` — per-organism relative-abundance percentages for
  completed vaginal-health kits (Part 2).

## legacy_test_results.csv

One row per **marker result**. A single physical test kit (identified by
`barcode`) screens for many markers, so each kit appears across multiple rows.

| column | notes |
| --- | --- |
| `barcode` | identifier for the physical test kit. Repeats once per marker. |
| `patient_name` | free-text patient name. The same patient can appear under multiple kits. |
| `patient_email` | the most reliable way to identify a unique patient. |
| `patient_dob` | patient date of birth (`YYYY-MM-DD`). |
| `clinic_name`, `clinic_state` | where the kit was ordered/processed. |
| `test_type` | `sti` or `vaginal-health`. Each type screens a different set of markers. |
| `marker` | the specific thing measured (e.g. `chlamydia`, `lactobacillus`). |
| `result` | `sti`: `positive` / `negative`. `vaginal-health`: `high` / `moderate` / `low` / `not-detected`. Empty when the kit is still in progress. |
| `status` | `in-progress` or `complete`. In-progress kits have empty results. |
| `sample_taken_at`, `results_completed_at` | timestamps; `results_completed_at` is empty until complete. |

### Things worth noticing

- The current `TestResult` model (`backend/test_results/models.py`) stores a
  single `is_positive` boolean per row. It cannot represent a kit that screens
  several markers, nor a patient who takes multiple kits over time. That gap
  is the point of the exercise.
- `result` is not a clean boolean: `vaginal-health` returns graded abundance
  levels, not positive/negative.
- Patient identity is spread across `patient_name` / `patient_email` /
  `patient_dob` and repeated on every row — classic redundancy to normalize.
- Roughly a quarter of kits are still `in-progress` with no results yet.

## microbiome_composition.csv

One row per **organism (taxon) within a kit**, giving its relative abundance as
a percentage. Only **completed vaginal-health kits** appear here.

| column | notes |
| --- | --- |
| `barcode` | the kit; joins to `legacy_test_results.csv` on `barcode`. |
| `patient_email` | included for convenience; the kit already implies the patient. |
| `taxon` | the organism measured, e.g. `Lactobacillus crispatus`, `Gardnerella vaginalis`. |
| `relative_abundance_pct` | percentage (two decimals). The values for a single kit sum to ~100. |

Things worth noticing:

- This is a **separate, more granular readout** than the coarse
  high/moderate/low buckets in `legacy_test_results.csv`. You are not expected to
  reconcile the two — model both cleanly.
- The organisms here are finer-grained than the Part 1 markers (e.g.
  `Lactobacillus` is split into species), which is worth considering when you
  decide whether organisms are shared reference data.
- Per-kit percentages sum to ~100, which suggests a constraint worth thinking
  about.
- Patients with more than one completed vaginal-health kit (e.g. Priya Patel,
  Grace Adams) show a clear shift in composition between kits — useful for the
  Part 4 comparison-over-time view.

The numbers, names, and clinics are entirely synthetic.
