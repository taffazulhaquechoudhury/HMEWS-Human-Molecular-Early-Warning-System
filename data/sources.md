# HMEWS Dataset Sources

This document lists the datasets used or planned for the
**Human-Molecular Early Warning System (HMEWS)** project.

The HMEWS project combines longitudinal clinical information with
molecular and biomarker information to investigate early-warning
patterns and changes in an individual's health trajectory.

---

## 1. MIMIC-IV Clinical Database Demo

**Purpose:**  
Used for initial HMEWS development, pipeline testing, clinical feature
engineering, experimentation, and validation of the prototype.

**Dataset:**  
MIMIC-IV Clinical Database Demo v2.2

**Official Source:**  
https://www.physionet.org/content/mimic-iv-demo/2.2/

**Provider:**  
PhysioNet / MIT Laboratory for Computational Physiology

**Access:**  
Available through PhysioNet subject to the applicable dataset terms.

**Usage in HMEWS:**  
The demo dataset can be used during early development to validate data
loading, preprocessing, feature engineering, model training, and
evaluation workflows before moving to larger datasets.

**Important:**  
The dataset itself is not stored in this GitHub repository.

---

## 2. MIMIC-IV Clinical Database

**Purpose:**  
Used as a potential primary clinical/EHR data source for larger-scale
experimentation and longitudinal patient trajectory modeling.

**Dataset:**  
MIMIC-IV v3.1

**Official Source:**  
https://www.physionet.org/content/mimiciv/3.1/

**Provider:**  
PhysioNet / MIT Laboratory for Computational Physiology

**Access:**  
Credentialed access is required.

**Usage in HMEWS:**  
Potential use includes:

- Longitudinal patient records
- Vital signs
- Laboratory measurements
- Diagnoses
- Procedures
- Medications
- Clinical events
- Patient trajectory analysis

**Important:**  
MIMIC-IV is not included in this GitHub repository. Researchers must
obtain the dataset directly from PhysioNet and comply with the applicable
Data Use Agreement and access requirements.

---

## 3. NCBI Gene Expression Omnibus (GEO)

**Purpose:**  
Provides publicly available molecular and gene-expression datasets that
can support the molecular component of HMEWS.

**Dataset Repository:**  
NCBI Gene Expression Omnibus (GEO)

**Official Source:**  
https://www.ncbi.nlm.nih.gov/geo/

**Provider:**  
National Center for Biotechnology Information (NCBI)

**Access:**  
Publicly accessible, subject to the terms and conditions applicable to
individual datasets.

**Usage in HMEWS:**  
Potential use includes:

- Gene-expression profiles
- Molecular signatures
- Differential-expression analysis
- Disease-associated molecular patterns
- Biomarker discovery
- Molecular feature engineering

Individual GEO studies should be documented separately when they are
selected for HMEWS experiments.

---

## 4. UK Biobank

**Purpose:**  
Potential future source of large-scale longitudinal health,
biomarker, proteomic, metabolomic, and genetic information.

**Official Source:**  
https://www.ukbiobank.ac.uk/use-our-data/apply-for-access/

**Provider:**  
UK Biobank

**Access:**  
Application and approval are required.

**Potential Usage in HMEWS:**  
Potential applications include:

- Biomarker analysis
- Proteomics
- Metabolomics
- Genetics
- Longitudinal health information
- Risk-factor analysis
- Population-level validation

**Important:**  
UK Biobank data must not be uploaded to this GitHub repository.
Access and use must follow UK Biobank's applicable policies and
research requirements.

---

# Dataset Selection Strategy

The HMEWS development pipeline is designed to progress through
different levels of data availability:

### Stage 1 — Prototype Development

Use:

**MIMIC-IV Clinical Database Demo**

Purpose:

- Validate the software pipeline
- Test preprocessing
- Build initial features
- Test model architecture
- Validate data-processing workflows

### Stage 2 — Clinical Model Development

Use:

**MIMIC-IV**

Purpose:

- Increase dataset size
- Perform longitudinal analysis
- Develop more robust clinical features
- Train and evaluate early-warning models

### Stage 3 — Molecular Integration

Use:

**NCBI GEO**

Purpose:

- Introduce molecular features
- Investigate gene-expression patterns
- Develop molecular signatures
- Explore relationships between clinical and molecular signals

### Stage 4 — Large-Scale Validation

Potentially use:

**UK Biobank**

Purpose:

- Large-scale validation
- Biomarker integration
- Population-level analysis
- Longitudinal modeling

---

# Dataset Usage Policy

The HMEWS GitHub repository stores:

- Dataset metadata
- Dataset source links
- Dataset versions
- Documentation
- Data-processing code
- Feature-engineering code
- Model-training code
- Reproducibility instructions

The repository does **NOT** store restricted or credentialed-access
raw datasets.

Users must obtain restricted datasets directly from their official
providers.

All users are responsible for complying with:

- Dataset licenses
- Data Use Agreements
- Privacy requirements
- Ethical requirements
- Institutional requirements
- Data-sharing restrictions

---

# Reproducibility

To reproduce HMEWS experiments:

1. Obtain the required dataset from its official source.
2. Confirm that the appropriate access requirements have been completed.
3. Place the dataset in the local data directory.
4. Run the HMEWS preprocessing pipeline.
5. Generate the required features.
6. Run the model-training pipeline.
7. Evaluate the model using the documented evaluation procedure.

Raw datasets should not be committed to this GitHub repository unless
their applicable license explicitly permits redistribution.

---

# Dataset Citation

When publishing results based on these datasets, users should cite the
original dataset and its associated publication according to the
requirements of the dataset provider.

The exact dataset version used for each HMEWS experiment should also be
recorded to ensure reproducibility.

---

## Disclaimer

HMEWS is a research prototype and is **not a medical diagnostic system**.

Dataset availability does not imply clinical validity, diagnostic
accuracy, or suitability for medical decision-making.
