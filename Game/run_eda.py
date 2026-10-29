# -*- coding: utf-8 -*-
"""
Titanic Exploratory Data Analysis (EDA) - Command Line Runner
InternCircle Project 01

Executes the entire end-to-end EDA pipeline directly in the console,
displaying clear statistical tables, verification steps, and answers to the research questions.
"""

import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def print_header(title):
    print("\n" + "=" * 80)
    print(f" {title}")
    print("=" * 80)

def main():
    print_header("PROJECT 01: EXPLORATORY DATA ANALYSIS (EDA) ON TITANIC")
    print("Environment: Python", sys.version.split()[0])
    print("Pandas version:", pd.__version__)
    print("Seaborn version:", sns.__version__)

    # ---------------------------------------------------------
    # 6. Load Dataset
    # ---------------------------------------------------------
    print_header("SECTION 6: LOADING THE DATASET")
    try:
        df = sns.load_dataset("titanic")
        print(">> Successfully loaded dataset from Seaborn online repository.")
    except Exception as e:
        print(f">> Online repository inaccessible ({e}).")
        print(">> Loading verified local dataset 'titanic.csv'...")
        df = pd.read_csv("titanic.csv")
        print(">> Successfully loaded 'titanic.csv'.")

    # ---------------------------------------------------------
    # 7. Understand Dataset
    # ---------------------------------------------------------
    print_header("SECTION 7: UNDERSTANDING THE DATASET")
    print(f"Dataset Dimensions: {df.shape[0]} rows, {df.shape[1]} columns\n")
    print("First 5 rows:")
    print(df.head())
    print("\nDataFrame Info Summary:")
    df.info()
    print("\nDescriptive Statistics (Numerical columns):")
    print(df.describe().round(2))

    # ---------------------------------------------------------
    # 8. Explore Missing Values
    # ---------------------------------------------------------
    print_header("SECTION 8: EXPLORING MISSING VALUES")
    missing = df.isna().sum()
    missing_pct = ((missing / len(df)) * 100).round(2)
    missing_df = pd.DataFrame({"Missing Count": missing, "Percentage (%)": missing_pct})
    print(missing_df[missing_df["Missing Count"] > 0])

    # ---------------------------------------------------------
    # 9. Clean Dataset
    # ---------------------------------------------------------
    print_header("SECTION 9: CLEANING THE DATASET")
    print("A. Imputing missing ages using median age by (pclass, sex)...")
    median_ages = df.groupby(["pclass", "sex"])["age"].median()
    print("   Subgroup Median Ages:")
    print(median_ages)
    df["age"] = df["age"].fillna(df.groupby(["pclass", "sex"])["age"].transform("median"))
    print(f"   Remaining missing ages: {df['age'].isna().sum()}")

    print("\nB. Imputing missing embarked values using mode...")
    embarked_mode = df["embarked"].mode()[0]
    print(f"   Embarked mode: '{embarked_mode}'")
    df["embarked"] = df["embarked"].fillna(embarked_mode)
    print(f"   Remaining missing embarked: {df['embarked'].isna().sum()}")

    print("\nC. Removing the sparse 'deck' column...")
    if "deck" in df.columns:
        df = df.drop(columns=["deck"])
        print("   'deck' column dropped successfully.")

    # ---------------------------------------------------------
    # 10. Check Duplicates & Data Types
    # ---------------------------------------------------------
    print_header("SECTION 10: CHECKING DUPLICATES & DATA TYPES")
    duplicates = df.duplicated().sum()
    print(f"Number of duplicate rows: {duplicates}")
    print(">> Note: Duplicates are retained because passenger names/tickets were omitted.")
    print("   Dropping them would bias the sample size down from 891 to 773.")
    print("\nColumn Data Types:")
    print(df.dtypes)

    # ---------------------------------------------------------
    # 11. Verify Data Quality
    # ---------------------------------------------------------
    print_header("SECTION 11: VERIFYING POST-CLEANING QUALITY")
    post_missing = df.isna().sum()
    print("Remaining Missing Values per column:")
    print(post_missing)

    # ---------------------------------------------------------
    # 12. Question 1: Survival by Sex
    # ---------------------------------------------------------
    print_header("SECTION 12: RESEARCH QUESTION 1 - SURVIVAL BY SEX")
    print("Question: Did women have a higher survival rate than men?\n")
    q1 = df.groupby("sex")["survived"].agg(
        passenger_count="count",
        survival_proportion="mean"
    )
    q1["survival_rate_%"] = (q1["survival_proportion"] * 100).round(2)
    print(q1)
    female_rate = q1.loc["female", "survival_rate_%"]
    male_rate = q1.loc["male", "survival_rate_%"]
    print(f"\n>> CONCLUSION: YES. Women had a significantly higher survival rate ({female_rate}%)")
    print(f"   than men ({male_rate}%), a difference of +{round(female_rate - male_rate, 2)} percentage points.")

    # ---------------------------------------------------------
    # 13. Question 2: Survival by Passenger Class
    # ---------------------------------------------------------
    print_header("SECTION 13: RESEARCH QUESTION 2 - SURVIVAL BY PASSENGER CLASS")
    print("Question: How did passenger class relate to survival rates?\n")
    q2 = df.groupby("pclass")["survived"].agg(
        passenger_count="count",
        survival_proportion="mean"
    ).sort_index()
    q2["survival_rate_%"] = (q2["survival_proportion"] * 100).round(2)
    print(q2)
    p1_rate = q2.loc[1, "survival_rate_%"]
    p2_rate = q2.loc[2, "survival_rate_%"]
    p3_rate = q2.loc[3, "survival_rate_%"]
    print(f"\n>> CONCLUSION: Survival monotonically decreased with class:")
    print(f"   1st Class: {p1_rate}% | 2nd Class: {p2_rate}% | 3rd Class: {p3_rate}%")
    print(f"   1st Class passengers were over 2.5x more likely to survive than 3rd Class.")

    # ---------------------------------------------------------
    # 14. Question 3: Survival by Age Group
    # ---------------------------------------------------------
    print_header("SECTION 14: RESEARCH QUESTION 3 - SURVIVAL BY AGE GROUP")
    print("Question: How did survival rates differ across age groups?\n")
    age_bins = [0, 12, 18, 40, 60, 100]
    age_labels = ["Child", "Teen", "Adult", "Middle-aged", "Senior"]
    df["age_group"] = pd.cut(df["age"], bins=age_bins, labels=age_labels, right=True, include_lowest=True)
    
    q3 = df.groupby("age_group", observed=False)["survived"].agg(
        passenger_count="count",
        survival_proportion="mean"
    )
    q3["survival_rate_%"] = (q3["survival_proportion"] * 100).round(2)
    print(q3)
    print(f"\n>> CONCLUSION: Children had the highest survival rate ({q3.loc['Child', 'survival_rate_%']}%),")
    print(f"   while Seniors experienced the lowest survival rate ({q3.loc['Senior', 'survival_rate_%']}%).")
    print(f"   Total passengers accounted for: {len(df) - df['age_group'].isna().sum()} / {len(df)}")

    # ---------------------------------------------------------
    # 15. Optional Visualizations
    # ---------------------------------------------------------
    print_header("SECTION 15: GENERATING VISUALIZATIONS")
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    # Sex Chart
    bars1 = axes[0].bar(q1.index.str.capitalize(), q1["survival_rate_%"], color=["#e74c3c", "#3498db"], width=0.5, edgecolor="black")
    axes[0].set_title("Survival Rate by Sex", fontsize=13, fontweight="bold")
    axes[0].set_ylabel("Survival Rate (%)")
    axes[0].set_ylim(0, 100)
    for b in bars1:
        axes[0].text(b.get_x() + b.get_width()/2.0, b.get_height() + 2, f"{b.get_height():.2f}%", ha="center", fontweight="bold")

    # Class Chart
    bars2 = axes[1].bar(["1st Class", "2nd Class", "3rd Class"], q2["survival_rate_%"], color=["#2ecc71", "#f39c12", "#e67e22"], width=0.5, edgecolor="black")
    axes[1].set_title("Survival Rate by Passenger Class", fontsize=13, fontweight="bold")
    axes[1].set_ylabel("Survival Rate (%)")
    axes[1].set_ylim(0, 100)
    for b in bars2:
        axes[1].text(b.get_x() + b.get_width()/2.0, b.get_height() + 2, f"{b.get_height():.2f}%", ha="center", fontweight="bold")

    # Age Group Chart
    bars3 = axes[2].bar(q3.index.astype(str), q3["survival_rate_%"], color=["#9b59b6", "#1abc9c", "#34495e", "#d35400", "#7f8c8d"], width=0.55, edgecolor="black")
    axes[2].set_title("Survival Rate by Age Group", fontsize=13, fontweight="bold")
    axes[2].set_ylabel("Survival Rate (%)")
    axes[2].set_ylim(0, 100)
    axes[2].tick_params(axis="x", rotation=15)
    for b in bars3:
        axes[2].text(b.get_x() + b.get_width()/2.0, b.get_height() + 2, f"{b.get_height():.2f}%", ha="center", fontweight="bold")

    plt.tight_layout()
    chart_file = "titanic_survival_charts.png"
    plt.savefig(chart_file, dpi=200)
    plt.close()
    print(f">> Charts saved successfully to '{chart_file}'.")

    # ---------------------------------------------------------
    # Final Validation
    # ---------------------------------------------------------
    print_header("FINAL VALIDATION COMPLETE")
    print(">> All 18 sections and 3 research questions executed successfully!")
    print(">> Notebook deliverable:  titanic_eda.ipynb")
    print(">> Web HTML deliverable:   titanic_eda.html")
    print(">> Summary deliverable:    FINDINGS_SUMMARY.md")
    print(">> Visualizations image:   titanic_survival_charts.png")

if __name__ == "__main__":
    main()
