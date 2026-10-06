# HMEWS Data

This directory contains documentation and references for datasets used
by the Human-Molecular Early Warning System (HMEWS).

## Repository Policy

Raw clinical, genomic or other restricted datasets are not stored in
this GitHub repository.

Instead, this directory provides:

- Dataset names and versions
- Official dataset URLs
- Access requirements
- License information
- Dataset usage notes
- Reproducibility guidance

## Dataset Sources

See [sources.md](./sources.md) for the complete dataset source list.

## Expected Local Structure

When datasets are obtained through their official sources, they may be
stored locally using a structure similar to:

data/
├── raw/
│   ├── mimic/
│   └── geo/
├── processed/
└── README.md

The `raw/` and other sensitive/generated data directories should remain
excluded from Git where appropriate.
