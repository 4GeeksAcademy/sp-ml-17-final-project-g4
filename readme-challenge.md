# Machine Learning Final Project

This is the final project of our Machine Learning bootcamp, where we demonstrate the skills and knowledge acquired throughout our studies.  
Throughout this bootcamp, we have worked with different models and data types, developing solutions for various domains.  
Now it's time to design, implement, and deploy our own project using the algorithm(s) best suited to our problem.

*"Hard work always beats talent when talent doesn't work hard"* – Tim Notke

---

## 👥 Credits
**Team Members**:  
- José Vicente Vareles Martínez  

**Academy:** 
> - [4Geeks Academy](https://4geeksacademy.com/us/index) 
> - **Bootcamp:** Spain-DS-17 
> - **Mentor:** [Ing. Héctor Chocobar Torrejón](https://github.com/hchocobar/)
> - **Teacher Assitant:** [Beatriz Solana Ros](https://github.com/mezcolantriz)

---

## 🎯 Challenge Goal

Develop a predictive model that determines the risk of imminent failure for Component X in Scania trucks, based on operational time series data and vehicle specifications. The model must output a risk class (0–4) for each vehicle, indicating windows of imminent failure.

---

## 🚀 Overview

### Problem Statement

Given anonymized operational readouts (sensor/counter data, histograms) and vehicle specification features, predict for each truck its risk window for Component X failure:
- **Classes:**
  - **0:** No imminent failure
  - **1:** 48–24 time units before failure
  - **2:** 24–12 time units before failure
  - **3:** 12–6 time units before failure
  - **4:** 6–0 time units before failure

Predictions must be made for a single "current snapshot" per vehicle (i.e., up to the last available readout).

### Dataset

- **Operational Readouts:** Time series & histogram features, anonymized.
- **Vehicle Specifications:** Categorical features (engine type, wheel config, etc.).
- **Train Set:** Full time series per vehicle, with failure/repair labels.
- **Validation/Test:** Data up to a randomly selected "last readout" per vehicle.
- **Test:** No labels provided; predictions must cover all vehicles in test set.

### Evaluation

- **Metric:** Cost-based penalty system
  - **Late/Missed Alarms:** High cost (200–500 per missed failure)
  - **False Alarms:** Lower cost (7–10 per unnecessary check)
- **Goal:** Minimize total cost (not simply maximize accuracy)

---

## 📝 Workflow & Methodology

### 1. Data Preparation
- Aggregate time series and histogram features up to each vehicle's last readout.
- One-hot encode categorical specs.
- Feature engineering: trends, last values, statistical summaries, etc.

### 2. Model Development
- Train cost-sensitive classifiers (e.g., LightGBM, XGBoost, CatBoost, or deep learning if appropriate).
- Tune thresholds for minimum expected cost using validation set.
- Experiment with ensemble approaches and calibration.

### 3. Evaluation
- Simulate test scenario on validation set (current snapshot per vehicle).
- Optimize for cost, not just class accuracy.

### 4. Submission
- **Predictions:** CSV file, one line per test vehicle, format:
  ```
  vehicle_id,predicted_class
  12345,2
  12346,0
  ```
- **Paper:** Written report detailing methodology, experiments, and insights (conference template).

---

## 📁 Project Structure

```
ida-2024-industrial-challenge/
├── data/                # Raw and processed datasets
│    ├── interim/        # Intermediate transformed data
│    ├── processed/      # Final modeling data
│    ├── raw/            # Unprocessed originals
├── models/              # Trained model artifacts
├── notebooks/           # Jupyter notebooks for EDA and modeling
├── src/                 # Source code modules
├── submissions/         # Submission CSVs and report
├── docs/                # Documentation and challenge materials
├── webapp/              # (Optional) Application for demo/visualization
```

---

## 🛠️ Technologies Used

- Python (Pandas, NumPy, scikit-learn, LightGBM/XGBoost/CatBoost, etc.)
- Jupyter Notebook
- (Optional) Flask/Streamlit for web app
- SQL database for data storage (if needed)

---

## 📊 Results

*To be updated with model performance, insights, and cost metric achieved on validation/test sets.*

---

## 🌐 Live Demo

*Link to be added if a web application is deployed for visualization or model serving.*

---

## 📄 References

- [IDA 2024 Industrial Challenge Description](https://doi.org/10.5878/bnh5-ka77)
- Scania truck predictive maintenance data (see challenge link for access)
