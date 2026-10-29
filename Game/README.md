# Titanic Exploratory Data Analysis (EDA)

**InternCircle Project 01 Submission**

This repository contains the complete implementation and verified deliverables for **Project 01: Exploratory Data Analysis (EDA) on Titanic**, strictly adhering to the InternCircle Project 01 guidelines.

---

## 📁 Repository Deliverables

| Deliverable | File | Description |
| :--- | :--- | :--- |
| **Master One-Click Runner** | [`run_all.py`](run_all.py) | Master pipeline script that runs the entire project end-to-end, validates all deliverables, and launches the web dashboard. |
| **Interactive Webpage** | [`index.html`](index.html) | Standalone interactive web dashboard displaying all 891 passenger records with live search, multi-filters, sorting, and EDA findings. |
| **Deliverable 1** | [`titanic_eda.ipynb`](titanic_eda.ipynb) | Complete Jupyter Notebook with 18 structured sections, documented code, and inline executed results & charts. |
| **Deliverable 2** | [`FINDINGS_SUMMARY.md`](FINDINGS_SUMMARY.md) | Standalone executive summary answering the three research questions with verified numerical evidence. |
| **Deliverable 3** | [`titanic_eda.html`](titanic_eda.html) | Submission-ready, fully self-contained HTML export of the notebook for instant viewing in any web browser. |
| **Data & Scripts**| [`titanic.csv`](titanic.csv) | Verified local cache of the official Seaborn Titanic dataset. |
| | [`run_eda.py`](run_eda.py) | Standalone console runner displaying all 18 sections and tables in the terminal. |
| | [`build_titanic_project.py`](build_titanic_project.py) | Automated reproduction script that generates, validates, executes, and exports the notebook. |
| | [`generate_webpage.py`](generate_webpage.py) | Generator script for the interactive webpage dashboard. |

---

## 🔬 Research Questions & Core Findings

### Question 1: Did women have a higher survival rate than men?
- **Numerical Result**: Female survival was **74.20%** (233 / 314) vs. Male survival of **18.89%** (109 / 577).
- **Conclusion**: **Yes.** Women were nearly 4x more likely to survive (+55.31 percentage point difference), proving rigorous adherence to the *"women and children first"* maritime convention.

### Question 2: How did passenger class relate to survival rates?
- **Numerical Result**: 
  - **1st Class**: **62.96%** (136 / 216)
  - **2nd Class**: **47.28%** (87 / 184)
  - **3rd Class**: **24.24%** (119 / 491)
- **Conclusion**: Passenger class had a direct and powerful positive relationship with survival. First-class passengers were over 2.5x more likely to survive than third-class passengers.

### Question 3: How did survival rates differ across age groups?
- **Numerical Result**:
  - **Child (`0–12` yrs)**: **57.97%** (40 / 69)
  - **Teen (`12–18` yrs)**: **42.86%** (30 / 70)
  - **Adult (`18–40` yrs)**: **36.05%** (217 / 602)
  - **Middle-aged (`40–60` yrs)**: **39.06%** (50 / 128)
  - **Senior (`60–100` yrs)**: **22.73%** (5 / 22)
- **Conclusion**: Survival rates favored the youngest passengers and penalized the oldest. Children had the highest survival rate (57.97%), while Seniors experienced the lowest (22.73%).

---

## 🛠️ Data Cleaning & Integrity Decisions

1. **Missing Age Handling**: Filled using the median age within each passenger class and gender cohort (`pclass` × `sex`). Reduced missing ages from 177 to 0 without introducing global population distortion.
2. **Missing Embarkation Handling**: Imputed 2 missing records using mode (`'S'` - Southampton, 72.4% frequency).
3. **Deck Column Dropped**: Removed safely due to 77.2% missingness (688 / 891 missing).
4. **Duplicate Row Audit**: 118 duplicate rows identified and deliberately retained. Because identifying columns (name, ticket) are omitted in the dataset, multiple distinct passengers share identical recorded attributes; removing them would falsify passenger counts and introduce attrition bias.
5. **No Machine Learning Scope Creep**: Stated focus remains strictly descriptive EDA with transparent statistical comparisons.

---

## 🚀 How to Run

### Option 1: View HTML Directly
Open [`titanic_eda.html`](titanic_eda.html) directly in any web browser (Chrome, Edge, Firefox, Safari).

### Option 2: Run in Jupyter Notebook
```bash
jupyter notebook titanic_eda.ipynb
```
Select **Kernel -> Restart & Run All**.

### Option 3: Automated Regeneration
```bash
python build_titanic_project.py
```
This script rebuilds the notebook, runs it headlessly using `nbconvert`'s `ExecutePreprocessor`, verifies all cell outputs, and exports the updated HTML deliverable.
