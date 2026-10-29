"""
app.py
DataSphere AI: Unified Data Science & AI Portfolio Web Application.
Main entry point connecting Projects 01 through 05 under a cohesive, interactive architecture.
"""

import streamlit as st
from modules.utils import apply_custom_theme
from modules.home import render_home
from modules.project1 import render_project_1
from modules.project2 import render_project_2
from modules.project3 import render_project_3
from modules.project4 import render_project_4
from modules.project5 import render_project_5

# Configure Streamlit Page
st.set_page_config(
    page_title="DataSphere AI | Data Science & AI Portfolio",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Apply unified dark navy styling
apply_custom_theme()

# Initialize Session State Routing
if "selected_project" not in st.session_state:
    st.session_state["selected_project"] = 0

# Mapping of Project IDs to Labels
PROJECT_MAP = {
    0: "🏠 Portfolio Home",
    1: "1️⃣ Project 01: Titanic EDA (Foundation)",
    2: "2️⃣ Project 02: Data Visualization (Tips)",
    3: "3️⃣ Project 03: E-Commerce Trends (BI)",
    4: "4️⃣ Project 04: ML Classifier (Titanic)",
    5: "5️⃣ Project 05: Interactive ML App",
}

# -----------------------------------------------------------------------------
# SIDEBAR NAVIGATION
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown(
        """
        <div style="padding: 10px 0 16px 0;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <div style="background: linear-gradient(135deg, #0284c7 0%, #38bdf8 100%); 
                            width: 36px; height: 36px; border-radius: 8px; display: flex; 
                            align-items: center; justify-content: center; font-size: 1.2rem; font-weight: 800;">
                    🌐
                </div>
                <div>
                    <h2 style="font-size: 1.25rem; font-weight: 800; color: #ffffff; margin: 0; line-height: 1.1;">
                        DataSphere <span style="color: #38bdf8;">AI</span>
                    </h2>
                    <span style="font-size: 0.72rem; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.08em; font-weight: 600;">
                        Projects 01–05 Portfolio
                    </span>
                </div>
            </div>
            <p style="font-size: 0.8rem; color: #cbd5e1; font-style: italic; margin-top: 10px; margin-bottom: 0;">
                From Raw Data to Intelligent Applications.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.markdown("<div style='font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: #64748b; margin-bottom: 6px;'>Select Project Dashboard</div>", unsafe_allow_html=True)

    # Radio Selector linked to session state
    nav_keys = list(PROJECT_MAP.keys())
    nav_labels = [PROJECT_MAP[k] for k in nav_keys]
    current_index = nav_keys.index(st.session_state["selected_project"])

    chosen_label = st.radio(
        label="Project Navigation",
        options=nav_labels,
        index=current_index,
        label_visibility="collapsed",
    )

    # Synchronize state when sidebar radio is changed
    for k, v in PROJECT_MAP.items():
        if v == chosen_label:
            if st.session_state["selected_project"] != k:
                st.session_state["selected_project"] = k
                st.rerun()

    st.markdown("---")

    # Quick Jump to Home
    if st.session_state["selected_project"] != 0:
        if st.button("🏠 Return to Portfolio Home", use_container_width=True):
            st.session_state["selected_project"] = 0
            st.rerun()

    # Sidebar Datasets Status Widget
    st.markdown(
        """
        <div style="background-color: #152238; border: 1px solid #1e293b; border-radius: 8px; padding: 12px; margin-top: 14px;">
            <div style="font-size: 0.75rem; font-weight: 700; color: #38bdf8; text-transform: uppercase; margin-bottom: 6px;">
                Verified Datasets
            </div>
            <div style="font-size: 0.78rem; color: #cbd5e1; line-height: 1.5;">
                • <strong>P02:</strong> Tips (244 records)<br>
                • <strong>P03:</strong> E-Comm (2,500 orders)<br>
                • <strong>P04/P05:</strong> Titanic (891 rows)
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.markdown(
        """
        <div style="font-size: 0.75rem; color: #64748b; line-height: 1.5;">
            <strong>InternCircle Portfolio</strong><br>
            Student Developer: Aswath<br>
            Python 3.13 • Streamlit 1.66<br>
            <a href="https://github.com/your-username/datasphere-ai" target="_blank" style="color: #38bdf8; text-decoration: none;">GitHub Repository ↗</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------------------------------------------------------
# TOP NAVBAR BREADCRUMB
# -----------------------------------------------------------------------------
active_proj = st.session_state["selected_project"]
active_name = PROJECT_MAP.get(active_proj, "Portfolio Home")

st.markdown(
    f"""
    <div class="top-navbar">
        <div style="display: flex; align-items: center; gap: 12px;">
            <span style="color: #64748b; font-size: 0.88rem;">DataSphere AI</span>
            <span style="color: #334155;">/</span>
            <span style="color: #f8fafc; font-weight: 700; font-size: 0.95rem;">{active_name}</span>
        </div>
        <div>
            <span class="badge-pill" style="margin: 0;">Interactive Portfolio</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# DYNAMIC ROUTING DISPATCHER
# -----------------------------------------------------------------------------
if active_proj == 0:
    render_home()
elif active_proj == 1:
    render_project_1()
elif active_proj == 2:
    render_project_2()
elif active_proj == 3:
    render_project_3()
elif active_proj == 4:
    render_project_4()
elif active_proj == 5:
    render_project_5()
else:
    render_home()

# Global Footer
st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; font-size: 0.82rem; color: #64748b; padding: 12px 0 24px 0;">
        DataSphere AI • InternCircle Unified Data Science & AI Portfolio • Projects 01–05<br>
        All metrics and models verified against real and reproducible datasets.
    </div>
    """,
    unsafe_allow_html=True,
)
