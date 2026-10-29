# DataSphere AI: Unified Data Science & AI Portfolio (Projects 01–05)
> *From Raw Data to Intelligent Applications.*

A unified, interactive student portfolio application showcasing five progressive Data Science and Artificial Intelligence projects from **InternCircle**. Built as a cohesive single application powered by **Python, Streamlit, Pandas, Scikit-learn, Plotly, and Joblib**.

---

## 1. Portfolio Architecture & Overview

| Project | Title | Category | Core Tech Stack | Dataset |
|---|---|---|---|---|
| **01** | Exploratory Data Analysis (EDA) on RMS Titanic | Foundation & EDA | Python, Pandas, Seaborn, Matplotlib | RMS Titanic (891 passengers) |
| **02** | Data Visualization with Matplotlib & Seaborn | Visualization | Plotly, Seaborn, Matplotlib | Seaborn Tips (244 checks) |
| **03** | E-Commerce Sales Trend Analysis | Business Analytics | Plotly, Pandas, Pareto Analysis | Synthetic Retail (2,500 orders) |
| **04** | First Machine Learning Classifier | Supervised ML | Scikit-learn, Decision Tree | Titanic Survival (891 passengers) |
| **05** | Streamlit Interactive ML Web App | Deployment & AI | Streamlit, Joblib, Plotly Gauges | Trained Decision Tree Artifact |

### Unified Application Design
- **Single Entry Point:** The entire multi-project portfolio runs from a single unified command: `streamlit run app.py`.
- **State Management & Routing:** Project selection changes view dynamically without reloading separate disconnected websites.
- **Dark Navy Analytics Theme:** Custom CSS injection featuring `#080d1a` deep navy backgrounds, cobalt blue (`#38bdf8`) accents, and responsive layout grids.
- **Verified Metrics Only:** No fabricated visitor numbers, artificial badges, or hardcoded predictions.

---

## 2. Directory Structure

```
DataSphereAI/
├── app.py                      # Main entrypoint with session routing and sidebar
├── requirements.txt            # Unified Python dependencies
├── README.md                   # Comprehensive documentation & CMD execution guide
├── .gitignore                  # Git exclusions for clean repository tracking
├── train_model.py              # Scikit-learn pipeline training and serialization script
├── run.bat                     # Windows CMD one-click launcher
├── data/
│   ├── tips.csv                # Project 02: 244-row authentic Seaborn Tips dataset
│   ├── ecommerce_data.csv      # Project 03: 2,500-order synthetic retail transactions (seed 42)
│   ├── titanic.csv             # Project 04 & 05: 891-row authentic Titanic manifest
│   └── generate_ecommerce.py   # Reproducible generation script
├── models/
│   └── titanic_model.joblib    # Serialized Decision Tree Pipeline & evaluation metadata
└── modules/
    ├── __init__.py
    ├── home.py                 # Landing page (Hero, stats, cards, visual journey, tech stack)
    ├── project1.py             # Project 01: Professional awaiting-guide interface
    ├── project2.py             # Project 02: Interactive Tips EDA & cross-filtering
    ├── project3.py             # Project 03: E-commerce BI, Pareto curve, 3 recommendations
    ├── project4.py             # Project 04: Titanic Decision Tree classifier & overfitting curve
    ├── project5.py             # Project 05: Real-time passenger survival prediction app
    └── utils.py                # Styling, data/model caching, and navigation helpers
```

---

## 3. Windows Command Prompt (CMD) Execution Guide

Follow these exact copyable commands in **Windows Command Prompt** (`cmd.exe`).

> **Important Note on Windows Application Control:**  
> Windows Defender Application Control (WDAC) and AppLocker policies block running C-extension binaries (`.pyd` / `.dll`) from OneDrive folders (`D:\OneDrive\...`). Because all required packages (`streamlit`, `pandas`, `scikit-learn`, `plotly`, `joblib`, `matplotlib`, `seaborn`) are already installed in your trusted system Python (`C:\Users\Aswath\AppData\Local\Programs\Python\Python313`), do **not** activate a local `venv` inside the OneDrive folder. Run directly with system Python.

### Step 1: Open Windows Command Prompt
If you previously activated a virtual environment in your command prompt window, deactivate it first:
```cmd
deactivate
```

### Step 2: Navigate to the Project Folder
```cmd
cd /d "D:\OneDrive\Documents\New folder\DataSphereAI"
```

### Step 3: Train the Machine Learning Classifier Artifact
Train the Scikit-learn Decision Tree pipeline and generate `models/titanic_model.joblib`:
```cmd
python train_model.py
```
*Expected Output:*
```
Baseline Accuracy: 61.45% (Majority Class = 0: Died)
Test Accuracy:     79.33% (+17.88% vs baseline)
Test Precision:    77.59%
Test Recall:       65.22%
Test F1-Score:     70.87%
Saved trained model bundle to models\titanic_model.joblib
```

### Step 4: Launch the Unified Application
```cmd
python -m streamlit run app.py
```

### Step 5: Open in Browser
If your browser does not open automatically, navigate to:
```
http://localhost:8501
```

### Step 6: Stop the Application Safely
In the Command Prompt window running Streamlit, press:
```cmd
Ctrl + C
```
Type `y` when prompted to terminate the batch job.

*(Alternatively, you can simply double-click `run.bat` to launch everything in one click).*

---

## 4. Project Highlights & Analytical Details

### Project 01: Exploratory Data Analysis (EDA) on RMS Titanic
- **Imported directly from InternCircle Project 01 specifications (`Game/PROJECT_DESCRIPTION.md`).**
- **Data Cleaning Protocol:** Subgroup median age imputation across `(pclass, sex)`, mode embarkation imputation (`'S'`), sparse `deck` exclusion, duplicate retention analysis.
- **Three Research Questions Answered:**
  1. *Gender Disparity:* Women achieved 74.20% survival vs. 18.89% for men (+55.31% gap / ~3.93x ratio).
  2. *Ticket Class Gradient:* 1st Class (62.96%), 2nd Class (47.28%), 3rd Class (24.24%).
  3. *Age Cohorts:* Children (0–12) achieved highest survival (57.97%); Seniors (60+) lowest (22.73%).
- **Visuals & Deliverables:** Interactive Plotly tabs, high-resolution Seaborn export (`outputs/titanic_survival_charts.png`), and searchable cleaned data table with CSV export. Zero ML constraint strictly respected.

### Project 02: Data Visualization with Matplotlib & Seaborn
- **Dataset:** 244 receipts, 7 features from the classic Bryant & Smith (1995) study.
- **Dynamic Filtering:** Filter by Day, Meal Time, and Smoker status; metrics and charts recalculate in real-time.
- **5 Interactive Plotly Charts:**
  1. *Distribution of Restaurant Bills:* Histogram with bin slider and Mean/Median vertical threshold lines.
  2. *Average Tip by Day:* Bar chart with exact dollar amounts annotated on bars.
  3. *Distribution of Tips Across Days:* Box plot showing medians, IQR spread, and the \$10.00 Saturday outlier.
  4. *Total Bill vs. Tip Scatter Plot:* Colored by Lunch/Dinner with Ordinary Least Squares (OLS) regression line ($r = 0.676$).
  5. *Correlation Heatmap:* Pairwise Pearson correlation matrix with annotated coefficients.
- **Searchable Table & CSV Export:** Download currently filtered records.

### Project 03: E-Commerce Sales Trend Analysis
- **Dataset:** 2,500 transactions generated reproducibly (fixed seed 42) with retail seasonality.
- **Executive KPIs:** Total Revenue (\$758,221.15), 2,193 Completed Transactions, 271 Unique Customers, \$345.75 AOV.
- **Visualizations:** Monthly Revenue Trend, MoM Growth Rate %, Category Breakdown, Top 10 Customers by spend, Lorenz Pareto 80/20 Curve, Monthly Category Pivot Table.
- **3 Calculated Business Recommendations:**
  1. *VIP Client Retention:* Top 20% of customers drive 68.4% of revenue. Churn proxy defined as >60 days inactivity.
  2. *Category Expansion & Bundles:* Electronics generates 43% of GMV. Target KPI: +12% AOV lift.
  3. *Q4 Inventory Buffer:* Nov & Dec sales total 28% of annual revenue. Target KPI: Maintain OOS < 2%.
- **Downloadable Executive Brief:** Download formatted markdown brief.

### Project 04: First Machine Learning Classifier
- **Dataset:** 891 Titanic passengers, 4 features (`pclass`, `sex`, `age`, `fare`), target `survived`.
- **Data Hygiene:** Median imputation for 177 missing `age` values fitted strictly on the training set.
- **Evaluation:** 80/20 stratified split (712 train, 179 test).
- **Results on Held-Out Test Set:**
  - Baseline Accuracy: 61.45%
  - Test Accuracy: **79.33%**
  - Precision: **77.59%**
  - Recall: **65.22%**
  - F1-Score: **70.87%**
  - Confusion Matrix: TN=97, FP=13, FN=24, TP=45.
- **Overfitting Analysis:** Tree depth sweep from 1 to 12. Explains why `max_depth=3` achieves optimal out-of-sample generalization while depth 12 overfits to training noise.
- **Feature Importance:** Highlights `sex` and `pclass` as primary predictors.

### Project 05: Streamlit Interactive ML Web App
- **Live Inference Engine:** Loads `@st.cache_resource` serialized pipeline from `models/titanic_model.joblib`.
- **Input Parameters:** Ticket Class (1st, 2nd, 3rd), Sex (Female, Male), Age (1–80), Fare (£0–£500).
- **Prediction:** Computes exact probability of survival (`model.predict_proba`).
- **Visuals:** Status box ("Likely to Survive" vs. "Unlikely to Survive") + interactive Plotly gauge meter.
- **Attribution & Download:** Feature impact breakdown and downloadable prediction CSV audit log.

---

## 5. Free Online Deployment Guide (Streamlit Community Cloud)

Streamlit Community Cloud provides 100% free, permanent hosting directly from your GitHub repository.

### Step 1: Initialize Git and Commit
In Windows CMD:
```cmd
cd /d "D:\OneDrive\Documents\New folder\DataSphereAI"
git init
git add .
git commit -m "Initial release of DataSphere AI unified portfolio"
```

### Step 2: Push to GitHub
1. Create a new public repository on [GitHub](https://github.com/new) named `datasphere-ai`.
2. Push your code:
```cmd
git branch -M main
git remote add origin https://github.com/<your-username>/datasphere-ai.git
git push -u origin main
```

### Step 3: Deploy to Streamlit Community Cloud
1. Visit [share.streamlit.io](https://share.streamlit.io/) and log in with your GitHub account.
2. Click **New app**.
3. Select your repository: `<your-username>/datasphere-ai`.
4. Set **Branch:** `main` and **Main file path:** `app.py`.
5. Click **Deploy!**
Your unified portfolio will be live in ~2 minutes at:
`https://<your-app-name>.streamlit.app`

---

## 6. Internship Submission Details

When submitting to your **InternCircle** evaluation dashboard:
- **Project Title:** DataSphere AI: Unified Data Science & AI Portfolio (Projects 01–05)
- **GitHub Repository:** `https://github.com/<your-username>/datasphere-ai`
- **Live Application URL:** `https://<your-app-name>.streamlit.app`
- **Student Name:** Aswath
- **Portfolio Tagline:** *From Raw Data to Intelligent Applications.*
- **Evaluation Highlights:**
  - 5 unified modules under a single Streamlit architecture.
  - Interactive project selection and state management without page reloads.
  - Real calculations across 3 datasets (Tips, E-Commerce, Titanic).
  - Production Scikit-learn ML pipeline with held-out test evaluation (79.33% accuracy).
  - Real-time interactive ML prediction engine with downloadable audit logs.
