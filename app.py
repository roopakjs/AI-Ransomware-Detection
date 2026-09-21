import streamlit as st
import pandas as pd
import joblib
import json

from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Sentinel | AI Threat Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
<style>

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(30, 136, 229, 0.10),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 20%,
            rgba(0, 188, 212, 0.08),
            transparent 30%
        ),
        #080c14;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1400px;
}


/* =========================
   SIDEBAR
   ========================= */

section[data-testid="stSidebar"] {
    background: #0b111c;
    border-right: 1px solid rgba(255,255,255,0.08);
}

section[data-testid="stSidebar"] .block-container {
    padding-top: 2rem;
}


/* =========================
   METRICS
   ========================= */

div[data-testid="stMetric"] {
    background:
        linear-gradient(
            145deg,
            rgba(19,30,47,0.95),
            rgba(10,17,29,0.95)
        );

    border: 1px solid rgba(255,255,255,0.07);

    padding: 18px 20px;

    border-radius: 15px;

    box-shadow:
        0 8px 25px rgba(0,0,0,0.22);
}

div[data-testid="stMetricLabel"] {
    color: #8294aa;
}

div[data-testid="stMetricValue"] {
    font-weight: 800;
}


/* =========================
   SECTION HEADERS
   ========================= */

.section-title {
    font-size: 22px;
    font-weight: 750;
    margin-top: 30px;
    margin-bottom: 8px;
}

.section-description {
    color: #8495aa;
    font-size: 14px;
    margin-bottom: 18px;
}


/* =========================
   UPLOAD AREA
   ========================= */

section[data-testid="stFileUploaderDropzone"] {
    background: rgba(11,20,33,0.75);
    border: 1px dashed rgba(85,182,255,0.30);
    border-radius: 14px;
}


/* =========================
   DATAFRAME
   ========================= */

div[data-testid="stDataFrame"] {
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.07);
}


/* =========================
   BUTTON
   ========================= */

.stDownloadButton button {
    border-radius: 10px;
    font-weight: 650;
}


/* =========================
   FOOTER
   ========================= */

.footer {
    text-align: center;
    color: #53657b;
    font-size: 12px;
    padding: 35px 0 10px 0;
}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# FILE PATHS
# ============================================================

MODEL_FILE = Path("models/ransomware_model.pkl")

FEATURE_FILE = Path("models/feature_names.json")

METRICS_FILE = Path("reports/results/metrics.json")


# ============================================================
# LOAD MODEL
# ============================================================

try:

    model = joblib.load(MODEL_FILE)

except Exception as e:

    st.error(
        f"Unable to load trained model: {e}"
    )

    st.stop()


# ============================================================
# LOAD FEATURE NAMES
# ============================================================

try:

    with open(
        FEATURE_FILE,
        "r"
    ) as file:

        feature_names = json.load(file)

except Exception as e:

    st.error(
        f"Unable to load feature names: {e}"
    )

    st.stop()


# ============================================================
# LOAD METRICS
# ============================================================

metrics = None

if METRICS_FILE.exists():

    try:

        with open(
            METRICS_FILE,
            "r"
        ) as file:

            metrics = json.load(file)

    except Exception:

        metrics = None


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.html(
        """
        <div style="
            font-size:25px;
            font-weight:800;
            margin-bottom:5px;
        ">
            🛡️ SENTINEL
        </div>

        <div style="
            color:#71839a;
            font-size:13px;
            margin-bottom:25px;
        ">
            AI Threat Detection Platform
        </div>
        """
    )

    st.markdown("### System")

    st.success(
        "● Detection Engine Online"
    )

    st.markdown("---")

    st.markdown("### Model")

    st.write(
        "**Algorithm:** Random Forest"
    )

    st.write(
        f"**Features:** {len(feature_names)}"
    )

    st.write(
        "**Mode:** Classification"
    )

    st.markdown("---")

    st.caption(
        "Defensive cybersecurity research project"
    )


# ============================================================
# HERO HEADER
# ============================================================

st.html(
    """
    <div style="
        padding:32px;
        border-radius:20px;

        background:
            linear-gradient(
                135deg,
                rgba(20,32,52,0.96),
                rgba(9,18,31,0.96)
            );

        border:1px solid rgba(80,180,255,0.20);

        box-shadow:
            0 15px 45px rgba(0,0,0,0.35);

        margin-bottom:28px;
    ">

        <div style="
            font-size:38px;
            font-weight:800;
            letter-spacing:-1px;
            margin-bottom:10px;
            color:#ffffff;
        ">

            🛡️

            <span style="
                color:#55b6ff;
            ">
                SENTINEL
            </span>

            Threat Detection

        </div>


        <div style="
            color:#91a4bb;
            font-size:16px;
            line-height:1.6;
            margin-bottom:20px;
        ">

            AI-powered security analytics using machine learning
            to classify uploaded feature data.

        </div>


        <div style="
            display:flex;
            gap:12px;
            flex-wrap:wrap;
        ">


            <span style="
                display:inline-block;
                padding:8px 15px;
                border-radius:999px;

                background:
                    rgba(34,197,94,0.12);

                color:#4ade80;

                border:
                    1px solid rgba(34,197,94,0.25);

                font-size:12px;
                font-weight:700;
            ">

                ● SYSTEM ONLINE

            </span>


            <span style="
                display:inline-block;
                padding:8px 15px;
                border-radius:999px;

                background:
                    rgba(59,130,246,0.12);

                color:#60a5fa;

                border:
                    1px solid rgba(59,130,246,0.25);

                font-size:12px;
                font-weight:700;
            ">

                RANDOM FOREST ENGINE

            </span>


        </div>

    </div>
    """
)


# ============================================================
# TOP INFORMATION CARDS
# ============================================================

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Detection Engine",
        "ONLINE"
    )


with col2:

    st.metric(
        "Model",
        "Random Forest"
    )


with col3:

    st.metric(
        "Features",
        len(feature_names)
    )


with col4:

    if metrics:

        st.metric(
            "Accuracy",
            f"{metrics['accuracy'] * 100:.2f}%"
        )

    else:

        st.metric(
            "Accuracy",
            "N/A"
        )


# ============================================================
# MODEL PERFORMANCE
# ============================================================

if metrics:

    st.html(
        """
        <div class="section-title">
            📊 Model Performance
        </div>

        <div class="section-description">
            Performance measured on the project test dataset.
        </div>
        """
    )


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "Accuracy",
            f"{metrics['accuracy'] * 100:.2f}%"
        )


    with col2:

        st.metric(
            "Precision",
            f"{metrics['precision'] * 100:.2f}%"
        )


    with col3:

        st.metric(
            "Recall",
            f"{metrics['recall'] * 100:.2f}%"
        )


    with col4:

        st.metric(
            "F1 Score",
            f"{metrics['f1_score'] * 100:.2f}%"
        )


    st.subheader(
        "Confusion Matrix"
    )


    cm = metrics["confusion_matrix"]


    cm_df = pd.DataFrame(
        cm,
        index=[
            "Actual 0",
            "Actual 1"
        ],
        columns=[
            "Predicted 0",
            "Predicted 1"
        ]
    )


    st.dataframe(
        cm_df,
        use_container_width=True
    )


# ============================================================
# DETECTION CENTER
# ============================================================

st.html(
    """
    <div class="section-title">
        🔎 Detection Center
    </div>

    <div class="section-description">
        Upload a CSV containing the feature set used by the trained model.
    </div>
    """
)


# ============================================================
# UPLOAD CARD
# ============================================================

st.html(
    """
    <div style="
        padding:25px;
        border-radius:18px;

        background:
            linear-gradient(
                145deg,
                rgba(15,29,48,0.92),
                rgba(9,18,31,0.92)
            );

        border:
            1px dashed rgba(83,178,255,0.35);

        margin-bottom:12px;
    ">

        <div style="
            font-size:18px;
            font-weight:700;
            margin-bottom:6px;
        ">

            📁 Upload Security Feature Dataset

        </div>

        <div style="
            color:#8798ac;
            font-size:14px;
        ">

            Supported format: CSV · Numeric feature data

        </div>

    </div>
    """
)


# ============================================================
# FILE UPLOADER
# ============================================================

uploaded_file = st.file_uploader(
    "Choose CSV file",
    type=["csv"]
)


# ============================================================
# PROCESS FILE
# ============================================================

if uploaded_file is not None:

    try:

        # ----------------------------------------------------
        # LOAD DATA
        # ----------------------------------------------------

        data = pd.read_csv(
            uploaded_file
        )


        # ----------------------------------------------------
        # DATASET OVERVIEW
        # ----------------------------------------------------

        st.html(
            """
            <div class="section-title">
                📄 Dataset Overview
            </div>
            """
        )


        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "Rows",
                f"{data.shape[0]:,}"
            )


        with col2:

            st.metric(
                "Columns",
                data.shape[1]
            )


        with col3:

            st.metric(
                "Numeric Features",
                len(
                    data.select_dtypes(
                        include=["number"]
                    ).columns
                )
            )


        # ----------------------------------------------------
        # DATA PREVIEW
        # ----------------------------------------------------

        with st.expander(
            "Preview uploaded data"
        ):

            st.dataframe(
                data.head(10),
                use_container_width=True
            )


        # ----------------------------------------------------
        # REMOVE TARGET COLUMN
        # ----------------------------------------------------

        if "Benign" in data.columns:

            numeric_data = data.drop(
                columns=["Benign"]
            )

        else:

            numeric_data = data.copy()


        # ----------------------------------------------------
        # KEEP NUMERIC FEATURES
        # ----------------------------------------------------

        numeric_data = numeric_data.select_dtypes(
            include=["number"]
        )


        # ----------------------------------------------------
        # FEATURE VALIDATION
        # ----------------------------------------------------

        missing_features = [
            feature
            for feature in feature_names
            if feature not in numeric_data.columns
        ]


        extra_features = [
            feature
            for feature in numeric_data.columns
            if feature not in feature_names
        ]


        # ----------------------------------------------------
        # CHECK MISSING FEATURES
        # ----------------------------------------------------

        if missing_features:

            st.error(
                "❌ Required features are missing."
            )

            st.write(
                "Missing features:"
            )

            st.code(
                "\n".join(
                    missing_features
                )
            )


        else:

            # ------------------------------------------------
            # EXTRA FEATURES
            # ------------------------------------------------

            if extra_features:

                st.warning(
                    f"{len(extra_features)} extra feature(s) "
                    "detected. They will be ignored."
                )


            # ------------------------------------------------
            # CORRECT FEATURE ORDER
            # ------------------------------------------------

            numeric_data = numeric_data[
                feature_names
            ]


            # ------------------------------------------------
            # PREDICTION
            # ------------------------------------------------

            predictions = model.predict(
                numeric_data
            )


            probabilities = model.predict_proba(
                numeric_data
            )


            # ------------------------------------------------
            # RESULTS
            # ------------------------------------------------

            results = data.copy()


            results["Prediction"] = predictions


            results["Confidence"] = (
                probabilities.max(axis=1) * 100
            ).round(2)


            results["Result"] = results[
                "Prediction"
            ].apply(
                lambda x:
                "BENIGN"
                if x == 1
                else "MALICIOUS"
            )


            # ------------------------------------------------
            # COUNTS
            # ------------------------------------------------

            benign_count = int(
                (predictions == 1).sum()
            )


            malicious_count = int(
                (predictions == 0).sum()
            )


            total_count = len(
                predictions
            )


            # =================================================
            # DETECTION OVERVIEW
            # =================================================

            st.html(
                """
                <div class="section-title">
                    🚨 Detection Overview
                </div>
                """
            )


            col1, col2, col3 = st.columns(3)


            with col1:

                st.html(
                    f"""
                    <div style="
                        padding:22px;
                        border-radius:16px;
                        background:#0d1522;
                        border:1px solid rgba(255,255,255,0.07);
                        text-align:center;
                    ">

                        <div style="
                            color:#8294aa;
                            font-size:13px;
                        ">
                            TOTAL ANALYZED
                        </div>

                        <div style="
                            color:#60a5fa;
                            font-size:32px;
                            font-weight:800;
                            margin-top:8px;
                        ">
                            {total_count:,}
                        </div>

                    </div>
                    """
                )


            with col2:

                st.html(
                    f"""
                    <div style="
                        padding:22px;
                        border-radius:16px;
                        background:#0d1522;
                        border:1px solid rgba(255,255,255,0.07);
                        text-align:center;
                    ">

                        <div style="
                            color:#8294aa;
                            font-size:13px;
                        ">
                            BENIGN SAMPLES
                        </div>

                        <div style="
                            color:#4ade80;
                            font-size:32px;
                            font-weight:800;
                            margin-top:8px;
                        ">
                            {benign_count:,}
                        </div>

                    </div>
                    """
                )


            with col3:

                st.html(
                    f"""
                    <div style="
                        padding:22px;
                        border-radius:16px;
                        background:#0d1522;
                        border:1px solid rgba(255,255,255,0.07);
                        text-align:center;
                    ">

                        <div style="
                            color:#8294aa;
                            font-size:13px;
                        ">
                            MALICIOUS SAMPLES
                        </div>

                        <div style="
                            color:#fb7185;
                            font-size:32px;
                            font-weight:800;
                            margin-top:8px;
                        ">
                            {malicious_count:,}
                        </div>

                    </div>
                    """
                )


            # =================================================
            # CLASSIFICATION RESULTS
            # =================================================

            st.html(
                """
                <div class="section-title">
                    🔬 Classification Results
                </div>
                """
            )


            with st.expander(
                "View detailed detection results",
                expanded=True
            ):

                st.dataframe(
                    results,
                    use_container_width=True,
                    height=420
                )


            # =================================================
            # DOWNLOAD REPORT
            # =================================================

            csv_data = results.to_csv(
                index=False
            )


            st.download_button(
                label="⬇️ Download Detection Report",
                data=csv_data,
                file_name="detection_results.csv",
                mime="text/csv"
            )


            # =================================================
            # FEATURE IMPORTANCE
            # =================================================

            st.html(
                """
                <div class="section-title">
                    🧠 Feature Intelligence
                </div>

                <div class="section-description">
                    Top features used by the Random Forest model.
                </div>
                """
            )


            importance_df = pd.DataFrame(
                {
                    "Feature": feature_names,
                    "Importance": model.feature_importances_
                }
            )


            importance_df = (
                importance_df
                .sort_values(
                    "Importance",
                    ascending=False
                )
                .head(10)
            )


            st.bar_chart(
                importance_df.set_index(
                    "Feature"
                )
            )


            # =================================================
            # PREDICTION CONFIDENCE
            # =================================================

            st.html(
                """
                <div class="section-title">
                    🎯 Prediction Confidence
                </div>
                """
            )


            average_confidence = (
                probabilities.max(axis=1).mean()
                * 100
            )


            st.progress(
                int(
                    min(
                        average_confidence,
                        100
                    )
                )
            )


            st.write(
                f"Average prediction confidence: "
                f"**{average_confidence:.2f}%**"
            )


    except Exception as e:

        st.error(
            f"❌ Error processing file: {e}"
        )


# ============================================================
# FOOTER
# ============================================================

st.html(
    """
    <div style="
        text-align:center;
        color:#53657b;
        font-size:12px;
        padding:35px 0 10px 0;
    ">

        SENTINEL · AI Threat Detection Platform

        <br>

        Defensive cybersecurity research project

    </div>
    """
)