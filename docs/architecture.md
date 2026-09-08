# Architecture

1. **Stage 0 - Data & Label Schema Lock-in**: confirm Zenodo annotations are
   panel boxes; define PVF-10 label mapping.
2. **Stage 1 - Panel Detector**: YOLO-family model trained on Zenodo panel
   boxes to localize each PV panel.
3. **Stage 1.5 - Hotspot Proposal**: grayscale/HSV contrast thresholding
   within each detected panel crop; connected components -> candidate boxes.
4. **Stage 2 - Artifact Classifier**: candidate crop -> likely_fault /
   likely_reflection / likely_occlusion / uncertain.
5. **Decision Layer**: aggregate per-panel candidate classifications into a
   3-tier maintenance priority (A: dispatch, B: re-fly, C: monitor).
6. **Report Generator**: produces a CSV/PDF maintenance report with
   evidence crops and priority ranking.
