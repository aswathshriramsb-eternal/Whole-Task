"""
project1.py
Project 01: Exploratory Data Analysis (EDA) on RMS Titanic Passenger Dataset.
Full implementation imported from InternCircle Project 01 specifications (Game folder).
Features subgroup age imputation, data cleaning audit, research questions Q1-Q3 with verified metrics,
interactive Plotly visualizations, high-res Seaborn visual export, and data explorer.
"""

import os
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from modules.utils import load_titanic_data, render_project_nav


@st.cache_data
def get_cleaned_titanic_eda_data():
    """
    Implements the exact cleaning pipeline specified in InternCircle Project 01:
    1. Impute missing Age using median by (pclass, sex)
    2. Impute missing Embarked with mode ('S')
    3. Drop sparse 'deck' column
    4. Retain 118 demographic duplicate rows (names/tickets omitted)
    5. Discretize age into 5 standardized cohorts: Child, Teen, Adult, Middle-aged, Senior
    """
    df = load_titanic_data().copy()
    if df.empty:
        return df

    # Subgroup median age imputation
    df["age"] = df["age"].fillna(df.groupby(["pclass", "sex"])["age"].transform("median"))

    # Mode embarkation imputation
    if "embarked" in df.columns:
        embarked_mode = df["embarked"].mode()[0] if not df["embarked"].mode().empty else "S"
        df["embarked"] = df["embarked"].fillna(embarked_mode)

    # Drop sparse deck if present
    if "deck" in df.columns:
        df = df.drop(columns=["deck"])

    # Discretize age cohorts per Section 5 of Project Dossier
    bins = [0, 12, 18, 40, 60, 100]
    labels = ["Child (0-12)", "Teen (12-18)", "Adult (18-40)", "Middle-aged (40-60)", "Senior (60+)"]
    df["age_group"] = pd.cut(df["age"], bins=bins, labels=labels, right=True)

    # Class labels for display
    class_map = {1: "1st Class", 2: "2nd Class", 3: "3rd Class"}
    df["class_label"] = df["pclass"].map(class_map)
    df["survival_status"] = df["survived"].map({0: "Perished", 1: "Survived"})

    return df


def render_project_1():
    """Render Project 01 complete EDA dashboard."""

    df = get_cleaned_titanic_eda_data()
    if df.empty:
        st.error("Titanic dataset could not be loaded.")
        return

    st.markdown(
        """
        <div style="background: linear-gradient(135deg, #1e1b4b 0%, #152238 100%); 
                    border: 1px solid #4338ca; border-radius: 14px; padding: 28px 24px; margin-bottom: 24px;">
            <div style="display: flex; gap: 8px; margin-bottom: 8px;">
                <span class="badge-pill amber">Project 01</span>
                <span class="badge-pill">InternCircle Verified EDA</span>
                <span class="badge-pill green">Zero ML Constraint</span>
            </div>
            <h2 style="color: #ffffff; margin-bottom: 6px;">
                Exploratory Data Analysis (EDA) on RMS Titanic
            </h2>
            <p style="color: #cbd5e1; font-size: 0.95rem; margin-bottom: 0;">
                Rigorous descriptive data investigation exploring demographic survival disparities (gender, class, age cohorts) 
                without machine learning scope creep, adhering strictly to the 18 mandatory InternCircle sections.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # -------------------------------------------------------------
    # KPI Overview Cards (Exact verified numbers from Section 1)
    # -------------------------------------------------------------
    total_passengers = len(df)
    survivors = int(df["survived"].sum())
    perished = total_passengers - survivors
    overall_survival_rate = (survivors / total_passengers) * 100

    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">Total Manifest</div>
                <div class="metric-value">{total_passengers}</div>
                <div class="metric-sub">100% complete records</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with k2:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">Overall Survivors</div>
                <div class="metric-value" style="color: #38bdf8;">{survivors}</div>
                <div class="metric-sub">{overall_survival_rate:.2f}% survival rate</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with k3:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">Total Perished</div>
                <div class="metric-value" style="color: #f43f5e;">{perished}</div>
                <div class="metric-sub">{100 - overall_survival_rate:.2f}% non-survivors</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with k4:
        female_surv_rate = (df[df["sex"] == "female"]["survived"].mean()) * 100
        male_surv_rate = (df[df["sex"] == "male"]["survived"].mean()) * 100
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">Gender Disparity</div>
                <div class="metric-value" style="color: #34d399;">+55.3%</div>
                <div class="metric-sub">Female {female_surv_rate:.1f}% vs Male {male_surv_rate:.1f}%</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)

    # -------------------------------------------------------------
    # Data Cleaning Protocol Audit (Section 4 of Dossier)
    # -------------------------------------------------------------
    with st.expander("🛠️ Data Cleaning & Integrity Audit Protocol (Sections 8–11)"):
        st.markdown(
            """
            1. **Subgroup Median Age Imputation:**
               - 177 missing records (19.87%) imputed using the median age of the intersection of `pclass` and `sex`:
                 - *1st Class:* Female = 35.0 yrs, Male = 40.0 yrs
                 - *2nd Class:* Female = 28.0 yrs, Male = 30.0 yrs
                 - *3rd Class:* Female = 21.5 yrs, Male = 25.0 yrs
               - *Verification:* Missing count reduced from 177 to **0** while preserving socioeconomic age distributions.
            2. **Missing Embarkation Imputation:**
               - 2 missing values imputed with statistical mode `'S'` (Southampton, accounting for 72.4% of boardings). Missing count: **0**.
            3. **Deck Feature Exclusion:**
               - Dropped sparse `deck` feature (688 missing records, 77.22% sparsity).
            4. **Duplicate Rows Investigation (118 duplicates post-cleaning):**
               - *Audit Finding:* Duplicates arise because passenger names and ticket numbers were omitted from the dataset.
               - *Decision:* **Retained all 118 rows**. Removing them would artificially delete real historical passengers, biasing the sample from 891 down to 773.
            """
        )

    # -------------------------------------------------------------
    # 3 Mandatory Research Questions & Numerical Evidence
    # -------------------------------------------------------------
    st.markdown("### 🔬 Verified Research Questions & Empirical Evidence")

    # Tabbed Interface for the 3 Research Questions
    tab_q1, tab_q2, tab_q3 = st.tabs([
        "Q1: Gender Disparity (Women vs. Men)",
        "Q2: Socioeconomic Class Gradient",
        "Q3: Age Cohorts & Priority Groups"
    ])

    with tab_q1:
        st.markdown("#### Question 1: Did women have a higher survival rate than men?")
        q1_df = df.groupby("sex")["survived"].agg(
            Total="count",
            Survivors="sum",
            Rate="mean"
        ).reset_index()
        q1_df["Rate_Pct"] = (q1_df["Rate"] * 100).round(2)
        q1_df["Perished"] = q1_df["Total"] - q1_df["Survivors"]

        c_q1_text, c_q1_plot = st.columns([1.1, 1.4])

        with c_q1_text:
            st.markdown(
                """
                - **Female Passengers:** 314 total | 233 survivors | **74.20% survival rate**
                - **Male Passengers:** 577 total | 109 survivors | **18.89% survival rate**
                - **Statistical Gap:** **+55.31 percentage points** (~3.93x higher survival probability for women).
                - **Empirical Conclusion:** **Yes.** Quantitative disparity confirms the strict maritime enforcement 
                  of the *"women and children first"* protocol during lifeboat boarding.
                """
            )
            st.dataframe(
                q1_df[["sex", "Total", "Survivors", "Perished", "Rate_Pct"]].rename(
                    columns={"sex": "Sex", "Rate_Pct": "Survival Rate (%)"}
                ),
                use_container_width=True
            )

        with c_q1_plot:
            fig_q1 = px.bar(
                q1_df,
                x="sex",
                y="Rate_Pct",
                text=q1_df["Rate_Pct"].apply(lambda v: f"{v:.1f}%"),
                title="Survival Rate by Gender (%)",
                color="sex",
                color_discrete_map={"female": "#38bdf8", "male": "#94a3b8"},
                labels={"Rate_Pct": "Survival Rate (%)", "sex": "Gender"},
                template="plotly_dark",
            )
            fig_q1.update_traces(textposition="outside", showlegend=False)
            fig_q1.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(15,23,42,0.6)",
                yaxis=dict(range=[0, 90]),
                margin=dict(l=40, r=20, t=50, b=40),
            )
            st.plotly_chart(fig_q1, use_container_width=True)

    with tab_q2:
        st.markdown("#### Question 2: How did passenger class relate to survival rates?")
        q2_df = df.groupby(["pclass", "class_label"], observed=False)["survived"].agg(
            Total="count",
            Survivors="sum",
            Rate="mean"
        ).reset_index()
        q2_df["Rate_Pct"] = (q2_df["Rate"] * 100).round(2)
        q2_df["Perished"] = q2_df["Total"] - q2_df["Survivors"]

        c_q2_text, c_q2_plot = st.columns([1.1, 1.4])

        with c_q2_text:
            st.markdown(
                """
                - **1st Class:** 216 passengers | 136 survivors | **62.96% survival rate**
                - **2nd Class:** 184 passengers | 87 survivors | **47.28% survival rate**
                - **3rd Class:** 491 passengers | 119 survivors | **24.24% survival rate**
                - **Statistical Gap:** Monotonic gradient. 1st-class passengers were **over 2.5x more likely to survive** than 3rd-class passengers.
                - **Empirical Conclusion:** Class was heavily correlated with survival due to physical deck proximity 
                  to lifeboats and structured boarding prioritization.
                """
            )
            st.dataframe(
                q2_df[["class_label", "Total", "Survivors", "Perished", "Rate_Pct"]].rename(
                    columns={"class_label": "Ticket Class", "Rate_Pct": "Survival Rate (%)"}
                ),
                use_container_width=True
            )

        with c_q2_plot:
            fig_q2 = px.bar(
                q2_df,
                x="class_label",
                y="Rate_Pct",
                text=q2_df["Rate_Pct"].apply(lambda v: f"{v:.1f}%"),
                title="Survival Rate by Ticket Class (%)",
                color="class_label",
                color_discrete_map={"1st Class": "#38bdf8", "2nd Class": "#818cf8", "3rd Class": "#f43f5e"},
                labels={"Rate_Pct": "Survival Rate (%)", "class_label": "Ticket Class"},
                template="plotly_dark",
            )
            fig_q2.update_traces(textposition="outside", showlegend=False)
            fig_q2.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(15,23,42,0.6)",
                yaxis=dict(range=[0, 80]),
                margin=dict(l=40, r=20, t=50, b=40),
            )
            st.plotly_chart(fig_q2, use_container_width=True)

    with tab_q3:
        st.markdown("#### Question 3: How did survival rates differ across age groups?")
        q3_df = df.groupby("age_group", observed=False)["survived"].agg(
            Total="count",
            Survivors="sum",
            Rate="mean"
        ).reset_index()
        q3_df["Rate_Pct"] = (q3_df["Rate"] * 100).round(2)
        q3_df["Perished"] = q3_df["Total"] - q3_df["Survivors"]

        c_q3_text, c_q3_plot = st.columns([1.1, 1.4])

        with c_q3_text:
            st.markdown(
                """
                - **Child (0–12 yrs):** 69 passengers | 40 survivors | **57.97% survival rate**
                - **Teen (12–18 yrs):** 70 passengers | 30 survivors | **42.86% survival rate**
                - **Adult (18–40 yrs):** 602 passengers | 217 survivors | **36.05% survival rate**
                - **Middle-aged (40–60 yrs):** 128 passengers | 50 survivors | **39.06% survival rate**
                - **Senior (60–100 yrs):** 22 passengers | 5 survivors | **22.73% survival rate**
                - **Empirical Conclusion:** Children experienced the highest survival likelihood (57.97%), 
                  while seniors experienced the lowest survival rate (22.73%).
                """
            )
            st.dataframe(
                q3_df[["age_group", "Total", "Survivors", "Perished", "Rate_Pct"]].rename(
                    columns={"age_group": "Age Cohort", "Rate_Pct": "Survival Rate (%)"}
                ),
                use_container_width=True
            )

        with c_q3_plot:
            fig_q3 = px.bar(
                q3_df,
                x="age_group",
                y="Rate_Pct",
                text=q3_df["Rate_Pct"].apply(lambda v: f"{v:.1f}%"),
                title="Survival Rate by Age Cohort (%)",
                color="age_group",
                color_discrete_sequence=["#34d399", "#38bdf8", "#818cf8", "#fbbf24", "#f43f5e"],
                labels={"Rate_Pct": "Survival Rate (%)", "age_group": "Age Cohort"},
                template="plotly_dark",
            )
            fig_q3.update_traces(textposition="outside", showlegend=False)
            fig_q3.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(15,23,42,0.6)",
                yaxis=dict(range=[0, 75]),
                margin=dict(l=40, r=20, t=50, b=40),
            )
            st.plotly_chart(fig_q3, use_container_width=True)

    st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)

    # -------------------------------------------------------------
    # High-Resolution Publication Chart View (From Game Folder)
    # -------------------------------------------------------------
    st.markdown("### 📊 Publication Visual Export (Seaborn & Matplotlib)")
    chart_img_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "outputs", "titanic_survival_charts.png")
    if os.path.exists(chart_img_path):
        st.image(chart_img_path, caption="Comprehensive Seaborn EDA Visualization Export (Q1 Gender, Q2 Class, Q3 Age Cohorts)", use_container_width=True)

    # -------------------------------------------------------------
    # Searchable Cleaned Data Explorer & CSV Export
    # -------------------------------------------------------------
    st.markdown("### 🔎 Cleaned Dataset Explorer (891 Complete Records)")
    
    fe_col1, fe_col2, fe_col3 = st.columns([1.2, 1.2, 1.4])
    with fe_col1:
        f_sex = st.selectbox("Filter Sex:", ["All", "female", "male"])
    with fe_col2:
        f_class = st.selectbox("Filter Class:", ["All", "1st Class", "2nd Class", "3rd Class"])
    with fe_col3:
        f_status = st.selectbox("Filter Status:", ["All", "Survived", "Perished"])

    df_filtered = df.copy()
    if f_sex != "All":
        df_filtered = df_filtered[df_filtered["sex"] == f_sex]
    if f_class != "All":
        df_filtered = df_filtered[df_filtered["class_label"] == f_class]
    if f_status != "All":
        df_filtered = df_filtered[df_filtered["survival_status"] == f_status]

    st.dataframe(df_filtered.head(100), use_container_width=True)

    csv_data = df_filtered.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Cleaned Titanic EDA Dataset as CSV",
        data=csv_data,
        file_name="titanic_eda_cleaned.csv",
        mime="text/csv",
    )

    # Methodological Limitations
    with st.expander("📐 Methodological Limitations & Integrity Notes"):
        st.markdown(
            """
            1. **Descriptive Association vs. Causation:** Class and survival correlations reflect egress barriers and boat placement rather than ticket cost acting as an isolated biological determinant.
            2. **Tabular Anonymization:** Omission of unique ticket numbers prevents distinguishing true duplicates from distinct identical demographic profiles.
            3. **Imputation Trade-offs:** Subgroup medians maintain demographic realism while slightly compressing intra-group variance.
            """
        )

    render_project_nav(1)
