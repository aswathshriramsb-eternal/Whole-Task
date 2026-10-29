"""
project5.py
Project 05: Streamlit Interactive ML Web App.
Production inference interface loading the serialized Decision Tree pipeline.
Features passenger input parameters, real probability prediction, interactive gauge,
contextual evidence explanation, and downloadable prediction audit logs.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
from modules.utils import load_titanic_model, render_project_nav


def render_project_5():
    """Render Project 05 interactive machine learning prediction application."""

    st.markdown(
        """
        <div style="background: linear-gradient(135deg, #1e3a8a 0%, #152238 100%); 
                    border: 1px solid #2563eb; border-radius: 14px; padding: 28px 24px; margin-bottom: 24px;">
            <div style="display: flex; gap: 8px; margin-bottom: 8px;">
                <span class="badge-pill">Project 05</span>
                <span class="badge-pill green">Production Inference Engine</span>
                <span class="badge-pill purple">Joblib Pipeline</span>
            </div>
            <h2 style="color: #ffffff; margin-bottom: 6px;">
                Interactive Machine Learning Prediction Web App
            </h2>
            <p style="color: #cbd5e1; font-size: 0.95rem; margin-bottom: 0;">
                Live inference interface powered by the trained Decision Tree classifier (Project 04).
                Input passenger features to compute real-time survival probabilities with feature impact breakdowns.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Load model artifact
    bundle = load_titanic_model()
    if bundle is None:
        st.error(
            "⚠️ **Model Artifact Not Found:** `models/titanic_model.joblib` is missing.\n\n"
            "Please run `python train_model.py` in the project root to train and serialize the model artifact."
        )
        render_project_nav(5)
        return

    pipeline = bundle.get("pipeline")
    metadata = bundle.get("metadata", {})

    # Display Model Provenance Metadata
    with st.expander("ℹ️ Model Architecture & Provenance Verification"):
        m_c1, m_c2, m_c3, m_c4 = st.columns(4)
        m_c1.metric("Model Architecture", "Decision Tree (d=3)")
        m_c2.metric("Held-Out Test Acc", f"{metadata.get('test_accuracy', 0.7933)*100:.2f}%")
        m_c3.metric("Training Samples", f"{metadata.get('train_size', 712):,}")
        m_c4.metric("Test Samples", f"{metadata.get('test_size', 179):,}")

    st.markdown("### 🎛️ Passenger Profile Parameters")
    st.write("Configure passenger demographics and travel details to calculate survival likelihood:")

    # Input Form Layout
    in_col1, in_col2 = st.columns(2)

    with in_col1:
        pclass_label = st.selectbox(
            "Ticket Class (Economic Status):",
            ["1st Class (Upper / Luxury)", "2nd Class (Middle)", "3rd Class (Standard / Lower)"],
            index=0,
            help="Passenger socioeconomic status and deck proximity.",
        )
        pclass_map = {
            "1st Class (Upper / Luxury)": 1,
            "2nd Class (Middle)": 2,
            "3rd Class (Standard / Lower)": 3,
        }
        pclass = pclass_map[pclass_label]

        sex_label = st.radio(
            "Passenger Sex:",
            ["female", "male"],
            index=0,
            horizontal=True,
            help="Biological sex of passenger.",
        )
        sex = sex_label.lower()

    with in_col2:
        age = st.slider(
            "Passenger Age (Years):",
            min_value=1.0,
            max_value=80.0,
            value=28.0,
            step=1.0,
            help="Age in completed years at embarkation.",
        )

        fare = st.number_input(
            "Passenger Fare (£ British Pounds in 1912):",
            min_value=0.0,
            max_value=500.0,
            value=35.0,
            step=5.0,
            help="Ticket price paid in 1912 British currency. 3rd Class median was ~£8, 1st Class exceeded £70.",
        )

    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)

    # Prominent Prediction Button
    predict_clicked = st.button("🔮 PREDICT SURVIVAL PROBABILITY", type="primary", use_container_width=True)

    # In Streamlit, maintain prediction in session_state or evaluate on click
    if "p5_prediction" not in st.session_state:
        st.session_state["p5_prediction"] = None

    if predict_clicked:
        # Input Validation
        if not (1 <= pclass <= 3):
            st.error("Invalid ticket class selected.")
            return
        if sex not in ["female", "male"]:
            st.error("Invalid sex parameter.")
            return
        if not (0 < age <= 100):
            st.error("Age must be between 1 and 100.")
            return
        if fare < 0:
            st.error("Fare cannot be negative.")
            return

        # Prepare DataFrame with matching feature names
        input_df = pd.DataFrame(
            [{"pclass": pclass, "sex": sex, "age": float(age), "fare": float(fare)}]
        )

        try:
            # Model inference
            pred_class = int(pipeline.predict(input_df)[0])
            pred_proba_survive = float(pipeline.predict_proba(input_df)[0, 1])

            st.session_state["p5_prediction"] = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "pclass": pclass,
                "pclass_label": pclass_label,
                "sex": sex,
                "age": age,
                "fare": fare,
                "predicted_class": pred_class,
                "probability": pred_proba_survive,
            }
        except Exception as e:
            st.error(f"Inference execution failure: {e}")
            return

    # Render Prediction Output if Available
    pred = st.session_state["p5_prediction"]
    if pred is not None:
        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        st.markdown("### 🎯 Model Prediction Results")

        res_col1, res_col2 = st.columns([1.2, 1.8])

        is_survived = pred["probability"] >= 0.50
        prob_pct = pred["probability"] * 100

        with res_col1:
            if is_survived:
                st.markdown(
                    f"""
                    <div class="prediction-box-survived">
                        <div style="font-size: 0.85rem; font-weight: 700; text-transform: uppercase; color: #10b981; letter-spacing: 0.08em; margin-bottom: 6px;">
                            Predicted Outcome
                        </div>
                        <h2 style="color: #ffffff; margin-bottom: 8px;">LIKELY TO SURVIVE</h2>
                        <div style="font-size: 2.8rem; font-weight: 800; color: #34d399; line-height: 1;">
                            {prob_pct:.1f}%
                        </div>
                        <div style="font-size: 0.82rem; color: #cbd5e1; margin-top: 10px;">
                            Estimated Survival Likelihood
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    f"""
                    <div class="prediction-box-perished">
                        <div style="font-size: 0.85rem; font-weight: 700; text-transform: uppercase; color: #f43f5e; letter-spacing: 0.08em; margin-bottom: 6px;">
                            Predicted Outcome
                        </div>
                        <h2 style="color: #ffffff; margin-bottom: 8px;">UNLIKELY TO SURVIVE</h2>
                        <div style="font-size: 2.8rem; font-weight: 800; color: #f43f5e; line-height: 1;">
                            {prob_pct:.1f}%
                        </div>
                        <div style="font-size: 0.82rem; color: #cbd5e1; margin-top: 10px;">
                            Estimated Survival Likelihood
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        with res_col2:
            # Interactive Gauge Meter
            gauge_color = "#10b981" if is_survived else "#f43f5e"
            fig_gauge = go.Figure(
                go.Indicator(
                    mode="gauge+number",
                    value=prob_pct,
                    domain={"x": [0, 1], "y": [0, 1]},
                    title={"text": "Survival Probability Gauge", "font": {"color": "#cbd5e1", "size": 15}},
                    number={"suffix": "%", "font": {"color": "#ffffff", "size": 32}},
                    gauge={
                        "axis": {"range": [0, 100], "tickcolor": "#94a3b8", "tickfont": {"color": "#94a3b8"}},
                        "bar": {"color": gauge_color, "thickness": 0.3},
                        "bgcolor": "rgba(15, 23, 42, 0.6)",
                        "borderwidth": 1,
                        "bordercolor": "#334155",
                        "steps": [
                            {"range": [0, 40], "color": "rgba(244, 63, 94, 0.25)"},
                            {"range": [40, 60], "color": "rgba(251, 191, 36, 0.25)"},
                            {"range": [60, 100], "color": "rgba(16, 185, 129, 0.25)"},
                        ],
                        "threshold": {
                            "line": {"color": "#ffffff", "width": 3},
                            "thickness": 0.8,
                            "value": 50,
                        },
                    },
                )
            )
            fig_gauge.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(15,23,42,0.6)",
                margin=dict(l=20, r=20, t=40, b=20),
                height=220,
            )
            st.plotly_chart(fig_gauge, use_container_width=True)

        # Contextual Feature Explanation
        st.markdown("#### 🔬 Feature Attribution & Historical Context")
        explanation_text = ""
        if pred["sex"] == "female":
            explanation_text += (
                "- **Sex (Female):** Female passengers had prioritized access to lifeboats under maritime protocol, "
                "substantially raising survival likelihood.\n"
            )
        else:
            explanation_text += (
                "- **Sex (Male):** Male passengers experienced high mortality due to lifeboat evacuation priority given to women and children.\n"
            )

        if pred["pclass"] == 1:
            explanation_text += (
                "- **Ticket Class (1st Class):** 1st Class cabins were situated on the upper decks with immediate access to lifeboat davits.\n"
            )
        elif pred["pclass"] == 3:
            explanation_text += (
                "- **Ticket Class (3rd Class):** 3rd Class cabins were located deep in lower decks, creating severe egress bottlenecks during evacuation.\n"
            )

        if pred["age"] < 16:
            explanation_text += "- **Age (< 16 years):** Child status conferred priority lifeboat boarding.\n"

        st.markdown(explanation_text)

        # Downloadable Prediction CSV
        audit_row = pd.DataFrame(
            [
                {
                    "timestamp": pred["timestamp"],
                    "pclass": pred["pclass"],
                    "sex": pred["sex"],
                    "age": pred["age"],
                    "fare": pred["fare"],
                    "predicted_survival": "Yes" if is_survived else "No",
                    "survival_probability_pct": round(prob_pct, 2),
                }
            ]
        )
        csv_audit = audit_row.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download Prediction Audit Log as CSV",
            data=csv_audit,
            file_name=f"titanic_prediction_{pred['sex']}_pclass{pred['pclass']}.csv",
            mime="text/csv",
        )

    # Educational Disclaimer
    st.markdown("---")
    st.caption(
        "⚠️ **Educational Simulation Disclaimer:** This machine learning prediction tool is an educational portfolio "
        "demonstration fitted exclusively on historical archival records from the 1912 RMS Titanic manifest. "
        "It does not represent modern maritime safety modeling, modern navigation standards, or contemporary emergency protocols."
    )

    render_project_nav(5)
