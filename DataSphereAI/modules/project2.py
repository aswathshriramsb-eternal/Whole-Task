"""
project2.py
Project 02: Data Visualization with Matplotlib & Seaborn.
Interactive exploratory data visualization dashboard built on the authentic Seaborn Tips dataset.
Features dynamic cross-filtering, 5 Plotly charts, key insights, and data export.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from modules.utils import load_tips_data, render_project_nav


def render_project_2():
    """Render Project 02 interactive visualization dashboard."""

    df_raw = load_tips_data()
    if df_raw.empty:
        st.error("Seaborn tips dataset could not be loaded.")
        return

    # Add derived column if not present
    if "tip_pct" not in df_raw.columns:
        df_raw["tip_pct"] = (df_raw["tip"] / df_raw["total_bill"] * 100).round(2)

    st.markdown(
        """
        <div style="background: linear-gradient(135deg, #0d1a33 0%, #152238 100%); 
                    border: 1px solid #1e3a5f; border-radius: 14px; padding: 28px 24px; margin-bottom: 24px;">
            <div style="display: flex; gap: 8px; margin-bottom: 8px;">
                <span class="badge-pill">Project 02</span>
                <span class="badge-pill green">Seaborn Tips (244 Records)</span>
            </div>
            <h2 style="color: #ffffff; margin-bottom: 6px;">
                Data Visualization with Matplotlib & Seaborn
            </h2>
            <p style="color: #cbd5e1; font-size: 0.95rem; margin-bottom: 0;">
                Multivariate exploratory analysis exploring dining check totals, tip distributions, meal times, and party sizes.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Cross-Filtering Toolbar
    st.markdown("#### 🔍 Interactive Dashboard Filters")
    f_col1, f_col2, f_col3, f_col4 = st.columns([1.2, 1.2, 1.2, 1.4])

    with f_col1:
        day_options = ["All"] + list(df_raw["day"].unique())
        selected_day = st.selectbox("Filter by Day:", day_options, index=0)

    with f_col2:
        time_options = ["All"] + list(df_raw["time"].unique())
        selected_time = st.selectbox("Meal Time:", time_options, index=0)

    with f_col3:
        smoker_options = ["All", "No", "Yes"]
        selected_smoker = st.selectbox("Smoker Status:", smoker_options, index=0)

    with f_col4:
        bin_count = st.slider("Histogram Bins:", min_value=10, max_value=35, value=20, step=5)

    # Apply Filters
    df = df_raw.copy()
    if selected_day != "All":
        df = df[df["day"] == selected_day]
    if selected_time != "All":
        df = df[df["time"] == selected_time]
    if selected_smoker != "All":
        df = df[df["smoker"] == selected_smoker]

    st.caption(f"Showing **{len(df)}** of **{len(df_raw)}** verified dining checks based on active filters.")

    if len(df) == 0:
        st.warning("No records match the selected filter combination. Please broaden your selection.")
        render_project_nav(2)
        return

    # Real Dynamically Calculated KPI Cards
    avg_bill = df["total_bill"].mean()
    avg_tip = df["tip"].mean()
    avg_tip_pct = df["tip_pct"].mean()
    median_bill = df["total_bill"].median()
    median_tip = df["tip"].median()

    # Peak tip day in current subset
    day_means = df.groupby("day", observed=False)["tip"].mean()
    peak_day = day_means.idxmax() if not day_means.empty else "N/A"
    peak_day_val = day_means.max() if not day_means.empty else 0.0

    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">Active Records</div>
                <div class="metric-value">{len(df)}</div>
                <div class="metric-sub">Total unfiltered: 244</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with k2:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">Average Bill</div>
                <div class="metric-value">${avg_bill:.2f}</div>
                <div class="metric-sub">Median: ${median_bill:.2f}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with k3:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">Average Tip</div>
                <div class="metric-value" style="color: #38bdf8;">${avg_tip:.2f}</div>
                <div class="metric-sub">Median: ${median_tip:.2f}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with k4:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">Avg Tip Rate / Peak</div>
                <div class="metric-value" style="color: #34d399;">{avg_tip_pct:.1f}%</div>
                <div class="metric-sub">Top Day: {peak_day} (${peak_day_val:.2f})</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)

    # -------------------------------------------------------------
    # Visualizations Grid
    # -------------------------------------------------------------
    st.markdown("### 📈 Interactive Visual Analytics")

    # Chart 1 & Chart 2 (Row 1)
    ch_col1, ch_col2 = st.columns(2)

    with ch_col1:
        # Chart 1: Histogram (Distribution of Restaurant Bills)
        fig_hist = px.histogram(
            df,
            x="total_bill",
            nbins=bin_count,
            title="Chart 1: Distribution of Restaurant Bills",
            color_discrete_sequence=["#38bdf8"],
            opacity=0.8,
            labels={"total_bill": "Total Bill ($)"},
            template="plotly_dark",
        )
        fig_hist.add_vline(x=avg_bill, line_dash="dash", line_color="#fbbf24", annotation_text=f"Mean (${avg_bill:.2f})")
        fig_hist.add_vline(x=median_bill, line_dash="dot", line_color="#34d399", annotation_text=f"Median (${median_bill:.2f})")
        fig_hist.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(15,23,42,0.6)",
            margin=dict(l=40, r=20, t=50, b=40),
            yaxis_title="Check Frequency",
        )
        st.plotly_chart(fig_hist, use_container_width=True)
        st.caption("Right-skewed distribution. 50% of dining checks cluster tightly between $13.35 and $24.13.")

    with ch_col2:
        # Chart 2: Bar Chart (Average Tip by Day)
        day_order = ["Thur", "Fri", "Sat", "Sun"]
        day_avg = df.groupby("day", observed=False)["tip"].agg(["mean", "count"]).reindex(day_order).dropna()
        day_avg = day_avg.reset_index()

        fig_bar = px.bar(
            day_avg,
            x="day",
            y="mean",
            text=day_avg["mean"].apply(lambda v: f"${v:.2f}"),
            title="Chart 2: Average Tip by Day",
            color="day",
            color_discrete_map={"Thur": "#38bdf8", "Fri": "#818cf8", "Sat": "#a855f7", "Sun": "#ec4899"},
            labels={"mean": "Average Tip ($)", "day": "Day of Week"},
            template="plotly_dark",
        )
        fig_bar.update_traces(textposition="outside", showlegend=False)
        fig_bar.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(15,23,42,0.6)",
            margin=dict(l=40, r=20, t=50, b=40),
            yaxis=dict(range=[0, max(day_avg["mean"].max() * 1.25, 4.0)]),
        )
        st.plotly_chart(fig_bar, use_container_width=True)
        st.caption("Sunday consistently commands the highest average tip ($3.26 overall), followed by Saturday ($2.99).")

    # Chart 3 & Chart 4 (Row 2)
    ch_col3, ch_col4 = st.columns(2)

    with ch_col3:
        # Chart 3: Box Plot (Distribution of Tips Across Days)
        fig_box = px.box(
            df,
            x="day",
            y="tip",
            color="day",
            category_orders={"day": day_order},
            title="Chart 3: Distribution of Tips Across Days",
            color_discrete_map={"Thur": "#38bdf8", "Fri": "#818cf8", "Sat": "#a855f7", "Sun": "#ec4899"},
            labels={"tip": "Tip Amount ($)", "day": "Day of Week"},
            template="plotly_dark",
        )
        fig_box.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(15,23,42,0.6)",
            showlegend=False,
            margin=dict(l=40, r=20, t=50, b=40),
        )
        st.plotly_chart(fig_box, use_container_width=True)
        st.caption("Saturday displays the widest interquartile spread and contains the maximum outlier tip of $10.00.")

    with ch_col4:
        # Chart 4: Scatter Plot (Relationship Between Total Bill and Tip)
        fig_scatter = px.scatter(
            df,
            x="total_bill",
            y="tip",
            color="time",
            title="Chart 4: Relationship Between Total Bill and Tip",
            color_discrete_map={"Dinner": "#38bdf8", "Lunch": "#fbbf24"},
            labels={"total_bill": "Total Bill ($)", "tip": "Tip ($)", "time": "Meal Time"},
            hover_data=["size", "day", "smoker", "tip_pct"],
            template="plotly_dark",
        )
        fig_scatter.update_traces(marker=dict(size=9, opacity=0.85))

        # Add OLS regression trendline calculated directly via NumPy (eliminates statsmodels dependency)
        if len(df) > 1:
            x_vals = df["total_bill"].to_numpy()
            y_vals = df["tip"].to_numpy()
            slope, intercept = np.polyfit(x_vals, y_vals, 1)
            corr_mat = np.corrcoef(x_vals, y_vals)
            r_val = corr_mat[0, 1] if corr_mat.shape == (2, 2) else 0.0

            x_line = np.array([float(x_vals.min()), float(x_vals.max())])
            y_line = slope * x_line + intercept

            fig_scatter.add_trace(
                go.Scatter(
                    x=x_line,
                    y=y_line,
                    mode="lines",
                    name=f"Trend (r = {r_val:.3f})",
                    line=dict(color="#cbd5e1", width=2, dash="dash"),
                    hoverinfo="skip",
                )
            )

        fig_scatter.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(15,23,42,0.6)",
            margin=dict(l=40, r=20, t=50, b=40),
            legend=dict(
                bgcolor="rgba(15, 23, 42, 0.7)",
                bordercolor="#334155",
                borderwidth=1,
            ),
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
        st.caption("Strong positive linear correlation (r = 0.676). Higher total checks consistently scale dollar tips.")

    # Chart 5: Correlation Heatmap
    st.markdown("#### Chart 5: Correlation Heatmap (Numerical Variables)")
    num_cols = ["total_bill", "tip", "size"]
    corr_df = df[num_cols].corr()
    corr_df.columns = ["Total Bill", "Tip", "Party Size"]
    corr_df.index = ["Total Bill", "Tip", "Party Size"]

    fig_heat = px.imshow(
        corr_df,
        text_auto=".3f",
        aspect="auto",
        color_continuous_scale=[[0.0, "#0f172a"], [0.5, "#1e3a8a"], [1.0, "#38bdf8"]],
        zmin=0.0,
        zmax=1.0,
        title="Pearson Correlation Matrix (Numerical Attributes)",
        template="plotly_dark",
    )
    fig_heat.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(15,23,42,0.6)",
        margin=dict(l=60, r=40, t=50, b=40),
    )
    st.plotly_chart(fig_heat, use_container_width=True)

    # Key Empirical Insights
    st.markdown("### 💡 Evidence-Based Empirical Findings")
    st.markdown(
        r"""
        - **Modal Spending:** Over 53.7% of dining checks settle between $10.00 and $20.00. Bills exceeding $40.00 account for only 4.1% of all visits.
        - **Peak Gratuity Day:** Sunday achieves the highest average gratuity ($3.26), outperforming Thursday ($2.77) and Friday ($2.73).
        - **Saturday Volatility:** Saturday accounts for the largest transaction volume (87 receipts) and the highest tip dispersion (standard deviation of 1.63).
        - **Linear Scale vs Rate Decline:** While dollar tips increase steadily with check size ($r = 0.676$), tip percentages decline from ~18–20% on small checks to ~13–14% on checks over $40.00.
        - **Primary Driver:** Total Bill is the direct driver of gratuities ($r = 0.676$), whereas party size exerts its influence indirectly through expanded total check volume ($r = 0.598$).
        """
    )

    # Searchable Data Explorer & CSV Download
    st.markdown("### 🔍 Searchable Data Explorer")
    search_q = st.text_input("Quick search (filter by bill, tip, day, or size):", "")
    df_display = df.copy()
    if search_q:
        q = search_q.lower()
        df_display = df_display[
            df_display["day"].str.lower().str.contains(q)
            | df_display["time"].str.lower().str.contains(q)
            | df_display["sex"].str.lower().str.contains(q)
            | df_display["total_bill"].astype(str).str.contains(q)
            | df_display["tip"].astype(str).str.contains(q)
        ]

    st.dataframe(df_display, use_container_width=True)

    csv_data = df_display.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Filtered Data as CSV",
        data=csv_data,
        file_name=f"tips_filtered_{selected_day}_{selected_time}.csv",
        mime="text/csv",
    )

    # Methodology & Limitations
    with st.expander("📐 Methodology, Statistical Formula & Limitations"):
        st.markdown(
            r"""
            **Methodology & Data Origin:**
            - Dataset recorded by a restaurant food server over several months in a suburban restaurant (Bryant & Smith, 1995).
            - Contains 244 complete records with 0 missing or corrupted values.
            - Linear correlation is calculated via Pearson's formula:
              $$r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}$$
            
            **Correlation vs. Causation:**
            - Although Total Bill and Tip correlate strongly ($r = 0.676$), higher bills do not unilaterally *cause* generosity. Confounding variables include party size, occasion, alcohol consumption, and service quality.
            
            **Limitations:**
            - Single restaurant location from the 1990s; spending totals do not account for inflation or geographic tip culture variations.
            """
        )

    render_project_nav(2)
