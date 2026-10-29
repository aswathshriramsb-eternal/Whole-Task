"""
project3.py
Project 03: E-commerce Sales Trend Analysis.
Executive Business Intelligence dashboard analyzing 2,500 e-commerce transactions.
Features KPI cards, MoM growth, Pareto 80/20 analysis, monthly category pivot,
3 data-backed business recommendations, and a downloadable executive brief.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from modules.utils import load_ecommerce_data, render_project_nav


def render_project_3():
    """Render Project 03 E-commerce BI dashboard."""

    df_raw = load_ecommerce_data()
    if df_raw.empty:
        st.error("E-commerce dataset could not be loaded. Please ensure `data/ecommerce_data.csv` exists.")
        return

    # Convert Date to datetime
    df_raw["Date"] = pd.to_datetime(df_raw["Date"])
    df_raw["YearMonth"] = df_raw["Date"].dt.to_period("M").astype(str)

    st.markdown(
        """
        <div style="background: linear-gradient(135deg, #1e1b4b 0%, #152238 100%); 
                    border: 1px solid #4338ca; border-radius: 14px; padding: 28px 24px; margin-bottom: 24px;">
            <div style="display: flex; gap: 8px; margin-bottom: 8px;">
                <span class="badge-pill purple">Project 03</span>
                <span class="badge-pill">Synthetic Dataset (Seed 42 • 2,500 Orders)</span>
            </div>
            <h2 style="color: #ffffff; margin-bottom: 6px;">
                E-Commerce Sales Trend & Revenue Analysis
            </h2>
            <p style="color: #cbd5e1; font-size: 0.95rem; margin-bottom: 0;">
                Executive Business Intelligence platform evaluating 12-month revenue velocity, category share, customer Pareto concentration, and growth levers.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.info(
        "🏷️ **Data Integrity Notice:** This analysis utilizes a rigorously generated, reproducible synthetic dataset "
        "(2,500 transactions, fixed seed 42) designed with realistic retail seasonality and a Pareto power-law distribution. "
        "All figures reflect simulated business performance."
    )

    # Filtering Toolbar
    st.markdown("#### 🔍 BI Dashboard Filters")
    f_c1, f_c2, f_c3 = st.columns([1.5, 1.5, 1.2])

    with f_c1:
        min_date = df_raw["Date"].min().date()
        max_date = df_raw["Date"].max().date()
        date_range = st.date_input("Date Range:", (min_date, max_date))

    with f_c2:
        category_options = ["All Categories"] + sorted(list(df_raw["Product_Category"].unique()))
        selected_category = st.selectbox("Product Category:", category_options)

    with f_c3:
        status_options = ["Completed Only", "All Statuses (incl. Returns & Cancellations)"]
        selected_status = st.selectbox("Transaction Filter:", status_options)

    # Apply Filters
    df = df_raw.copy()
    if isinstance(date_range, (list, tuple)) and len(date_range) == 2:
        df = df[(df["Date"].dt.date >= date_range[0]) & (df["Date"].dt.date <= date_range[1])]

    if selected_category != "All Categories":
        df = df[df["Product_Category"] == selected_category]

    if selected_status == "Completed Only":
        df_active = df[df["Status"] == "Completed"]
    else:
        df_active = df

    if len(df_active) == 0:
        st.warning("No transactions match the selected criteria.")
        render_project_nav(3)
        return

    # -------------------------------------------------------------
    # Executive KPI Cards
    # -------------------------------------------------------------
    total_rev = df_active["Total_Amount"].sum()
    total_orders = len(df_active)
    unique_cust = df_active["Customer_ID"].nunique()
    aov = total_rev / total_orders if total_orders > 0 else 0

    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">Total Revenue</div>
                <div class="metric-value" style="color: #38bdf8;">${total_rev:,.2f}</div>
                <div class="metric-sub">Filter: {selected_status}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with k2:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">Transactions</div>
                <div class="metric-value">{total_orders:,}</div>
                <div class="metric-sub">Across 12 months</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with k3:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">Unique Customers</div>
                <div class="metric-value" style="color: #c084fc;">{unique_cust}</div>
                <div class="metric-sub">Active purchasers</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with k4:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">Avg Order Value (AOV)</div>
                <div class="metric-value" style="color: #34d399;">${aov:.2f}</div>
                <div class="metric-sub">Revenue per transaction</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)

    # -------------------------------------------------------------
    # Charts Grid: Monthly Trend & MoM Growth
    # -------------------------------------------------------------
    st.markdown("### 📈 Revenue Velocity & Seasonality")

    # Group by Month
    monthly = df_active.groupby("YearMonth")["Total_Amount"].sum().reset_index()
    monthly["MoM_Growth_Pct"] = monthly["Total_Amount"].pct_change() * 100

    c_trend, c_mom = st.columns(2)

    with c_trend:
        fig_trend = px.area(
            monthly,
            x="YearMonth",
            y="Total_Amount",
            title="Monthly Revenue Trend (2023)",
            labels={"Total_Amount": "Revenue ($)", "YearMonth": "Month"},
            color_discrete_sequence=["#38bdf8"],
            template="plotly_dark",
        )
        fig_trend.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(15,23,42,0.6)",
            margin=dict(l=40, r=20, t=50, b=40),
        )
        st.plotly_chart(fig_trend, use_container_width=True)
        st.caption("Strong upward momentum with dramatic Q4 spike in November & December driven by holiday promotions.")

    with c_mom:
        mom_clean = monthly.dropna(subset=["MoM_Growth_Pct"]).copy()
        mom_clean["Color"] = mom_clean["MoM_Growth_Pct"].apply(lambda v: "#10b981" if v >= 0 else "#f43f5e")

        fig_mom = px.bar(
            mom_clean,
            x="YearMonth",
            y="MoM_Growth_Pct",
            title="Month-over-Month (MoM) Revenue Growth Rate (%)",
            labels={"MoM_Growth_Pct": "Growth Rate (%)", "YearMonth": "Month"},
            color="Color",
            color_discrete_map="identity",
            template="plotly_dark",
        )
        fig_mom.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(15,23,42,0.6)",
            showlegend=False,
            margin=dict(l=40, r=20, t=50, b=40),
        )
        st.plotly_chart(fig_mom, use_container_width=True)
        st.caption("Monthly percentage acceleration. High positive gains in peak promotional quarters.")

    # -------------------------------------------------------------
    # Category Performance & Top 10 Customers
    # -------------------------------------------------------------
    st.markdown("### 🏷️ Category Share & High-Value Clients")
    c_cat, c_cust = st.columns(2)

    with c_cat:
        cat_rev = df_active.groupby("Product_Category")["Total_Amount"].sum().reset_index()
        cat_rev = cat_rev.sort_values(by="Total_Amount", ascending=True)

        fig_cat = px.bar(
            cat_rev,
            x="Total_Amount",
            y="Product_Category",
            orientation="h",
            title="Revenue Contribution by Product Category",
            labels={"Total_Amount": "Total Sales ($)", "Product_Category": "Category"},
            color="Total_Amount",
            color_continuous_scale="Viridis",
            template="plotly_dark",
        )
        fig_cat.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(15,23,42,0.6)",
            showlegend=False,
            margin=dict(l=40, r=20, t=50, b=40),
        )
        st.plotly_chart(fig_cat, use_container_width=True)
        st.caption("Electronics and Fashion & Apparel dominate gross merchandise value (GMV).")

    with c_cust:
        top10 = (
            df_active.groupby("Customer_ID")["Total_Amount"]
            .sum()
            .reset_index()
            .sort_values(by="Total_Amount", ascending=False)
            .head(10)
        )
        top10 = top10.sort_values(by="Total_Amount", ascending=True)

        fig_top10 = px.bar(
            top10,
            x="Total_Amount",
            y="Customer_ID",
            orientation="h",
            title="Top 10 Customers by Total Spend",
            labels={"Total_Amount": "Cumulative Spend ($)", "Customer_ID": "Customer ID"},
            color_discrete_sequence=["#818cf8"],
            template="plotly_dark",
        )
        fig_top10.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(15,23,42,0.6)",
            margin=dict(l=40, r=20, t=50, b=40),
        )
        st.plotly_chart(fig_top10, use_container_width=True)
        st.caption("VIP repeat buyers contribute disproportionately high enterprise value.")

    # -------------------------------------------------------------
    # Pareto Analysis (Lorenz 80/20 Curve)
    # -------------------------------------------------------------
    st.markdown("### ⚖️ Customer Pareto Analysis (80/20 Rule)")

    cust_spend = (
        df_active.groupby("Customer_ID")["Total_Amount"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    cust_spend["Cum_Revenue"] = cust_spend["Total_Amount"].cumsum()
    cust_spend["Cum_Rev_Pct"] = (cust_spend["Cum_Revenue"] / cust_spend["Total_Amount"].sum()) * 100
    cust_spend["Cust_Rank"] = np.arange(1, len(cust_spend) + 1)
    cust_spend["Cust_Pct"] = (cust_spend["Cust_Rank"] / len(cust_spend)) * 100

    # Calculate actual 20% mark
    top_20_pct_cust = int(len(cust_spend) * 0.20)
    top_20_rev_share = cust_spend.iloc[top_20_pct_cust]["Cum_Rev_Pct"] if top_20_pct_cust < len(cust_spend) else 100

    fig_pareto = go.Figure()
    fig_pareto.add_trace(
        go.Scatter(
            x=cust_spend["Cust_Pct"],
            y=cust_spend["Cum_Rev_Pct"],
            mode="lines",
            name="Lorenz Curve",
            line=dict(color="#38bdf8", width=3),
        )
    )
    # 45-degree reference line (perfect equality)
    fig_pareto.add_trace(
        go.Scatter(
            x=[0, 100],
            y=[0, 100],
            mode="lines",
            name="Equality Baseline",
            line=dict(color="#64748b", dash="dash"),
        )
    )
    # 80/20 guideline
    fig_pareto.add_vline(x=20, line_dash="dot", line_color="#fbbf24", annotation_text="Top 20% Customers")
    fig_pareto.add_hline(y=top_20_rev_share, line_dash="dot", line_color="#fbbf24", annotation_text=f"{top_20_rev_share:.1f}% Revenue")

    fig_pareto.update_layout(
        title=f"Customer Pareto Distribution: Top 20% Customers Drive {top_20_rev_share:.1f}% of Revenue",
        xaxis_title="Cumulative % of Customers",
        yaxis_title="Cumulative % of Revenue",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(15,23,42,0.6)",
        template="plotly_dark",
        margin=dict(l=40, r=20, t=50, b=40),
    )
    st.plotly_chart(fig_pareto, use_container_width=True)

    # -------------------------------------------------------------
    # Monthly Category Pivot Matrix
    # -------------------------------------------------------------
    st.markdown("### 🗂️ Monthly Category Pivot Table")
    pivot_df = pd.pivot_table(
        df_active,
        values="Total_Amount",
        index="Product_Category",
        columns="YearMonth",
        aggfunc="sum",
        fill_value=0,
    )
    st.dataframe(pivot_df.style.format("${:,.0f}").background_gradient(cmap="Blues"), use_container_width=True)

    # -------------------------------------------------------------
    # 3 Evidence-Based Business Recommendations
    # -------------------------------------------------------------
    st.markdown("### 💼 Actionable Business Recommendations")

    rec1, rec2, rec3 = st.columns(3)

    with rec1:
        st.markdown(
            f"""
            <div class="portfolio-card">
                <div style="font-weight: 700; color: #38bdf8; margin-bottom: 6px;">Recommendation #01</div>
                <h4 style="color: #ffffff; margin-bottom: 8px;">VIP Client Retention & Tiered Loyalty</h4>
                <p style="font-size: 0.88rem; color: #cbd5e1; line-height: 1.5;">
                    <strong>Supporting Evidence:</strong> The top 20% of buyers generate <strong>{top_20_rev_share:.1f}%</strong> of gross revenue.
                </p>
                <p style="font-size: 0.88rem; color: #cbd5e1; line-height: 1.5;">
                    <strong>Opportunity:</strong> Losing a single top-decile customer causes disproportionate top-line erosion.
                </p>
                <p style="font-size: 0.88rem; color: #cbd5e1; line-height: 1.5;">
                    <strong>Recommended Action:</strong> Institute an invite-only VIP concierge service and personalized quarterly rebate tiers.
                </p>
                <div style="background-color: #0f172a; padding: 8px; border-radius: 6px; font-size: 0.82rem; color: #34d399; font-weight: 600;">
                    Target KPI: Reduce top-decile churn by 15% (Threshold: >60 days inactivity proxy).
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with rec2:
        top_cat = cat_rev.iloc[-1]["Product_Category"]
        top_cat_sales = cat_rev.iloc[-1]["Total_Amount"]
        top_cat_share = (top_cat_sales / total_rev) * 100

        st.markdown(
            f"""
            <div class="portfolio-card">
                <div style="font-weight: 700; color: #c084fc; margin-bottom: 6px;">Recommendation #02</div>
                <h4 style="color: #ffffff; margin-bottom: 8px;">Category Expansion & Bundle Pricing</h4>
                <p style="font-size: 0.88rem; color: #cbd5e1; line-height: 1.5;">
                    <strong>Supporting Evidence:</strong> {top_cat} accounts for <strong>${top_cat_sales:,.0f}</strong> ({top_cat_share:.1f}% GMV).
                </p>
                <p style="font-size: 0.88rem; color: #cbd5e1; line-height: 1.5;">
                    <strong>Opportunity:</strong> High basket value categories have low cross-sell attachment to accessory categories.
                </p>
                <p style="font-size: 0.88rem; color: #cbd5e1; line-height: 1.5;">
                    <strong>Recommended Action:</strong> Introduce automated checkout bundles (e.g. hardware + warranty/accessories).
                </p>
                <div style="background-color: #0f172a; padding: 8px; border-radius: 6px; font-size: 0.82rem; color: #c084fc; font-weight: 600;">
                    Target KPI: Lift Average Order Value (AOV) by +12% from current ${aov:.2f}.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with rec3:
        q4_rev = df_active[df_active["Date"].dt.month.isin([11, 12])]["Total_Amount"].sum()
        q4_share = (q4_rev / total_rev) * 100 if total_rev > 0 else 0

        st.markdown(
            f"""
            <div class="portfolio-card">
                <div style="font-weight: 700; color: #fbbf24; margin-bottom: 6px;">Recommendation #03</div>
                <h4 style="color: #ffffff; margin-bottom: 8px;">Q4 Inventory & Working Capital Buffer</h4>
                <p style="font-size: 0.88rem; color: #cbd5e1; line-height: 1.5;">
                    <strong>Supporting Evidence:</strong> Nov & Dec sales total <strong>${q4_rev:,.0f}</strong> ({q4_share:.1f}% of annual GMV).
                </p>
                <p style="font-size: 0.88rem; color: #cbd5e1; line-height: 1.5;">
                    <strong>Opportunity:</strong> High holiday demand creates inventory stockout risks during peak holiday traffic.
                </p>
                <p style="font-size: 0.88rem; color: #cbd5e1; line-height: 1.5;">
                    <strong>Recommended Action:</strong> Advance supply chain procurement cycles to late August with safety stock buffers.
                </p>
                <div style="background-color: #0f172a; padding: 8px; border-radius: 6px; font-size: 0.82rem; color: #fbbf24; font-weight: 600;">
                    Target KPI: Maintain out-of-stock (OOS) rate below 2.0% during Q4 peak.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # -------------------------------------------------------------
    # Downloadable Executive Business Brief
    # -------------------------------------------------------------
    st.markdown("### 📄 Executive Business Brief")
    brief_content = f"""# EXECUTIVE E-COMMERCE BUSINESS INTELLIGENCE BRIEF
Generated from DataSphere AI Analytics Engine

## 1. Portfolio Performance Summary
- Total Revenue Analyzed: ${total_rev:,.2f}
- Completed Transactions: {total_orders:,}
- Unique Active Customers: {unique_cust:,}
- Average Order Value (AOV): ${aov:.2f}

## 2. Customer Concentration & Pareto Finding
- Top 20% of customers generate {top_20_rev_share:.1f}% of total annual sales.
- Churn Proxy Definition: Customers inactive for >60 days are flagged as churn risks.

## 3. Strategic Action Plan
1. Launch VIP Concierge & Tiered Loyalty (KPI: Churn reduction by 15%).
2. Bundle Accessory Packages with Top Category {top_cat} (KPI: +12% AOV growth).
3. Pre-position Q4 Holiday Inventory buffer (KPI: Maintain OOS < 2%).

Dataset: Synthetic 2,500 Transactions (Fixed Seed: 42)
Generated by DataSphere AI Portfolio.
"""
    st.download_button(
        label="📥 Download Executive Business Brief (Markdown Report)",
        data=brief_content,
        file_name="DataSphere_AI_Ecommerce_Business_Brief.md",
        mime="text/markdown",
    )

    # Transaction Explorer
    with st.expander("🔎 Browse Raw Transactions Table"):
        st.dataframe(df_active.head(200), use_container_width=True)

    render_project_nav(3)
