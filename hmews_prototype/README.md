# HMEWS — Human Molecular Early-Warning System

Research prototype v0.1. This is NOT a medical diagnostic system.

The prototype learns an individual's baseline from longitudinal virtual biomarkers and detects unusual multi-marker trajectories.

Run:
`pip install -r requirements.txt`
`python train_demo.py`

Outputs: demo_sensor_data.csv, anomaly_results.csv, anomaly_plot.png, model.joblib.

Future real-data schema: patient_id, timestamp, heart_signal, liver_signal, kidney_signal, inflammation_signal, infection_signal.

Real datasets should be mapped into this intermediate schema only after checking units, sampling frequency, labels, population differences, leakage and access/licensing conditions.
