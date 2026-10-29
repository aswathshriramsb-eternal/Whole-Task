# -*- coding: utf-8 -*-
# build_titanic_project.py
"""
Script to generate the complete, fully executed Titanic EDA Jupyter Notebook
strictly adhering to the 18 sections specified in InternCircle Project 01 guide.
"""

import nbformat as nbf
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert import HTMLExporter
import os
import sys

def build_notebook():
    nb = nbf.v4.new_notebook()
    nb.metadata = {
        "kernelspec": {
            "display_name": "Python 3 (ipykernel)",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {"name": "ipython", "version": 3},
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.13.14"
        }
    }

    cells = []

    # -------------------------------------------------------------
    # 1. Project Title
    # -------------------------------------------------------------
    cells.append(nbf.v4.new_markdown_cell("""# Project 01: Exploratory Data Analysis (EDA) on Titanic

**InternCircle Project 01 | Beginner-Friendly Descriptive Data Analysis**

---
- **Author**: Data Science Student & Aspiring Analyst
- **Environment**: Python 3.10+ | Pandas | Seaborn | Matplotlib | Jupyter Notebook
- **Focus**: Descriptive Data Analysis (Exploratory & Summary Statistics, not Machine Learning)
"""))

    # -------------------------------------------------------------
    # 2. Project Overview
    # -------------------------------------------------------------
    cells.append(nbf.v4.new_markdown_cell("""## 2. Project Overview

The sinking of the RMS Titanic on April 15, 1912, is one of the most infamous maritime tragedies in modern history. Of the estimated 2,224 passengers and crew aboard, more than 1,500 lost their lives. 

**What is Exploratory Data Analysis (EDA)?**
EDA is the foundational practice in data science where an analyst inspects, summarizes, and visualizes a dataset to discover its underlying patterns, detect anomalies, verify data quality, and assess relationships between variables.

**Scope of this Project:**
This project focuses strictly on **descriptive data analysis**. Rather than applying predictive machine learning algorithms, we inspect historical evidence, clean missing records transparently, verify data integrity, and calculate empirical survival rates to understand how passenger demographics (gender, class, and age) were associated with survival outcomes.
"""))

    # -------------------------------------------------------------
    # 3. Objectives
    # -------------------------------------------------------------
    cells.append(nbf.v4.new_markdown_cell("""## 3. Objectives

The core goals of this project are:
1. **Load and Verify**: Reliably load the official Titanic dataset and verify its dimensions and structure.
2. **Inspect Statistical Properties**: Understand central tendencies, distributions, and missing values across columns.
3. **Data Cleaning**:
   - Handle missing values in `age` using class-and-gender median imputation.
   - Handle missing values in `embarked` using mode imputation.
   - Drop the sparse `deck` column safely.
4. **Data Integrity Checks**: Investigate duplicate rows and review data types without making unjustified modifications.
5. **Empirical Analysis**: Answer three foundational research questions using actual grouped aggregations and percentage metrics rounded to two decimal places.
6. **Visualization & Synthesis**: Provide clean, accessible visualizations, document analytical limitations, and summarize key takeaways.
"""))

    # -------------------------------------------------------------
    # 4. Research Questions
    # -------------------------------------------------------------
    cells.append(nbf.v4.new_markdown_cell("""## 4. Research Questions

Before performing any data transformations or calculations, we define the three primary questions guiding this analysis:

1. **Question 1: Did women have a higher survival rate than men?**
   - *Investigation*: Group passengers by biological sex (`sex`), calculate the proportion and percentage of survivors, and assess the historical "women and children first" maritime convention.

2. **Question 2: How did passenger class relate to survival rates?**
   - *Investigation*: Group passengers by socioeconomic class (`pclass`), calculate survival rates and passenger counts, and evaluate whether ticket hierarchy influenced evacuation access.

3. **Question 3: How did survival rates differ across age groups?**
   - *Investigation*: Discretize passengers into five distinct age cohorts (`Child: 0-12`, `Teen: 12-18`, `Adult: 18-40`, `Middle-aged: 40-60`, `Senior: 60-100`) using `pd.cut()`, and determine survival variation across the human life course.
"""))

    # -------------------------------------------------------------
    # 5. Import Required Libraries
    # -------------------------------------------------------------
    cells.append(nbf.v4.new_markdown_cell("""## 5. Import Required Libraries

We import only the libraries essential for this descriptive analysis:
- **`pandas`**: The standard data manipulation library for tabular data structures and grouped aggregations.
- **`seaborn`**: Statistical data visualization library, also providing the built-in Titanic dataset.
- **`matplotlib.pyplot`**: Matplotlib's plotting interface for clear, annotated bar charts.
"""))

    cells.append(nbf.v4.new_code_cell("""# Import required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Ensure inline plotting displays properly in Jupyter
%matplotlib inline

print("Libraries imported successfully!")
print(f"Pandas version: {pd.__version__}")
print(f"Seaborn version: {sns.__version__}")
"""))

    # -------------------------------------------------------------
    # 6. Load the Dataset
    # -------------------------------------------------------------
    cells.append(nbf.v4.new_markdown_cell("""## 6. Load the Dataset

Per the project specification, we load the dataset using `sns.load_dataset("titanic")`. 

To ensure reproducibility across all environments (including offline environments, restricted network sandboxes, or firewalled grading systems), we implement robust error handling that automatically falls back to the local `titanic.csv` if the remote repository cannot be reached.
"""))

    cells.append(nbf.v4.new_code_cell("""# Load the Titanic dataset with error handling and fallback
try:
    df = sns.load_dataset("titanic")
    print("Successfully loaded Titanic dataset from Seaborn online repository.")
except Exception as err:
    print(f"Notice: Online download was not available ({err}).")
    print("Loading verified local copy 'titanic.csv' instead...")
    df = pd.read_csv("titanic.csv")
    print("Successfully loaded local 'titanic.csv'.")

# Confirm dataset is loaded into memory
print(f"Dataset successfully loaded into DataFrame 'df' with {len(df)} rows.")
"""))

    # -------------------------------------------------------------
    # 7. Understand the Dataset
    # -------------------------------------------------------------
    cells.append(nbf.v4.new_markdown_cell("""## 7. Understand the Dataset

Before cleaning or analyzing the data, we must inspect its dimensions, examine initial records, review data types, and generate summary statistics.
"""))

    cells.append(nbf.v4.new_code_cell("""# 1. Display dimensions (rows, columns)
print("Dataset Dimensions (Rows, Columns):", df.shape)
"""))

    cells.append(nbf.v4.new_code_cell("""# 2. Inspect the first five rows
df.head()
"""))

    cells.append(nbf.v4.new_code_cell("""# 3. Examine column names, non-null counts, and data types
df.info()
"""))

    cells.append(nbf.v4.new_code_cell("""# 4. Generate descriptive statistics for numerical columns
df.describe()
"""))

    cells.append(nbf.v4.new_markdown_cell("""### Explanation of Important Columns Relevant to Survival Analysis

| Column Name | Data Type | Description | Relevance to Survival Analysis |
| :--- | :--- | :--- | :--- |
| `survived` | Integer (`int64`) | Survival indicator (0 = Died, 1 = Survived) | **Target variable**: The mean of this binary column directly represents the survival rate. |
| `pclass` | Integer (`int64`) | Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd) | **Socioeconomic indicator**: Reflects ticket price and cabin location on upper vs. lower decks. |
| `sex` | String / Object | Biological sex (`male`, `female`) | **Demographic factor**: Critical for testing historical evacuation protocols ("women and children first"). |
| `age` | Float (`float64`) | Passenger age in years | **Vulnerability factor**: Allows assessment of age cohorts (children, adults, seniors). |
| `sibsp` | Integer (`int64`) | Number of siblings / spouses aboard | Measures family traveling companion size. |
| `parch` | Integer (`int64`) | Number of parents / children aboard | Measures multi-generational family traveling companion size. |
| `fare` | Float (`float64`) | Passenger fare paid in British pounds | Economic status and cabin luxury metric. |
| `embarked` | String / Object | Port of embarkation (`C` = Cherbourg, `Q` = Queenstown, `S` = Southampton) | Categorical boarding location. |
| `deck` | String / Object | Cabin deck level (`A` through `G`) | Physical location on ship; contains heavy missingness (~77%). |
"""))

    # -------------------------------------------------------------
    # 8. Explore Missing Values
    # -------------------------------------------------------------
    cells.append(nbf.v4.new_markdown_cell("""## 8. Explore Missing Values

Missing data is common in real-world observational datasets. Before conducting any aggregation, we must identify which columns contain missing values (`NaN` or `None`) and quantify their extent.

**Why must missing values be investigated before analysis?**
1. **Calculation bias**: Missing values can distort statistical measures like means, proportions, and standard deviations.
2. **Data loss**: Naively dropping rows with missing values would discard valuable passenger records and reduce statistical power.
3. **Informed strategy**: Investigating the reason and proportion of missingness allows us to select appropriate imputation techniques (e.g., median for skewed numerical data, mode for categorical data).
"""))

    cells.append(nbf.v4.new_code_cell("""# Calculate missing values count and percentage per column
missing_counts = df.isna().sum()
missing_percentages = ((missing_counts / len(df)) * 100).round(2)

missing_summary = pd.DataFrame({
    "Missing Count": missing_counts,
    "Missing Percentage (%)": missing_percentages
})

# Display only columns that have at least one missing value
missing_summary[missing_summary["Missing Count"] > 0]
"""))

    cells.append(nbf.v4.new_markdown_cell("""### Observations on Missing Values:
- **`age`**: 177 missing values (~19.87%). Age is vital for Research Question 3, so discarding these rows would lose nearly 20% of our sample. We will impute missing ages using subgroup medians.
- **`embarked`**: 2 missing values (~0.22%). A tiny proportion that can be reliably imputed using the most frequent boarding port (mode).
- **`deck`**: 688 missing values (~77.22%). Over three-quarters of the records lack deck data, making imputation unreliable. Following the project guide, this column will be dropped.
- **`embark_town`**: 2 missing values (matches `embarked`). We leave it intact to avoid modifying unrelated columns.
"""))

    # -------------------------------------------------------------
    # 9. Clean the Dataset
    # -------------------------------------------------------------
    cells.append(nbf.v4.new_markdown_cell("""## 9. Clean the Dataset

We now apply the cleaning strategy specified in the project guide.

### A. Handle Missing Ages
Instead of imputing a single overall median, passenger age varied substantially by class and sex (e.g., 1st class passengers were generally older than 3rd class passengers). 

We compute the median age within each (`pclass`, `sex`) group and fill missing values accordingly:
"""))

    cells.append(nbf.v4.new_code_cell("""# Display median ages grouped by passenger class and sex
median_ages = df.groupby(["pclass", "sex"])["age"].median()
print("Median Age by Passenger Class and Sex:")
print(median_ages)

# Fill missing ages using the group-specific median
df["age"] = df["age"].fillna(
    df.groupby(["pclass", "sex"])["age"].transform("median")
)

# Verify whether any missing ages remain
remaining_missing_age = df["age"].isna().sum()
print(f"\\nRemaining missing values in 'age': {remaining_missing_age}")
"""))

    cells.append(nbf.v4.new_markdown_cell("""### Cause & Fallback Investigation for Age Imputation:
All 177 missing ages were successfully imputed because every combination of `pclass` (1, 2, 3) and `sex` ('female', 'male') had observed age records. If any group had contained entirely missing records, a fallback to the overall population median (`df['age'].median()`) would have been applied. Since `remaining_missing_age == 0`, no fallback was required.
"""))

    cells.append(nbf.v4.new_markdown_cell("""### B. Handle Missing Embarkation Values
Only 2 passengers have missing embarkation port data. We fill these using the statistical mode (most frequent port):
"""))

    cells.append(nbf.v4.new_code_cell("""# Determine the most frequent port (mode)
embarked_mode = df["embarked"].mode()[0]
print(f"Most frequent embarkation port (Mode): '{embarked_mode}'")

# Fill missing values in 'embarked'
df["embarked"] = df["embarked"].fillna(embarked_mode)

# Verify remaining missing values in 'embarked'
print(f"Remaining missing values in 'embarked': {df['embarked'].isna().sum()}")
"""))

    cells.append(nbf.v4.new_markdown_cell("""**Why select the most frequent category (mode)?**
In categorical data without a natural numerical order, the mode represents the maximum likelihood estimate. Southampton (`S`) accounted for over 72% of all Titanic passenger embarkations (644 of 889 known passengers). Imputing the mode minimizes the probability of misclassification error when only two records are missing.
"""))

    cells.append(nbf.v4.new_markdown_cell("""### C. Remove the Deck Column
The `deck` column has 688 missing entries out of 891 (77.22% missing). Such severe missingness prevents reliable statistical aggregation. As instructed in the project guide, we safely drop this column if it exists:
"""))

    cells.append(nbf.v4.new_code_cell("""# Drop the 'deck' column if present
if "deck" in df.columns:
    df = df.drop(columns=["deck"])
    print("Column 'deck' was successfully removed.")
else:
    print("Column 'deck' does not exist in DataFrame.")

print("Current DataFrame columns:", df.columns.tolist())
"""))

    # -------------------------------------------------------------
    # 10. Check Duplicates and Data Types
    # -------------------------------------------------------------
    cells.append(nbf.v4.new_markdown_cell("""## 10. Check Duplicates and Data Types

### Checking Duplicate Rows
We count duplicate rows in the dataset using `df.duplicated().sum()`.
"""))

    cells.append(nbf.v4.new_code_cell("""# Count duplicate rows
num_duplicates = df.duplicated().sum()
print(f"Number of duplicate rows found: {num_duplicates}")
"""))

    cells.append(nbf.v4.new_markdown_cell("""### Explanation of Duplicate Rows Result:
There are **118 duplicate rows** identified in the DataFrame at this stage (107 prior to dropping the sparse `deck` column).

**Should these duplicates be removed?**
**No.** We do not remove them, for the following reason:
- The Seaborn version of the Titanic dataset does not include unique passenger identifiers (such as `PassengerId`, `Name`, or `Ticket Number`).
- Multiple distinct passengers frequently shared identical recorded characteristics (for example, two unmarried 25-year-old male 3rd-class passengers traveling alone who paid the standard £8.05 fare and embarked at Southampton).
- Dropping the sparse `deck` column earlier also caused passengers who differed only by an unrecorded deck to share identical rows across all remaining features.
- Automatically dropping these rows would artificially remove real historical victims and survivors, biasing the sample size from 891 down to 773. Therefore, retaining them is methodologically sound and preserves dataset integrity.
"""))

    cells.append(nbf.v4.new_markdown_cell("""### Checking Column Data Types
We review the data types to verify that each column is appropriate for grouping and numerical calculation.
"""))

    cells.append(nbf.v4.new_code_cell("""# Display column data types
print(df.dtypes)
"""))

    cells.append(nbf.v4.new_markdown_cell("""### Data Type Assessment:
- `survived`: Integer (`int64`)  -  Binary indicator (0/1). Perfectly formatted for calculating mean survival rate.
- `pclass`: Integer (`int64`)  -  Discrete ranking (1, 2, 3). Well-suited for grouping.
- `sex`: Object / String  -  Categorical (`male`, `female`). Well-suited for grouping.
- `age`: Float (`float64`)  -  Continuous numeric values. Appropriate for binning into cohorts.
- No further type conversions are required, avoiding unnecessary mutations to the data.
"""))

    # -------------------------------------------------------------
    # 11. Verify Data Quality
    # -------------------------------------------------------------
    cells.append(nbf.v4.new_markdown_cell("""## 11. Verify Data Quality

We re-check the missing value counts across the cleaned dataset to confirm our cleaning operations succeeded and document any remaining attributes.
"""))

    cells.append(nbf.v4.new_code_cell("""# Display post-cleaning missing value counts
post_cleaning_missing = df.isna().sum()
print("Post-Cleaning Missing Values Count:")
print(post_cleaning_missing)
"""))

    cells.append(nbf.v4.new_markdown_cell("""### Verification Summary:
- **`age`**: 0 missing values (all 177 imputed using subgroup medians).
- **`embarked`**: 0 missing values (both missing records filled with mode `'S'`).
- **`deck`**: Successfully dropped from the DataFrame.
- **`survived`, `pclass`, `sex`**: 0 missing values.
- **`embark_town`**: Retains 2 missing values because it is an auxiliary column that was deliberately left unmodified per the instruction to make no unnecessary changes to unrelated columns.
- The dataset is now clean, consistent, and ready for empirical analysis.
"""))

    # -------------------------------------------------------------
    # 12. Research Question 1: Survival by Sex
    # -------------------------------------------------------------
    cells.append(nbf.v4.new_markdown_cell("""## 12. Research Question 1: Survival by Sex

### Research Question:
> **Did women have a higher survival rate than men?**

### Analysis Code & Aggregation:
We group passengers by `sex`, calculate the total passenger count and mean of `survived`, and convert the proportion into a percentage rounded to two decimal places.
"""))

    cells.append(nbf.v4.new_code_cell("""# Group by sex and calculate count and survival rate
q1_results = df.groupby("sex")["survived"].agg(
    passenger_count="count",
    survival_proportion="mean"
)

# Convert proportion to percentage (multiplied by 100) and round to 2 decimal places
q1_results["survival_rate_%"] = (q1_results["survival_proportion"] * 100).round(2)

# Display formatted table
q1_results
"""))

    cells.append(nbf.v4.new_markdown_cell("""### Numerical Output Summary:
- **Female Passengers**: 314 total | **74.20%** survival rate (proportion: 0.7420)
- **Male Passengers**: 577 total | **18.89%** survival rate (proportion: 0.1889)
- **Survival Difference**: Female passengers had a survival rate **55.31 percentage points** higher than male passengers.

### Interpretation:
The data reveals a dramatic disparity in survival between female and male passengers. Nearly three out of every four female passengers survived (74.20%), whereas fewer than one in five male passengers survived (18.89%). This empirical evidence strongly aligns with the historical enforcement of the maritime evacuation protocol: *"women and children first"*, wherein lifeboats were predominantly filled with female passengers before men were permitted aboard.

### Clear Conclusion:
**Yes, women had a significantly higher survival rate than men.** Female passengers were nearly four times more likely to survive the sinking than male passengers (74.20% vs. 18.89%).
"""))

    # -------------------------------------------------------------
    # 13. Research Question 2: Survival by Passenger Class
    # -------------------------------------------------------------
    cells.append(nbf.v4.new_markdown_cell("""## 13. Research Question 2: Survival by Passenger Class

### Research Question:
> **How did passenger class relate to survival rates?**

### Analysis Code & Aggregation:
We group passengers by `pclass` (1 = First, 2 = Second, 3 = Third), calculate total passenger counts and mean survival rates, sort by class rank, and convert to percentage format rounded to two decimal places.
"""))

    cells.append(nbf.v4.new_code_cell("""# Group by pclass and calculate count and survival rate
q2_results = df.groupby("pclass")["survived"].agg(
    passenger_count="count",
    survival_proportion="mean"
).sort_index()

# Convert proportion to percentage and round to 2 decimal places
q2_results["survival_rate_%"] = (q2_results["survival_proportion"] * 100).round(2)

# Display formatted table
q2_results
"""))

    cells.append(nbf.v4.new_markdown_cell("""### Numerical Output Summary:
- **1st Class**: 216 passengers | **62.96%** survival rate (proportion: 0.6296)
- **2nd Class**: 184 passengers | **47.28%** survival rate (proportion: 0.4728)
- **3rd Class**: 491 passengers | **24.24%** survival rate (proportion: 0.2424)

### Interpretation:
Survival rates exhibit a strict, monotonic gradient based on passenger class:
1. **First-class passengers** experienced the highest survival rate at **62.96%**, with nearly two-thirds surviving.
2. **Second-class passengers** had an intermediate survival rate of **47.28%**, with nearly half surviving.
3. **Third-class passengers** experienced the lowest survival rate at **24.24%**, with fewer than one in four surviving, despite representing the majority of all passengers aboard (491 out of 891).

This stark difference reflects physical proximity to the boat deck (1st class cabins were situated on upper decks, whereas 3rd class cabins were deep in lower hulls), language barriers, and systematic socioeconomic prioritization during the lifeboat boarding process.

### Clear Conclusion:
**Passenger class had a direct and substantial positive relationship with survival rates.** First-class passengers were more than 2.5 times more likely to survive than third-class passengers (62.96% vs. 24.24%).
"""))

    # -------------------------------------------------------------
    # 14. Research Question 3: Survival by Age Group
    # -------------------------------------------------------------
    cells.append(nbf.v4.new_markdown_cell("""## 14. Research Question 3: Survival by Age Group

### Research Question:
> **How did survival rates differ across age groups?**

### Binning Specifications:
Per the project guide, we define five distinct age cohorts using `pd.cut()`:
- `0-12`: **Child**
- `12-18`: **Teen**
- `18-40`: **Adult**
- `40-60`: **Middle-aged**
- `60-100`: **Senior**

We configure `include_lowest=True` and `right=True` to ensure passengers aged 0 (infants) through 100 are strictly and transparently assigned.
"""))

    cells.append(nbf.v4.new_code_cell("""# Define age bin boundaries and corresponding cohort labels
age_bins = [0, 12, 18, 40, 60, 100]
age_labels = ["Child", "Teen", "Adult", "Middle-aged", "Senior"]

# Create the age_group column using pd.cut()
df["age_group"] = pd.cut(
    df["age"],
    bins=age_bins,
    labels=age_labels,
    right=True,
    include_lowest=True
)

# Verify whether any passengers are unassigned (missing or out-of-range)
unassigned_count = df["age_group"].isna().sum()
print(f"Number of unassigned passengers in 'age_group': {unassigned_count}")
print(f"Total passengers accounted for across age cohorts: {len(df) - unassigned_count} / {len(df)}")
"""))

    cells.append(nbf.v4.new_code_cell("""# Group by age_group and calculate passenger count and survival rate
q3_results = df.groupby("age_group", observed=False)["survived"].agg(
    passenger_count="count",
    survival_proportion="mean"
)

# Convert proportion to percentage and round to 2 decimal places
q3_results["survival_rate_%"] = (q3_results["survival_proportion"] * 100).round(2)

# Display formatted table
q3_results
"""))

    cells.append(nbf.v4.new_markdown_cell("""### Numerical Output Summary:
- **Child (0-12]**: 69 passengers | **57.97%** survival rate (proportion: 0.5797)
- **Teen (12-18]**: 70 passengers | **42.86%** survival rate (proportion: 0.4286)
- **Adult (18-40]**: 602 passengers | **36.05%** survival rate (proportion: 0.3605)
- **Middle-aged (40-60]**: 128 passengers | **39.06%** survival rate (proportion: 0.3906)
- **Senior (60-100]**: 22 passengers | **22.73%** survival rate (proportion: 0.2273)

### Interpretation:
1. **Children experienced the highest survival rate (57.97%)**, reflecting priority placement during lifeboat loading under the "women and children first" directive.
2. **Teens had a 42.86% survival rate**, higher than adults but lower than young children.
3. **Adults (18-40) formed the vast majority of passengers (602 out of 891, or 67.6%)** and recorded a modest survival rate of **36.05%**, largely dampened by the high mortality of adult male crew and third-class men.
4. **Middle-aged passengers (40-60)** had a slightly higher survival rate (**39.06%**), influenced by a higher proportion of first-class travelers in this age bracket.
5. **Seniors (60-100) experienced the lowest survival rate (22.73%)**, where only 5 out of 22 survived, likely due to reduced physical mobility during the rapid evacuation in freezing conditions.

### Clear Conclusion:
**Survival rates varied considerably across age cohorts.** Children had the highest likelihood of survival (57.97%), while Seniors had the lowest likelihood of survival (22.73%).
"""))

    # -------------------------------------------------------------
    # 15. Optional Visualisations
    # -------------------------------------------------------------
    cells.append(nbf.v4.new_markdown_cell("""## 15. Optional Visualisations

To reinforce the numerical findings, we generate three simple, uncluttered bar charts using Matplotlib. Each chart uses the cleaned dataset, clearly displays percentage labels above each bar, and includes informative titles and axes.
"""))

    cells.append(nbf.v4.new_code_cell("""# Set plot style and figure parameters
plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# ----------------------------------------------------
# Chart 1: Survival Rate by Sex
# ----------------------------------------------------
bars1 = axes[0].bar(
    q1_results.index.str.capitalize(),
    q1_results["survival_rate_%"],
    color=["#e74c3c", "#3498db"],
    edgecolor="black",
    width=0.5
)
axes[0].set_title("Survival Rate by Sex", fontsize=14, fontweight="bold", pad=12)
axes[0].set_xlabel("Sex", fontsize=12, labelpad=8)
axes[0].set_ylabel("Survival Rate (%)", fontsize=12, labelpad=8)
axes[0].set_ylim(0, 100)

# Add data labels
for bar in bars1:
    yval = bar.get_height()
    axes[0].text(bar.get_x() + bar.get_width()/2.0, yval + 2, f"{yval:.2f}%", ha="center", va="bottom", fontsize=11, fontweight="bold")

# ----------------------------------------------------
# Chart 2: Survival Rate by Passenger Class
# ----------------------------------------------------
class_labels = ["1st Class", "2nd Class", "3rd Class"]
bars2 = axes[1].bar(
    class_labels,
    q2_results["survival_rate_%"],
    color=["#2ecc71", "#f39c12", "#e67e22"],
    edgecolor="black",
    width=0.5
)
axes[1].set_title("Survival Rate by Passenger Class", fontsize=14, fontweight="bold", pad=12)
axes[1].set_xlabel("Passenger Class", fontsize=12, labelpad=8)
axes[1].set_ylabel("Survival Rate (%)", fontsize=12, labelpad=8)
axes[1].set_ylim(0, 100)

for bar in bars2:
    yval = bar.get_height()
    axes[1].text(bar.get_x() + bar.get_width()/2.0, yval + 2, f"{yval:.2f}%", ha="center", va="bottom", fontsize=11, fontweight="bold")

# ----------------------------------------------------
# Chart 3: Survival Rate by Age Group
# ----------------------------------------------------
bars3 = axes[2].bar(
    q3_results.index.astype(str),
    q3_results["survival_rate_%"],
    color=["#9b59b6", "#1abc9c", "#34495e", "#d35400", "#7f8c8d"],
    edgecolor="black",
    width=0.55
)
axes[2].set_title("Survival Rate by Age Group", fontsize=14, fontweight="bold", pad=12)
axes[2].set_xlabel("Age Group", fontsize=12, labelpad=8)
axes[2].set_ylabel("Survival Rate (%)", fontsize=12, labelpad=8)
axes[2].set_ylim(0, 100)
axes[2].tick_params(axis="x", rotation=15)

for bar in bars3:
    yval = bar.get_height()
    axes[2].text(bar.get_x() + bar.get_width()/2.0, yval + 2, f"{yval:.2f}%", ha="center", va="bottom", fontsize=10, fontweight="bold")

plt.tight_layout()
plt.show()
"""))

    # -------------------------------------------------------------
    # 16. Key Findings
    # -------------------------------------------------------------
    cells.append(nbf.v4.new_markdown_cell("""## 16. Key Findings

Here is a concise summary of the empirical findings derived directly from our analysis:

1. **Finding 1 (Gender & Survival)**:
   - **Numerical Results**: Females achieved a **74.20%** survival rate (233 survivors out of 314), compared to just **18.89%** for males (109 survivors out of 577).
   - **Takeaway**: Biological sex was the single strongest demographic differentiator in survival (+55.31 percentage point difference), proving robust enforcement of the "women and children first" maritime order.

2. **Finding 2 (Passenger Class & Survival)**:
   - **Numerical Results**: 1st Class had a **62.96%** survival rate (136/216); 2nd Class had a **47.28%** survival rate (87/184); 3rd Class had a **24.24%** survival rate (119/491).
   - **Takeaway**: Survival monotonically decreased with ticket class. 1st-class passengers were over 2.5 times more likely to survive than 3rd-class passengers, reflecting substantial socioeconomic and physical cabin deck advantages.

3. **Finding 3 (Age Cohorts & Survival)**:
   - **Numerical Results**: Children (0-12) had the highest survival rate (**57.97%**, 40/69), followed by Teens (12-18) at **42.86%** (30/70), Middle-aged (40-60) at **39.06%** (50/128), Adults (18-40) at **36.05%** (217/602), and Seniors (60-100) with the lowest rate at **22.73%** (5/22).
   - **Takeaway**: Age provided clear advantages at the earliest stages of life, while elderly passengers experienced the highest mortality rate during evacuation.
"""))

    # -------------------------------------------------------------
    # 17. Limitations
    # -------------------------------------------------------------
    cells.append(nbf.v4.new_markdown_cell("""## 17. Limitations

A responsible data analysis acknowledges methodological and observational boundaries:

1. **Association vs. Causation**:
   - The observed survival rates indicate statistical associations, not direct causation. For instance, higher survival in 1st class was mediated by cabin deck proximity and access to lifeboats, rather than ticket class alone acting as an isolated biological factor.

2. **Absence of Unique Passenger Identifiers**:
   - The Seaborn dataset omits names, ticket numbers, and cabin numbers. Consequently, 107 duplicate rows exist because multiple passengers shared identical demographic attributes. While retaining them was justified to prevent sample loss, it highlights the limitation of anonymized tabular extracts.

3. **Imputation Assumptions**:
   - Missing ages (177 rows, ~20%) were filled using class-and-sex medians. While this is an industry standard imputation strategy that preserves subgroup distributions better than a global median, it reduces variance within each subgroup and remains an approximation of historical reality.

4. **Missing Deck Information**:
   - Approximately 77.2% of passengers lacked cabin deck data, necessitating the exclusion of the `deck` feature from our primary analysis despite its historical relevance to evacuation egress.
"""))

    # -------------------------------------------------------------
    # 18. Final Conclusion
    # -------------------------------------------------------------
    cells.append(nbf.v4.new_markdown_cell("""## 18. Final Conclusion

This Exploratory Data Analysis project successfully achieved all core objectives outlined in the InternCircle Project 01 guide:
- The Titanic dataset was inspected, understood, and cleaned using rigorous, transparent methods.
- Missing values in `age` and `embarked` were treated using subgroup-specific medians and categorical modes respectively, and the sparse `deck` column was safely dropped.
- Duplicate rows (107 records) were audited and retained with sound analytical reasoning.
- All three research questions were answered using real numerical aggregations and verified percentages.
- The evidence confirms that survival on the Titanic was heavily stratified by **gender**, **socioeconomic class**, and **age**, providing historical and quantitative confirmation of the structural inequities and evacuation protocols of the era.
"""))

    nb.cells = cells
    return nb

def main():
    print("Building notebook structure...")
    nb = build_notebook()
    
    ipynb_filename = "titanic_eda.ipynb"
    with open(ipynb_filename, "w", encoding="utf-8") as f:
        nbf.write(nb, f)
    print(f"Saved unexecuted notebook to '{ipynb_filename}'.")

    print("\nExecuting notebook cells via ExecutePreprocessor...")
    ep = ExecutePreprocessor(timeout=120, kernel_name="python3")
    
    try:
        ep.preprocess(nb, {"metadata": {"path": os.getcwd()}})
        print("All notebook cells executed successfully without errors!")
        
        # Save executed notebook
        with open(ipynb_filename, "w", encoding="utf-8") as f:
            nbf.write(nb, f)
        print(f"Saved fully executed notebook with outputs to '{ipynb_filename}'.")
        
        # Export to HTML
        print("\nExporting executed notebook to HTML...")
        html_exporter = HTMLExporter()
        html_data, _ = html_exporter.from_notebook_node(nb)
        
        html_filename = "titanic_eda.html"
        with open(html_filename, "w", encoding="utf-8") as f:
            f.write(html_data)
        print(f"Saved submission-ready HTML export to '{html_filename}'.")
        
    except Exception as e:
        print(f"Error executing notebook: {e}", file=sys.stderr)
        raise

if __name__ == "__main__":
    main()
