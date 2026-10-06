import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import joblib
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

RANDOM_STATE = 42
rng = np.random.default_rng(RANDOM_STATE)


def generate_virtual_patient(days=240):
    day = np.arange(days)
    df = pd.DataFrame({
        "patient_id": "P001",
        "timestamp": pd.date_range("2026-01-01", periods=days, freq="D"),
        "heart_signal": rng.normal(0.20, 0.025, days),
        "liver_signal": rng.normal(0.25, 0.030, days),
        "kidney_signal": rng.normal(0.22, 0.025, days),
        "inflammation_signal": rng.normal(0.15, 0.020, days),
        "infection_signal": rng.normal(0.10, 0.015, days),
    })
    abnormal = day >= 175
    severity = np.clip((day - 174) / 65, 0, 1)
    df.loc[abnormal, "inflammation_signal"] += 0.35 * severity[abnormal]
    df.loc[abnormal, "liver_signal"] += 0.16 * severity[abnormal]
    df.loc[abnormal, "heart_signal"] += 0.08 * severity[abnormal]
    return df


def add_personal_baseline_features(df, features, baseline_days=60):
    out = df.copy()
    baseline = out.iloc[:baseline_days][features].mean()
    std = out.iloc[:baseline_days][features].std().replace(0, 1e-6)
    for feature in features:
        out[f"{feature}_z"] = (out[feature] - baseline[feature]) / std[feature]
    return out


def train_detector(df, z_features):
    scaler = StandardScaler()
    X = scaler.fit_transform(df[z_features])
    model = IsolationForest(n_estimators=300, contamination=0.08, random_state=RANDOM_STATE)
    model.fit(X)
    result = df.copy()
    result["anomaly_score"] = -model.decision_function(X)
    result["anomaly"] = np.where(model.predict(X) == -1, "INVESTIGATE", "NORMAL")
    return result, scaler, model


def main():
    raw = generate_virtual_patient()
    raw.to_csv("demo_sensor_data.csv", index=False)
    features = ["heart_signal", "liver_signal", "kidney_signal", "inflammation_signal", "infection_signal"]
    engineered = add_personal_baseline_features(raw, features)
    z_features = [f"{x}_z" for x in features]
    result, scaler, model = train_detector(engineered, z_features)
    result.to_csv("anomaly_results.csv", index=False)
    joblib.dump({"scaler": scaler, "model": model, "features": features, "z_features": z_features}, "model.joblib")

    fig, ax = plt.subplots(figsize=(12, 6))
    for col in ["inflammation_signal", "liver_signal", "heart_signal"]:
        ax.plot(result["timestamp"], result[col], label=col)
    abnormal = result["anomaly"] == "INVESTIGATE"
    ax.scatter(result.loc[abnormal, "timestamp"], result.loc[abnormal, "inflammation_signal"], label="AI anomaly")
    ax.set_title("HMEWS — Virtual Molecular Sensor Trajectory")
    ax.set_xlabel("Date")
    ax.set_ylabel("Virtual signal")
    ax.legend()
    fig.tight_layout()
    fig.savefig("anomaly_plot.png", dpi=160)
    plt.close(fig)
    print(result.tail(15).to_string(index=False))


if __name__ == "__main__":
    main()
