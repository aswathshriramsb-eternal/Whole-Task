# PROJECT 02: DATA VISUALIZATION WITH MATPLOTLIB & SEABORN
### Interactive Exploratory Data Analytics Dashboard & Web Application
**Data Science & Full-Stack Development Internship Project**
---

Experience the Whole Task on my Website : [Website Url](https://whole-task-mm89ujjjz449ex3rgdwhpm.streamlit.app/)

---

## 1. Executive Summary

This project delivers an interactive, publication-standard data visualization website built on the benchmark **Seaborn Tips dataset** (Bryant & Smith, 1995). Designed with a modern dark navy and cobalt blue aesthetic, the platform combines the analytical rigor of Python data science (`pandas`, `NumPy`, `Matplotlib`, `Seaborn`, and `Flask`) with responsive web technologies (`HTML5`, `CSS3`, `vanilla ES6+ JavaScript`, and `Plotly.js`).

Unlike static notebooks or basic HTML mockups, this application is a **fully functional, reactive web product** featuring:
- Dynamic calculation of all key summary metrics from the authentic 244 records.
- 5 interactive analytical charts with rich tooltips, legends, and dynamic trend calculations.
- Seamless dual-engine toggle: switch instantly between live browser **Plotly.js** charts and native Python **Seaborn / Matplotlib** figures.
- A searchable, sortable **Data Explorer** with pagination, cross-filters (Day, Meal Time, Smoker Status), and real-time CSV export.
- Dynamic cross-filtering that updates charts and KPI statistics in real-time.

---

## 2. Technology Stack & Architecture

| Layer | Technologies | Role / Description |
|---|---|---|
| **Data Science & Backend** | Python 3.13, Flask 3.1, pandas 3.0, NumPy 2.5 | Statistical computation, correlation matrix, REST API endpoints (`/api/data`, `/api/stats`). |
| **Data Visualization** | Seaborn 0.13, Matplotlib 3.11, Plotly.js 2.29 | Generation of publication-grade static figures in `outputs/` and responsive interactive browser graphics. |
| **Frontend Architecture** | HTML5, CSS3, Vanilla JavaScript (ES6+) | Semantic layout, custom dark navy theme, state management, sorting, pagination, and debounce search. |
| **Typography & Icons** | Inter, Fira Code, Font Awesome 6.5 | Clean typography, tabular numeric formatting, and intuitive iconography. |

### Architecture Diagram
```
┌──────────────────────────────────────────────────────────────────┐
│                         Browser Client                           │
│   index.html + css/style.css + js/app.js + js/plotly.min.js      │
│  - Reactive Dashboard (Histograms, Bar, Box, Scatter, Heatmap)   │
│  - Data Explorer (Search, Filter, Sort, Pagination, CSV Export)  │
└──────────────────┬──────────────────────────▲────────────────────┘
                   │                          │
        HTTP / REST API Requests       JSON Data & Chart Feeds
                   │                          │
┌──────────────────▼──────────────────────────┴────────────────────┐
│                      Python Backend (app.py)                     │
│  - Flask Web Server (Port 5000)                                  │
│  - REST Endpoints: /api/data, /api/stats, /health                │
│  - Static Asset Delivery: /outputs/<chart_images>                │
└──────────────────┬──────────────────────────▲────────────────────┘
                   │                          │
        Data Processing / Pandas       Visual Figure Exports
                   │                          │
┌──────────────────▼──────────────────────────┴────────────────────┐
│             Data Science Engine (generate_charts.py)             │
│  - Authentic Seaborn Tips Dataset (data/tips.csv, 244 records)   │
│  - Matplotlib & Seaborn Chart Generation Engine (outputs/)       │
└──────────────────────────────────────────────────────────────────┘
```

---

## 3. Website Sections & Capabilities

### A. Home / Overview
- **Project Title:** *Data Visualization with Matplotlib & Seaborn*.
- **Dataset Context:** 244 dining party records, 7 variables (3 numerical, 4 categorical), 0 missing values.
- **Dynamic KPI Stat Cards:**
  - **Total Records:** 244 authentic checks.
  - **Numerical Variables:** 3 (`total_bill`, `tip`, `size`).
  - **Average Restaurant Bill:** \$19.79 (Median: \$17.80, Max: \$50.81).
  - **Average Tip:** \$3.00 (Median: \$2.90, Max: \$10.00).
  - **Average Tip Rate:** 16.08% (hospitality industry benchmark).
  - **Peak Tip Day:** Sunday (\$3.26 mean tip per table).

### B. Interactive Analytics Dashboard
1. **Chart 1: Distribution of Restaurant Bills (Histogram)**
   - Explores continuous bill ranges, frequency, and density.
   - Includes Mean (\$19.79) and Median (\$17.80) threshold markers.
   - User-configurable bin selector (15, 20, 25, 30 bins).
2. **Chart 2: Average Tip by Day (Bar Chart)**
   - Compares Thursday, Friday, Saturday, and Sunday mean gratuities.
   - Annotates exact numerical values (\$3.26, \$2.99, \$2.77, \$2.73) and sample sizes directly on the bars.
3. **Chart 3: Distribution of Tips Across Days (Box Plot)**
   - Non-parametric five-number summary (Min, Q1, Median, Q3, Max) across days.
   - Highlights extreme outliers (e.g. Saturday \$10.00 tip) and interquartile ranges.
4. **Chart 4: Relationship Between Total Bill and Tip (Scatter Plot)**
   - Plots `total_bill` vs `tip` with color coding by meal time (Lunch = Amber, Dinner = Sky Blue).
   - Dynamic ordinary least squares (OLS) regression line with correlation readout ($r = 0.676$).
   - Rich hover tooltips revealing Bill, Tip, Tip %, Day, Time, Party Size, and Smoker status.
5. **Chart 5: Correlation Heatmap**
   - Pairwise Pearson correlation matrix between `total_bill`, `tip`, and `size`.
   - Exact correlation coefficients annotated inside every matrix cell.
   - Diverging centered palette with statistical interpretations.

### C. Key Insights
1. **Modal Spending Range:** 53.7% of all bills fall between \$10.00 and \$20.00, peaking at \$13.00–\$18.00.
2. **Sunday Dominance:** Sunday achieves the highest average tip (\$3.26), +8.7% above overall mean.
3. **Saturday Volatility:** Saturday has the highest table volume (87 tables) and highest variance ($\sigma = 1.63$).
4. **Bill vs Tip Elasticity:** While dollar tip scales linearly with bill size ($r = 0.676$), tip percentage declines from ~19% on small checks to ~13% on checks over \$40.
5. **Correlation Hierarchy:** Bill amount is the direct driver of gratuity ($r = 0.676$), while party size acts as a mediator ($r = 0.598$ to bill, $r = 0.489$ to tip).

### D. Data Explorer
- Real-time client-side search across all columns.
- Dedicated dropdown filters for **Day** (Thur, Fri, Sat, Sun), **Meal Time** (Lunch, Dinner), and **Smoker Status** (Yes, No).
- Multi-column ascending and descending sorting.
- Client-side pagination (10, 25, 50, All rows per page).
- **Export to CSV:** Downloads the currently filtered subset of data as a CSV file.
- **Bi-directional Synchronization:** Changing filters here automatically updates the dashboard charts and top KPI metrics!

### E. Methodology & Scientific Principles
- Detailed background on the Bryant & Smith (1995) dataset.
- Formal rationale for each chart type.
- Mathematical formulation of Pearson correlation:
  $$r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}$$
- Comprehensive discussion on why correlation does not imply causation (controlling for table size, occasion, alcohol).
- Visualization principles: WCAG AA color contrast, non-truncated zero baselines, and colorblind-safe palettes.

### F. Conclusion & Learning Outcomes
- Professional synthesis of findings.
- Educational takeaways in exploratory data analysis, visualization design, and full-stack deployment.

---

## 4. Project Directory Structure

```
DataVisualizationWebsite/
├── app.py                   # Flask backend with REST API and static routing
├── index.html               # Main interactive dashboard single-page web app
├── generate_charts.py       # Python script generating Seaborn/Matplotlib figures
├── run.bat                  # One-click Windows launcher for Flask & browser
├── requirements.txt         # Python dependencies
├── README.md                # Comprehensive project documentation
├── css/
│   └── style.css            # Custom dark navy theme & responsive layouts
├── js/
│   ├── app.js               # Reactive application logic, Plotly charts, filters
│   └── plotly.min.js        # Offline standalone bundle of Plotly.js v2.29.1
├── data/
│   ├── tips.csv             # Authentic 244-record Seaborn tips dataset
│   └── tips.json            # JSON export of dataset
└── outputs/                 # High-resolution Seaborn & Matplotlib figures
    ├── dist_bills.png       # Chart 1: Distribution of Bills
    ├── avg_tip_day.png      # Chart 2: Average Tip by Day
    ├── box_tips_day.png     # Chart 3: Box Plot of Tips Across Days
    ├── scatter_bill_tip.png # Chart 4: Total Bill vs Tip Scatter Plot
    └── correlation_heatmap.png # Chart 5: Correlation Heatmap
```

---

## 5. Local Setup & Execution Guide (Windows & VS Code)

### Prerequisites
- **Python 3.10+** (Python 3.13 tested and verified)
- **Visual Studio Code** (recommended editor)
- Modern web browser (Chrome, Edge, Firefox, Brave)

---

### Method 1: One-Click Launcher (Easiest)
1. Open File Explorer to `DataVisualizationWebsite/`.
2. Double-click **`run.bat`**.
3. A terminal window will open, start the Flask server, and automatically launch `http://127.0.0.1:5000` in your default web browser.

---

### Method 2: Terminal / VS Code Execution (Standard)
1. Open **VS Code**.
2. Go to **File -> Open Folder** and select `DataVisualizationWebsite/` (or the project root).
3. Open a terminal (`Ctrl + ~`) and verify dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```powershell
   python app.py
   ```
5. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

---

### Method 3: Standalone Zero-Server Execution (Static Mode)
Because `app.js` embeds the authentic dataset and `js/plotly.min.js` is bundled locally:
1. Open File Explorer.
2. Double-click **`index.html`** directly.
3. The entire website, all 5 interactive charts, all statistics, and the Data Explorer will work **100% offline** without running any terminal commands!

---

### Regenerating Matplotlib & Seaborn Figures
To re-render the high-resolution static charts in `outputs/`:
```powershell
python generate_charts.py
```

---

## 6. How to Deploy Online (Free Hosting Options)

### Option A: Free Deployment via GitHub Pages (Static Hosting)
GitHub Pages provides free hosting with custom domains and SSL.
1. Create a new public repository on GitHub (e.g. `seaborn-tips-visualization`).
2. Push the contents of `DataVisualizationWebsite` to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initial commit of Project 02: Data Visualization Website"
   git branch -M main
   git remote add origin https://github.com/<your-username>/seaborn-tips-visualization.git
   git push -u origin main
   ```
3. In GitHub, go to **Settings -> Pages**.
4. Under **Branch**, select `main` and root `/`, then click **Save**.
5. Within 1 minute, your live site will be accessible worldwide at:
   `https://<your-username>.github.io/seaborn-tips-visualization/`

---

### Option B: Free Deployment on Render (Full Python Flask Backend)
Render allows you to host Python Flask apps for free.
1. Push your repository to GitHub.
2. Sign in to [Render.com](https://render.com) using your GitHub account.
3. Click **New +** -> **Web Service**.
4. Connect your GitHub repository.
5. Configure the service:
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app` (or `python app.py`)
   - **Instance Type:** `Free`
6. Click **Create Web Service**. Your live Flask API and dashboard will be deployed at `https://<app-name>.onrender.com`.

---

## 7. Submission Checklist for Internship Dashboard

When submitting your project to your internship dashboard:
1. **GitHub Repository Link:**
   `https://github.com/<your-username>/seaborn-tips-visualization`
2. **Live Demo URL:**
   `https://<your-username>.github.io/seaborn-tips-visualization/`
3. **Project Title:**
   *PROJECT 02: DATA VISUALIZATION WITH MATPLOTLIB & SEABORN*
4. **Key Highlights to Mention:**
   - Real Seaborn dataset with verified 244 records.
   - Dual-mode visualization (Plotly interactive + Matplotlib/Seaborn static).
   - Dynamic recalculation of summary statistics upon filtering.
   - Searchable, sortable table with CSV export.
   - Strict adherence to dark navy analytics UI guidelines and responsive design.

---

## 8. Author & Project Metadata
- **Project:** 02 - Data Visualization with Matplotlib & Seaborn
- **Dataset:** Bryant & Smith (1995) Restaurant Tips Dataset
- **Created:** 2026
- **Status:** Complete, Verified, and Production-Ready
