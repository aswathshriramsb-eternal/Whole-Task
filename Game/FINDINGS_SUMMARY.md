# Project 01: Titanic EDA — Short Findings Summary

**InternCircle Project 01 Deliverable**  
*Descriptive Data Analysis on the RMS Titanic Passenger Dataset*

---

## Executive Summary
This document summarizes the core empirical findings from our Exploratory Data Analysis (EDA) of the Titanic passenger dataset (891 passengers). All figures and conclusions below are derived directly from the verified execution of our Python analysis (`titanic_eda.ipynb`).

---

## Finding 1: Survival by Gender

### 1. Research Question
> **Did women have a higher survival rate than men?**

### 2. Relevant Numerical Results
| Demographic Group (`sex`) | Passenger Count | Survivors | Non-Survivors | Survival Proportion | Survival Rate (%) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Female** | 314 | 233 | 81 | 0.7420 | **74.20%** |
| **Male** | 577 | 109 | 468 | 0.1889 | **18.89%** |
| **Total / Overall** | 891 | 342 | 549 | 0.3838 | **38.38%** |

- **Absolute Percentage Point Gap**: Female survival was **+55.31 percentage points** higher than male survival.
- **Relative Survival Ratio**: Female passengers were approximately **3.93 times more likely to survive** than male passengers.

### 3. Brief Interpretation & Conclusion
**Yes, women had a significantly higher survival rate than men.** The data demonstrates that biological sex was the single most decisive demographic factor in survival. This empirical result provides quantitative evidence of the strict historical enforcement of the *"women and children first"* protocol during the loading of lifeboats, where female passengers were systematically prioritized regardless of cabin class.

---

## Finding 2: Survival by Passenger Class

### 1. Research Question
> **How did passenger class relate to survival rates?**

### 2. Relevant Numerical Results
| Passenger Class (`pclass`) | Passenger Count | Survivors | Non-Survivors | Survival Proportion | Survival Rate (%) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **1st Class** | 216 | 136 | 80 | 0.6296 | **62.96%** |
| **2nd Class** | 184 | 87 | 97 | 0.4728 | **47.28%** |
| **3rd Class** | 491 | 119 | 372 | 0.2424 | **24.24%** |
| **Total / Overall** | 891 | 342 | 549 | 0.3838 | **38.38%** |

- **Class Comparison**: 1st Class passengers had a survival rate **+15.68 percentage points** higher than 2nd Class, and **+38.72 percentage points** higher than 3rd Class.
- **Relative Survival Ratio**: 1st Class passengers were approximately **2.60 times more likely to survive** than 3rd Class passengers.

### 3. Brief Interpretation & Conclusion
**Passenger class had a direct and substantial positive relationship with survival rates.** Survival followed a strict monotonic gradient from highest to lowest socioeconomic class. First-class passengers enjoyed prime cabin locations on the upper promenade decks with immediate outdoor access to the lifeboat stations. In contrast, third-class passengers were quartered deep in the ship's lower compartments, faced longer navigation pathways, and encountered locked barriers or communication delays, resulting in nearly three out of every four third-class passengers perishing (75.76% mortality).

---

## Finding 3: Survival by Age Group

### 1. Research Question
> **How did survival rates differ across age groups?**

### 2. Relevant Numerical Results
Age groups were constructed using `pd.cut()` across all 891 passengers (missing ages imputed via `pclass` and `sex` group medians):

| Age Cohort | Age Boundary (Years) | Passenger Count | Survivors | Non-Survivors | Survival Proportion | Survival Rate (%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Child** | `(0, 12]` | 69 | 40 | 29 | 0.5797 | **57.97%** |
| **Teen** | `(12, 18]` | 70 | 30 | 40 | 0.4286 | **42.86%** |
| **Adult** | `(18, 40]` | 602 | 217 | 385 | 0.3605 | **36.05%** |
| **Middle-aged** | `(40, 60]` | 128 | 50 | 78 | 0.3906 | **39.06%** |
| **Senior** | `(60, 100]` | 22 | 5 | 17 | 0.2273 | **22.73%** |
| **Total** | `(0, 100]` | **891** | **342** | **549** | **0.3838** | **38.38%** |

- **Highest vs. Lowest Group**: Children experienced the highest survival rate (**57.97%**), while Seniors experienced the lowest survival rate (**22.73%**), representing a difference of **35.24 percentage points**.

### 3. Brief Interpretation & Conclusion
**Survival rates varied considerably across age cohorts, favoring the youngest travelers and severely penalizing the elderly.** Young children were prioritized alongside women during the initial lifeboat loadings, resulting in the highest survival rate across any age cohort. In contrast, adults represented the bulk of the casualties, heavily weighted down by the loss of adult male passengers. Seniors faced the lowest survival rate (22.73%), consistent with physical mobility challenges during the midnight evacuation under sub-zero temperatures.

---

## Methodological Integrity & Verification Checklist
- [x] **Primary Dataset Loading**: Tested with `sns.load_dataset("titanic")` and verified offline fallback `pd.read_csv("titanic.csv")`.
- [x] **Age Imputation**: Missing values filled using subgroup medians by `pclass` and `sex` (0 missing remaining).
- [x] **Embarked Imputation**: Missing values filled using mode `'S'` (0 missing remaining).
- [x] **Deck Feature**: Dropped due to 77.2% missingness.
- [x] **Duplicate Row Audit**: 118 duplicate rows identified, analyzed, and intentionally retained because unique ticket identifiers are omitted in the anonymized data.
- [x] **Reproducibility**: All cells re-executed cleanly from top to bottom; HTML export rendered without errors.
