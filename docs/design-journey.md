# Design Journey

## 1. The Idea
UAV thermal imagery + deep learning to localize PV panel anomalies for
maintenance triage. Motivated by sustainability (earlier fault detection ->
more clean kWh, longer panel life, less e-waste) and safety (no humans on
rooftops).

## 2. Technical Pipeline v1
Original vision: flight -> preprocessing -> labeling -> model -> maintenance
decision. Clean on paper; each stage got more complicated in practice.

## 3. Constraints Lock In
- Bounding boxes only (segmentation too expensive to label)
- 8-bit colorized thermal only (radiometric data unavailable publicly)
- Deliverable scoped to a maintenance report, not real-time alerting

## 4. The Critical Flaw
Can the model tell a real electrical fault from an environmental
false-positive (glare, birds, shading)? Not fully solved in the literature,
especially without radiometric data. Mitigations: temporal consistency
checks (where data allows), a second lightweight artifact classifier, and
human-in-the-loop triage.

## 5. Regulatory Reality-Check
Flying a real drone over a real PV farm would require CASA flight
authorisation, landowner permission, safety risk assessment, and
university ethics review. Feasible in principle, out of scope for this
project -- hence the pivot to public datasets.

## 6. Pivot to Public Datasets
Sidesteps flight regulations but not licensing, attribution, or privacy
terms. Every dataset still requires due diligence.

## 7. Dataset Selection
- Zenodo UAV Thermal PV (DOI 10.5281/zenodo.16420123): public, detection-ready
- PVF-10: promising taxonomy, license pending confirmation
- Sense-Solar: dropped, no confirmed public access

## 8. Draft Plan v1
Two-stage architecture: Stage 1 detects hotspots directly on Zenodo,
Stage 2 classifies crops using PVF-10.

## 9. The Reality Check
Caught before implementation: Zenodo's ~26,678 annotations are PANEL boxes,
not HOTSPOT boxes. Training a hotspot detector on panel labels would have
been the wrong task entirely.

## 10. The Fix (Option A)
Reframe Stage 1 as a panel detector (uses Zenodo exactly as labeled), add
Stage 1.5 to propose hotspot candidates within each panel crop via
grayscale/HSV contrast thresholding (no extra labels needed), keep Stage 2
and the decision layer unchanged.

## Lesson
Understand your data before you build on it. Catching a label mismatch in
planning, not after weeks of training, is the entire point of validating
assumptions early.
