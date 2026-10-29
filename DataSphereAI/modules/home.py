"""
home.py
Landing page for DataSphere AI.
Features hero section, verified portfolio metrics, 5 interactive project cards,
clickable visual learning journey, and verified technology stack.
"""

import streamlit as st


def render_home():
    """Render the main landing page of DataSphere AI."""

    # Hero Section
    st.markdown(
        """
        <div style="background: linear-gradient(135deg, #0d1a33 0%, #152238 60%, #0f1d36 100%); 
                    border: 1px solid #1e3a5f; border-radius: 16px; padding: 36px 32px; margin-bottom: 28px;">
            <div style="display: flex; gap: 8px; margin-bottom: 12px; flex-wrap: wrap;">
                <span class="badge-pill">InternCircle Portfolio</span>
                <span class="badge-pill purple">Data Science & AI</span>
                <span class="badge-pill green">Production Ready</span>
            </div>
            <h1 style="font-size: 2.6rem; font-weight: 800; color: #ffffff; margin-bottom: 8px; letter-spacing: -0.03em;">
                DataSphere <span style="background: linear-gradient(90deg, #38bdf8 0%, #818cf8 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">AI</span>
            </h1>
            <p style="font-size: 1.25rem; font-style: italic; color: #94a3b8; margin-bottom: 16px;">
                From Raw Data to Intelligent Applications.
            </p>
            <p style="font-size: 1.05rem; color: #cbd5e1; max-width: 880px; line-height: 1.6; margin-bottom: 24px;">
                A unified, end-to-end portfolio tracking my progression across five core data disciplines:
                exploratory analysis, statistical visualization, e-commerce business analytics,
                predictive classification modeling, and real-time interactive machine learning deployment.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Hero Action Buttons
    col_act1, col_act2, col_act3 = st.columns([1.2, 1.4, 1.4])
    with col_act1:
        if st.button("🚀 Explore All Projects", use_container_width=True, type="primary"):
            st.session_state["selected_project"] = 2
            st.rerun()
    with col_act2:
        if st.button("⚡ Open Featured ML App (P05)", use_container_width=True):
            st.session_state["selected_project"] = 5
            st.rerun()
    with col_act3:
        st.markdown(
            """
            <a href="https://github.com/your-username/datasphere-ai" target="_blank" style="text-decoration: none;">
                <div style="background-color: #152238; border: 1px solid #334155; border-radius: 8px; 
                            padding: 8px 16px; text-align: center; color: #f8fafc; font-weight: 600; font-size: 0.95rem;">
                    📂 View GitHub Repository ↗
                </div>
            </a>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

    # Real Portfolio Statistics (No fabricated metrics)
    st.markdown("### 📊 Verified Portfolio Statistics")
    stat_c1, stat_c2, stat_c3, stat_c4 = st.columns(4)

    with stat_c1:
        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-title">Total Projects</div>
                <div class="metric-value">5</div>
                <div class="metric-sub">Complete unified modules</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with stat_c2:
        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-title">Real Datasets</div>
                <div class="metric-value">3</div>
                <div class="metric-sub">Tips, E-Commerce, Titanic</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with stat_c3:
        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-title">Analyzed Records</div>
                <div class="metric-value">3,635</div>
                <div class="metric-sub">244 + 2,500 + 891 records</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with stat_c4:
        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-title">ML Test Accuracy</div>
                <div class="metric-value" style="color: #38bdf8;">79.33%</div>
                <div class="metric-sub">+17.88% over 61.45% baseline</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)

    # Interactive Learning Journey
    st.markdown("### 🗺️ Visual Learning Journey")
    st.caption("Click any stage below to jump directly to its corresponding project dashboard:")

    j_c1, j_c2, j_c3, j_c4, j_c5 = st.columns(5)
    with j_c1:
        if st.button("1️⃣ Data Analysis\n(P01: Foundation)", use_container_width=True):
            st.session_state["selected_project"] = 1
            st.rerun()
    with j_c2:
        if st.button("2️⃣ Visualization\n(P02: Tips EDA)", use_container_width=True):
            st.session_state["selected_project"] = 2
            st.rerun()
    with j_c3:
        if st.button("3️⃣ Business BI\n(P03: E-Commerce)", use_container_width=True):
            st.session_state["selected_project"] = 3
            st.rerun()
    with j_c4:
        if st.button("4️⃣ Core ML\n(P04: Classifier)", use_container_width=True):
            st.session_state["selected_project"] = 4
            st.rerun()
    with j_c5:
        if st.button("5️⃣ ML Web App\n(P05: Predictor)", use_container_width=True):
            st.session_state["selected_project"] = 5
            st.rerun()

    st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)

    # 5 Project Cards Grid
    st.markdown("### 📂 Portfolio Projects (01–05)")

    # Row 1: Projects 1 & 2
    p_col1, p_col2 = st.columns(2)

    with p_col1:
        st.markdown(
            """
            <div class="portfolio-card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <span class="badge-pill amber">Project 01</span>
                    <span style="font-size: 0.8rem; color: #94a3b8;">1–2 Weeks • Foundation & EDA</span>
                </div>
                <h3 style="color: #ffffff; margin-bottom: 8px;">Exploratory Data Analysis on RMS Titanic</h3>
                <p style="font-size: 0.9rem; color: #cbd5e1; line-height: 1.5; min-height: 55px;">
                    Rigorous descriptive data investigation evaluating gender disparities (+55.3%), class gradients (2.5x), and age cohorts with zero ML constraint.
                </p>
                <div style="margin-bottom: 14px;">
                    <span class="badge-pill" style="font-size: 0.7rem;">Pandas</span>
                    <span class="badge-pill" style="font-size: 0.7rem;">Seaborn</span>
                    <span class="badge-pill" style="font-size: 0.7rem;">Data Cleaning</span>
                    <span class="badge-pill" style="font-size: 0.7rem;">891 Passengers</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Explore Project 01 →", key="btn_p1", use_container_width=True):
            st.session_state["selected_project"] = 1
            st.rerun()

    with p_col2:
        st.markdown(
            """
            <div class="portfolio-card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <span class="badge-pill">Project 02</span>
                    <span style="font-size: 0.8rem; color: #94a3b8;">1 Week • Intermediate</span>
                </div>
                <h3 style="color: #ffffff; margin-bottom: 8px;">Data Visualization with Matplotlib & Seaborn</h3>
                <p style="font-size: 0.9rem; color: #cbd5e1; line-height: 1.5; min-height: 55px;">
                    In-depth exploratory visual analytics of 244 restaurant dining checks. Analyzes distributions, weekly tip trends, regression lines, and correlation matrices.
                </p>
                <div style="margin-bottom: 14px;">
                    <span class="badge-pill" style="font-size: 0.7rem;">Matplotlib</span>
                    <span class="badge-pill" style="font-size: 0.7rem;">Seaborn</span>
                    <span class="badge-pill" style="font-size: 0.7rem;">Plotly</span>
                    <span class="badge-pill" style="font-size: 0.7rem;">Tips (244)</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Explore Project 02 →", key="btn_p2", use_container_width=True):
            st.session_state["selected_project"] = 2
            st.rerun()

    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)

    # Row 2: Projects 3 & 4
    p_col3, p_col4 = st.columns(2)

    with p_col3:
        st.markdown(
            """
            <div class="portfolio-card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <span class="badge-pill purple">Project 03</span>
                    <span style="font-size: 0.8rem; color: #94a3b8;">2 Weeks • Business Analytics</span>
                </div>
                <h3 style="color: #ffffff; margin-bottom: 8px;">E-Commerce Sales Trend Analysis</h3>
                <p style="font-size: 0.9rem; color: #cbd5e1; line-height: 1.5; min-height: 55px;">
                    Executive BI dashboard analyzing 2,500 retail transactions. Evaluates MoM revenue growth, Pareto 80/20 customer distribution, and 3 data-driven business recommendations.
                </p>
                <div style="margin-bottom: 14px;">
                    <span class="badge-pill purple" style="font-size: 0.7rem;">Pareto Analysis</span>
                    <span class="badge-pill purple" style="font-size: 0.7rem;">KPI Tracking</span>
                    <span class="badge-pill purple" style="font-size: 0.7rem;">Pivot Tables</span>
                    <span class="badge-pill purple" style="font-size: 0.7rem;">2,500 Orders</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Explore Project 03 →", key="btn_p3", use_container_width=True):
            st.session_state["selected_project"] = 3
            st.rerun()

    with p_col4:
        st.markdown(
            """
            <div class="portfolio-card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <span class="badge-pill green">Project 04</span>
                    <span style="font-size: 0.8rem; color: #94a3b8;">2 Weeks • Core ML</span>
                </div>
                <h3 style="color: #ffffff; margin-bottom: 8px;">First Machine Learning Classifier</h3>
                <p style="font-size: 0.9rem; color: #cbd5e1; line-height: 1.5; min-height: 55px;">
                    Titanic passenger survival classification using Scikit-learn Decision Trees. Evaluates held-out test data, confusion matrix, tree depth tuning (1–12), and feature importances.
                </p>
                <div style="margin-bottom: 14px;">
                    <span class="badge-pill green" style="font-size: 0.7rem;">Scikit-learn</span>
                    <span class="badge-pill green" style="font-size: 0.7rem;">Decision Tree</span>
                    <span class="badge-pill green" style="font-size: 0.7rem;">Overfitting Curve</span>
                    <span class="badge-pill green" style="font-size: 0.7rem;">79.33% Acc</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Explore Project 04 →", key="btn_p4", use_container_width=True):
            st.session_state["selected_project"] = 4
            st.rerun()

    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)

    # Row 3: Project 5 (Featured interactive app)
    st.markdown(
        """
        <div class="portfolio-card" style="border-color: #38bdf8;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span class="badge-pill" style="background-color: rgba(56, 189, 248, 0.2);">Project 05 • Featured Application</span>
                <span style="font-size: 0.8rem; color: #94a3b8;">1 Week • Deployment & Interactive AI</span>
            </div>
            <h3 style="color: #ffffff; margin-bottom: 8px;">Streamlit Interactive ML Web App</h3>
            <p style="font-size: 0.95rem; color: #cbd5e1; line-height: 1.6;">
                Transforms the trained Titanic classification pipeline into a real-time, interactive survival prediction engine.
                Input passenger characteristics (Ticket Class, Sex, Age, Fare) to calculate real predicted probabilities with interactive gauges,
                evidence explanations, and downloadable prediction audit logs.
            </p>
            <div style="margin-bottom: 14px;">
                <span class="badge-pill" style="font-size: 0.7rem;">Streamlit</span>
                <span class="badge-pill" style="font-size: 0.7rem;">Joblib Cache</span>
                <span class="badge-pill" style="font-size: 0.7rem;">Real-Time Inference</span>
                <span class="badge-pill" style="font-size: 0.7rem;">CSV Export</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("⚡ Launch Interactive Prediction App (P05) →", key="btn_p5", type="primary", use_container_width=True):
        st.session_state["selected_project"] = 5
        st.rerun()

    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

    # Technologies Section
    st.markdown("### 🛠️ Verified Technology Stack")
    t_c1, t_c2, t_c3, t_c4 = st.columns(4)

    with t_c1:
        st.markdown(
            """
            <div class="metric-card">
                <div style="font-weight: 700; color: #38bdf8; margin-bottom: 4px;">Core Language</div>
                <div style="font-size: 1.1rem; font-weight: 800; color: #ffffff;">Python 3.13</div>
                <div class="metric-sub">NumPy, Pandas, Standard Library</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with t_c2:
        st.markdown(
            """
            <div class="metric-card">
                <div style="font-weight: 700; color: #c084fc; margin-bottom: 4px;">Data Visualization</div>
                <div style="font-size: 1.1rem; font-weight: 800; color: #ffffff;">Plotly & Seaborn</div>
                <div class="metric-sub">Matplotlib, Plotly.js, Responsive Canvas</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with t_c3:
        st.markdown(
            """
            <div class="metric-card">
                <div style="font-weight: 700; color: #34d399; margin-bottom: 4px;">Machine Learning</div>
                <div style="font-size: 1.1rem; font-weight: 800; color: #ffffff;">Scikit-learn 1.9</div>
                <div class="metric-sub">Decision Trees, Pipelines, Joblib Serialization</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with t_c4:
        st.markdown(
            """
            <div class="metric-card">
                <div style="font-weight: 700; color: #fbbf24; margin-bottom: 4px;">Application & Web</div>
                <div style="font-size: 1.1rem; font-weight: 800; color: #ffffff;">Streamlit 1.66</div>
                <div class="metric-sub">Session Routing, Component Caching, Git</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
