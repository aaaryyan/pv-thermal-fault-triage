# Limitations

- **No radiometric data**: only 8-bit colorized thermal heatmaps are used,
  so absolute delta-T thresholds are not reliable; all cues are relative/
  appearance-based.
- **Fault vs. artifact discrimination is unresolved**: distinguishing a
  genuine electrical fault from glare, birds, or shading is an open problem
  in the literature, not solved by this project. The system is designed as
  a triage/decision-support tool, not an autonomous diagnostic authority.
- **No multi-pass flight data**: static datasets mean temporal-consistency
  and multi-view-geometry mitigation strategies cannot be fully tested;
  mitigated instead with a manually constructed hard-negative test set.
- **Dataset shift risk**: Zenodo and PVF-10 differ in flight conditions,
  colormaps, and viewpoints; cross-dataset generalization is untested.
- **Hotspot-proposal recall is unquantified**: the Stage 1.5 thresholding
  method may miss faults that don't stand out in simple contrast terms;
  this needs dedicated evaluation.
