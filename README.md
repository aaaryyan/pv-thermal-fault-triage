# PV Thermal Fault Triage

UAV thermal imagery + deep learning pipeline for PV panel fault triage.

## Overview
Thermal imagery captured by UAVs can reveal PV panel anomalies (hotspots, cell defects) before they're visible in RGB. This project builds a two-stage detection + classification pipeline that localizes candidate faults and triages them for maintenance, using only public, non-radiometric (8-bit colorized) thermal datasets.

See `docs/design-journey.md` for the full story, including a dataset/task mismatch caught and fixed before implementation began.

## Pipeline
1. **Stage 0** - Data & label schema lock-in
2. **Stage 1** - Panel detector (YOLO-family, trained on Zenodo panel annotations)
3. **Stage 1.5** - Within-panel hotspot proposal (grayscale/HSV contrast thresholding, no extra labels needed)
4. **Stage 2** - Artifact classifier (likely_fault / likely_reflection / likely_occlusion / uncertain)
5. **Decision Layer** - Aggregation into a 3-tier maintenance priority (A: dispatch, B: re-fly, C: monitor)

## Data & Licensing
See `DATA_LICENSES.md`. Datasets are not re-hosted in this repo -- see `data/README.md` for download instructions.

## Limitations
See `docs/limitations.md` -- no radiometric data (no absolute delta-T thresholds), fault-vs-artifact discrimination is an open problem, dataset shift between sources is untested.

## Status
Work in progress -- solo portfolio project.
