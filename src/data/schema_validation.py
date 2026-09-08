"""Annotation schema validation.

This module exists because of a real mistake caught during planning:
the Zenodo dataset's ~26,678 annotations are PANEL boxes, not HOTSPOT
boxes. Always validate what a dataset's labels actually represent
before building a pipeline around an assumption.
"""
