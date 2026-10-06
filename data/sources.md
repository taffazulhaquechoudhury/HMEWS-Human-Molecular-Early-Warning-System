# HMEWS Dataset Sources

This document lists the datasets used or planned for the
**Human-Molecular Early Warning System (HMEWS)** project.

---

## 1. MIMIC-IV Clinical Database Demo

**Purpose:**  
Used for initial development, testing, clinical feature engineering,
and validation of the HMEWS pipeline.

**Dataset:**  
MIMIC-IV Clinical Database Demo v2.2

**Official Source:**  
https://www.physionet.org/content/mimic-iv-demo/2.2/

**Access:**  
Open access subject to the dataset license and terms of use.

**License:**  
Open Data Commons Open Database License (ODbL) v1.0.

---

## 2. MIMIC-IV Clinical Database

**Purpose:**  
Used for larger-scale clinical/EHR modeling and longitudinal patient
trajectory analysis.

**Dataset:**  
MIMIC-IV v3.1

**Official Source:**  
https://www.physionet.org/content/mimiciv/3.1/

**Access:**  
Credentialed access through PhysioNet.

**Important:**  
The raw MIMIC-IV dataset must not be uploaded to this GitHub repository.
Users should obtain the dataset directly from PhysioNet and comply with
the applicable Data Use Agreement.

---

## 3. NCBI Gene Expression Omnibus (GEO)

**Purpose:**  
Used as a source of publicly available gene-expression and molecular
datasets for the molecular component of HMEWS.

**Official Source:**  
https://www.ncbi.nlm.nih.gov/geo/

**Access:**  
Publicly available datasets, subject to the terms applicable to
individual datasets.

---

## 4. UK Biobank

**Purpose:**  
Potential source for large-scale longitudinal health, biomarker,
proteomic, metabolomic, and genetic data.

**Official Source:**  
https://www.ukbiobank.ac.uk/use-our-data/apply-for-access/

**Access:**  
Application and approval required.

**Important:**  
UK Biobank data must not be uploaded to this repository.

---

# Dataset Usage Policy

The HMEWS repository stores dataset metadata, source links,
documentation, and preprocessing code.

Raw restricted datasets are **NOT included** in this repository.

Users should obtain restricted datasets directly from their official
providers and comply with all applicable:

- Dataset licenses
- Data Use Agreements
- Privacy requirements
- Ethical requirements
- Data-sharing restrictions

---

# Reproducibility

To reproduce the HMEWS experiments:

1. Obtain the required datasets from their official sources.
2. Place the datasets in the appropriate local data directory.
3. Follow the preprocessing instructions provided in the project.
4. Run the preprocessing and feature-engineering pipelines.
5. Train and evaluate the HMEWS models using the documented
   configuration.

Dataset files should not be committed to this GitHub repository unless
their license explicitly permits redistribution.
