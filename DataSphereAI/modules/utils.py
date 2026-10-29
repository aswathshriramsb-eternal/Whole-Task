"""
utils.py
Shared utilities, theme styling, dataset caching, and navigation helpers for DataSphere AI.
"""

import os
import joblib
import pandas as pd
import streamlit as st

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
MODEL_DIR = os.path.join(BASE_DIR, "models")


def apply_custom_theme():
    """Inject modern dark navy and cobalt theme CSS."""
    st.markdown(
        """
        <style>
        /* Global Page Background and Typography */
        .stApp {
            background-color: #080d1a;
            color: #f8fafc;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }

        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: #0f172a !important;
            border-right: 1px solid #1e293b;
        }

        [data-testid="stSidebar"] hr {
            margin: 1rem 0;
            border-color: #1e293b;
        }

        /* Top Header Container */
        .top-navbar {
            background: linear-gradient(90deg, #0f172a 0%, #152238 100%);
            border: 1px solid #1e293b;
            border-radius: 12px;
            padding: 16px 24px;
            margin-bottom: 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        /* Custom Cards */
        .portfolio-card {
            background: linear-gradient(135deg, #0f172a 0%, #152238 100%);
            border: 1px solid #1e3a5f;
            border-radius: 14px;
            padding: 24px;
            margin-bottom: 20px;
            box-shadow: 0 4px 20px -2px rgba(2, 6, 23, 0.7);
            transition: transform 0.2s ease, border-color 0.2s ease;
        }

        .portfolio-card:hover {
            transform: translateY(-2px);
            border-color: #38bdf8;
        }

        /* Metric Cards */
        .metric-card {
            background-color: #152238;
            border: 1px solid #1e293b;
            border-radius: 12px;
            padding: 18px 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.4);
        }

        .metric-title {
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: #94a3b8;
            font-weight: 600;
            margin-bottom: 6px;
        }

        .metric-value {
            font-size: 1.8rem;
            font-weight: 800;
            color: #ffffff;
            letter-spacing: -0.02em;
            line-height: 1.1;
        }

        .metric-sub {
            font-size: 0.75rem;
            color: #64748b;
            margin-top: 6px;
        }

        /* Badge Pills */
        .badge-pill {
            display: inline-block;
            font-size: 0.72rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            padding: 4px 10px;
            border-radius: 20px;
            background-color: rgba(56, 189, 248, 0.12);
            color: #38bdf8;
            border: 1px solid rgba(56, 189, 248, 0.25);
            margin-right: 6px;
        }

        .badge-pill.purple {
            background-color: rgba(168, 85, 247, 0.12);
            color: #c084fc;
            border-color: rgba(168, 85, 247, 0.25);
        }

        .badge-pill.green {
            background-color: rgba(16, 185, 129, 0.12);
            color: #34d399;
            border-color: rgba(16, 185, 129, 0.25);
        }

        .badge-pill.amber {
            background-color: rgba(251, 191, 36, 0.12);
            color: #fbbf24;
            border-color: rgba(251, 191, 36, 0.25);
        }

        /* Learning Journey Flow */
        .journey-step {
            background-color: #111d38;
            border: 1px solid #1e3a5f;
            border-radius: 10px;
            padding: 14px 16px;
            text-align: center;
        }

        /* Streamlit Input & Widget adjustments */
        div[data-baseweb="select"] > div {
            background-color: #0f172a !important;
            border-color: #334155 !important;
            color: #f8fafc !important;
        }

        .stButton>button {
            border-radius: 8px;
            font-weight: 600;
            transition: all 0.2s ease;
        }

        /* Prediction Result Box */
        .prediction-box-survived {
            background: linear-gradient(135deg, rgba(16, 185, 129, 0.15) 0%, rgba(6, 95, 70, 0.3) 100%);
            border: 1px solid #10b981;
            border-radius: 14px;
            padding: 24px;
            text-align: center;
        }

        .prediction-box-perished {
            background: linear-gradient(135deg, rgba(244, 63, 94, 0.15) 0%, rgba(136, 19, 55, 0.3) 100%);
            border: 1px solid #f43f5e;
            border-radius: 14px;
            padding: 24px;
            text-align: center;
        }

        /* Hide Streamlit Default Watermark */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """,
        unsafe_allow_html=True,
    )


@st.cache_data
def load_tips_data():
    """Load and cache the authentic 244-row Seaborn Tips dataset."""
    path = os.path.join(DATA_DIR, "tips.csv")
    if not os.path.exists(path):
        import seaborn as sns
        df = sns.load_dataset("tips")
        os.makedirs(DATA_DIR, exist_ok=True)
        df.to_csv(path, index=False)
        return df
    return pd.read_csv(path)


@st.cache_data
def load_ecommerce_data():
    """Load and cache the 2,500-transaction synthetic e-commerce dataset."""
    path = os.path.join(DATA_DIR, "ecommerce_data.csv")
    if not os.path.exists(path):
        st.error(f"E-commerce dataset not found at {path}. Run `generate_ecommerce.py` first.")
        return pd.DataFrame()
    return pd.read_csv(path)


@st.cache_data
def load_titanic_data():
    """Load and cache the 891-row Titanic passenger dataset."""
    path = os.path.join(DATA_DIR, "titanic.csv")
    if not os.path.exists(path):
        st.error(f"Titanic dataset not found at {path}.")
        return pd.DataFrame()
    return pd.read_csv(path)


@st.cache_resource
def load_titanic_model():
    """Load and cache the serialized Decision Tree ML Pipeline."""
    path = os.path.join(MODEL_DIR, "titanic_model.joblib")
    if not os.path.exists(path):
        return None
    try:
        return joblib.load(path)
    except Exception as e:
        st.error(f"Failed to load model artifact: {e}")
        return None


def render_project_nav(current_id):
    """Render consistent Previous / Next project and Return to Portfolio buttons."""
    project_names = {
        0: "Portfolio Home",
        1: "P01: AI Foundation",
        2: "P02: Data Visualization",
        3: "P03: E-Commerce Trends",
        4: "P04: ML Classifier",
        5: "P05: Interactive ML App",
    }

    st.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        if current_id > 1:
            prev_id = current_id - 1
            if st.button(f"← Previous: {project_names[prev_id]}", use_container_width=True):
                st.session_state["selected_project"] = prev_id
                st.rerun()
        else:
            if st.button("← Back to Portfolio Home", use_container_width=True):
                st.session_state["selected_project"] = 0
                st.rerun()

    with col2:
        if st.button("🏠 Portfolio Overview", use_container_width=True):
            st.session_state["selected_project"] = 0
            st.rerun()

    with col3:
        if current_id < 5:
            next_id = current_id + 1
            if st.button(f"Next: {project_names[next_id]} →", use_container_width=True):
                st.session_state["selected_project"] = next_id
                st.rerun()
        else:
            if st.button("↺ Back to Project 01", use_container_width=True):
                st.session_state["selected_project"] = 1
                st.rerun()
