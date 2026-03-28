
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import io
from datetime import datetime

st.set_page_config(
    page_title="AI-Assisted Data Wrangler & Visualizer",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# PREMIUM UI STYLE - PASTEL GREEN
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600;700&display=swap');

:root {
    --bg-1: #EEF4E8;
    --bg-2: #E3ECD9;
    --bg-3: #DCE8CF;
    --card: rgba(248, 251, 244, 0.92);
    --card-strong: #F7FBF2;
    --sage: #A9C09A;
    --sage-2: #BFD3AF;
    --sage-soft: #DDE9D2;
    --olive: #6F875A;
    --olive-dark: #4F6840;
    --olive-deep: #3F5632;
    --text: #30402B;
    --muted: #5F6F57;
    --border: #C9D7BF;
    --shadow: 0 10px 30px rgba(69, 92, 56, 0.08);
    --radius-xl: 30px;
    --radius-lg: 22px;
    --radius-md: 16px;
}

html, body, [class*="css"]  {
    font-family: 'Inter', sans-serif;
    color: var(--text);
}

.stApp {
    background:
        radial-gradient(circle at top left, rgba(201, 221, 188, 0.9) 0%, rgba(201, 221, 188, 0.0) 30%),
        radial-gradient(circle at bottom right, rgba(186, 210, 171, 0.55) 0%, rgba(186, 210, 171, 0.0) 28%),
        linear-gradient(180deg, var(--bg-1) 0%, var(--bg-2) 55%, var(--bg-3) 100%);
}

.block-container {
    padding-top: 2.2rem;
    padding-bottom: 2rem;
    max-width: 1250px;
}

section[data-testid="stSidebar"] {
    background: rgba(244, 249, 239, 0.97);
    border-right: 1px solid var(--border);
}

section[data-testid="stSidebar"] .block-container {
    padding-top: 1.8rem;
}

h1, h2, h3 {
    color: var(--olive-deep);
    letter-spacing: -0.02em;
    margin-bottom: 0.4rem;
}

h1 {
    font-family: 'Playfair Display', serif !important;
    font-size: 3.2rem !important;
    font-weight: 700 !important;
    line-height: 1.05 !important;
}

h2 {
    font-size: 1.65rem !important;
    font-weight: 700 !important;
}

h3 {
    font-size: 1.2rem !important;
    font-weight: 700 !important;
}

p, label, .stMarkdown, .stText, .stCaption {
    color: var(--muted);
}

.hero-kicker {
    display: inline-block;
    padding: 0.38rem 0.9rem;
    border-radius: 999px;
    background: var(--sage-soft);
    color: var(--olive-dark);
    font-size: 0.82rem;
    font-weight: 700;
    letter-spacing: 0.03em;
    margin-bottom: 0.9rem;
}

.soft-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: var(--radius-xl);
    padding: 1.35rem 1.4rem;
    box-shadow: var(--shadow);
    backdrop-filter: blur(4px);
}

.soft-card-tight {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 1rem 1.1rem;
    box-shadow: var(--shadow);
}

.section-title {
    font-size: 1.18rem;
    font-weight: 700;
    color: var(--olive-deep);
    margin-bottom: 0.35rem;
}

.section-note {
    color: var(--muted);
    font-size: 0.96rem;
    line-height: 1.65;
}

.feature-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
    margin-top: 0.8rem;
}

.feature-card {
    background: rgba(247, 251, 242, 0.88);
    border: 1px solid var(--border);
    border-radius: 22px;
    padding: 1rem 1rem;
}

.feature-card-title {
    color: var(--olive-dark);
    font-weight: 700;
    margin-bottom: 0.28rem;
}

.feature-card-text {
    color: var(--muted);
    font-size: 0.92rem;
    line-height: 1.55;
}

div[data-testid="stFileUploader"] {
    background: rgba(247, 251, 242, 0.85);
    border: 1.6px dashed var(--sage);
    border-radius: 24px;
    padding: 0.8rem;
}

div[data-testid="stMetric"] {
    background: var(--card-strong);
    border: 1px solid var(--border);
    border-radius: 24px;
    padding: 0.85rem 1rem;
    box-shadow: 0 8px 22px rgba(77, 88, 57, 0.06);
}

div[data-testid="stMetric"] label {
    color: var(--muted) !important;
    font-weight: 600;
}

div[data-testid="stMetricValue"] {
    color: var(--olive-deep) !important;
    font-weight: 700 !important;
}

.stButton > button,
.stDownloadButton > button {
    background: linear-gradient(180deg, #6F875A 0%, #587045 100%);
    color: #FFFFFF !important;
    border: none;
    border-radius: 999px;
    padding: 0.72rem 1.3rem;
    font-weight: 700;
    box-shadow: 0 10px 20px rgba(111, 126, 79, 0.2);
    transition: all 0.18s ease;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    transform: translateY(-1px);
    filter: brightness(1.03);
    color: #FFFFFF !important;
}

.stButton > button p,
.stDownloadButton > button p,
.stButton > button span,
.stDownloadButton > button span {
    color: #FFFFFF !important;
}

.stTextInput input,
.stTextArea textarea,
.stSelectbox div[data-baseweb="select"] > div,
.stMultiSelect div[data-baseweb="select"] > div,
.stNumberInput input {
    background: rgba(255,255,255,0.82) !important;
    border: 1px solid var(--border) !important;
    border-radius: 18px !important;
    color: var(--text) !important;
}

div[data-baseweb="tag"] {
    background: var(--sage-soft) !important;
    color: var(--olive-dark) !important;
    border-radius: 999px !important;
    border: none !important;
}

div[data-testid="stDataFrame"] {
    background: var(--card-strong);
    border: 1px solid var(--border);
    border-radius: 24px;
    padding: 0.45rem;
    box-shadow: 0 6px 18px rgba(77, 88, 57, 0.05);
}

[data-testid="stExpander"] {
    background: rgba(247, 251, 242, 0.75);
    border: 1px solid var(--border);
    border-radius: 22px;
}

.streamlit-expanderHeader {
    color: var(--olive-deep) !important;
    font-weight: 700 !important;
}

hr {
    border: none;
    height: 1px;
    background: var(--border);
    margin: 1.7rem 0;
}

.sidebar-caption {
    color: var(--muted);
    font-size: 0.92rem;
    line-height: 1.55;
    margin-top: -0.25rem;
    margin-bottom: 0.75rem;
}

.mini-divider {
    height: 1px;
    background: var(--border);
    margin: 1rem 0 1.2rem 0;
    border: none;
}

div[role="radiogroup"] label {
    color: var(--olive-deep) !important;
}

div[data-testid="stAlert"] {
    border-radius: 20px;
}

@media (max-width: 900px) {
    .feature-grid {
        grid-template-columns: 1fr;
    }
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HELPER UI FUNCTIONS
# -----------------------------
def render_hero():
    st.markdown('<div class="hero-kicker">Data Preparation Studio</div>', unsafe_allow_html=True)
    st.title("AI-Assisted Data Wrangler & Visualizer")
    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

def render_feature_cards():
    st.markdown("""
    <div class="feature-grid">
        <div class="feature-card">
            <div class="feature-card-title">Clean with control</div>
            <div class="feature-card-text">Treat missing values, duplicates, outliers, and category inconsistencies with guided actions.</div>
        </div>
        <div class="feature-card">
            <div class="feature-card-title">Transform with clarity</div>
            <div class="feature-card-text">Rename, scale, parse, bin, and create new columns while keeping a clear workflow history.</div>
        </div>
        <div class="feature-card">
            <div class="feature-card-title">Explore visually</div>
            <div class="feature-card-text">Build cleaner charts with filters, comparisons, and export-ready outputs in one place.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def section_card(title, note):
    st.markdown(
        f"""
        <div class="soft-card">
            <div class="section-title">{title}</div>
            <div class="section-note">{note}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

def compact_section_card(title, note):
    st.markdown(
        f"""
        <div class="soft-card-tight">
            <div class="section-title">{title}</div>
            <div class="section-note">{note}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# -----------------------------
# BACKEND HELPERS
# -----------------------------
@st.cache_data
def load_data(file_bytes, file_name):
    buffer = io.BytesIO(file_bytes)
    if file_name.endswith(".csv"):
        return pd.read_csv(buffer)
    elif file_name.endswith(".xlsx"):
        return pd.read_excel(buffer)
    elif file_name.endswith(".json"):
        return pd.read_json(buffer)
    else:
        raise ValueError("Unsupported file format")

def init_state():
    defaults = {
        "df": None,
        "original_df": None,
        "history": [],
        "log": [],
        "violations": pd.DataFrame()
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

def push_history():
    if st.session_state.df is not None:
        st.session_state.history.append(st.session_state.df.copy())

def add_log(step, params=None, affected_columns=None):
    st.session_state.log.append({
        "step": step,
        "params": params or {},
        "affected_columns": affected_columns or [],
        "timestamp": str(datetime.now())
    })

def reset_all():
    if st.session_state.original_df is not None:
        st.session_state.df = st.session_state.original_df.copy()
        st.session_state.history = []
        st.session_state.log = []
        st.session_state.violations = pd.DataFrame()

def missing_summary(df):
    ms = pd.DataFrame({
        "missing_count": df.isna().sum(),
        "missing_percent": (df.isna().mean() * 100).round(2)
    })
    return ms

def before_after_stats(before, after, cols):
    rows = []
    for c in cols:
        if c in before.columns and c in after.columns:
            rows.append({
                "column": c,
                "before_missing": int(before[c].isna().sum()),
                "after_missing": int(after[c].isna().sum()),
                "before_dtype": str(before[c].dtype),
                "after_dtype": str(after[c].dtype)
            })
    return pd.DataFrame(rows)

def safe_numeric_clean(series):
    return pd.to_numeric(
        series.astype(str)
        .str.replace(",", "", regex=False)
        .str.replace("$", "", regex=False)
        .str.replace("€", "", regex=False)
        .str.replace("£", "", regex=False)
        .str.strip(),
        errors="coerce"
    )

def export_excel_bytes(df):
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="clean_data")
    return output.getvalue()

def aggregate_for_bar(df, x, y, agg):
    if agg == "mean":
        return df.groupby(x, dropna=False)[y].mean().sort_values(ascending=False)
    elif agg == "sum":
        return df.groupby(x, dropna=False)[y].sum().sort_values(ascending=False)
    elif agg == "median":
        return df.groupby(x, dropna=False)[y].median().sort_values(ascending=False)
    else:
        return df.groupby(x, dropna=False)[y].count().sort_values(ascending=False)

# -----------------------------
# INIT
# -----------------------------
init_state()

# -----------------------------
# HEADER
# -----------------------------
render_hero()
render_feature_cards()
st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.markdown("## Workspace")
st.sidebar.markdown(
    '<div class="sidebar-caption">Move through each step of the data preparation journey in a clean, guided flow.</div>',
    unsafe_allow_html=True
)
st.sidebar.markdown('<hr class="mini-divider">', unsafe_allow_html=True)

menu = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "Cleaning Studio",
        "Transformations",
        "Validation",
        "Visualization",
        "Insights",
        "Export"
    ]
)

st.sidebar.markdown('<hr class="mini-divider">', unsafe_allow_html=True)
st.sidebar.markdown("## Session Controls")
st.sidebar.markdown(
    '<div class="sidebar-caption">Manage your current workflow safely with reset and undo actions.</div>',
    unsafe_allow_html=True
)

with st.sidebar:
    if st.button("Reset session"):
        st.session_state.df = None
        st.session_state.original_df = None
        st.session_state.history = []
        st.session_state.log = []
        st.session_state.violations = pd.DataFrame()
        st.success("Session reset")

    if st.button("Undo last step"):
        if len(st.session_state.history) > 0:
            st.session_state.df = st.session_state.history.pop()
            st.success("Last step undone")
        else:
            st.info("Nothing to undo")

    if st.button("Reset to original dataset"):
        reset_all()
        st.success("Dataset reset to original")

# -----------------------------
# PAGE 1 – OVERVIEW
# -----------------------------
if menu == "Overview":
    section_card(
        "Upload Dataset",
        "Import your CSV, Excel, or JSON file and begin working in a softer, more intuitive data preparation space."
    )
    st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

    file = st.file_uploader("Upload CSV, Excel, or JSON", type=["csv", "xlsx", "json"])
    st.caption("Supported formats: CSV, XLSX, JSON • Recommended for mixed-type datasets with missing values.")

    if file is not None:
        file_bytes = file.read()
        try:
            df = load_data(file_bytes, file.name)
            st.session_state.df = df.copy()
            st.session_state.original_df = df.copy()
            st.session_state.history = []
            st.session_state.log = []
            st.session_state.violations = pd.DataFrame()
            add_log("dataset_uploaded", {"filename": file.name}, list(df.columns))
            st.success("Dataset uploaded successfully")
        except Exception as e:
            st.error(f"Failed to load file: {e}")

    if st.session_state.df is not None:
        df = st.session_state.df

        compact_section_card(
            "Dataset Overview",
            "Review structure, data types, missing values, duplicates, and summary statistics before making any changes."
        )
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total Rows", df.shape[0])
        c2.metric("Total Columns", df.shape[1])
        c3.metric("Missing Cells", int(df.isna().sum().sum()))
        c4.metric("Duplicate Records", int(df.duplicated().sum()))

        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

        st.subheader("Preview")
        st.dataframe(df.head(10), use_container_width=True)

        st.subheader("Columns and Data Types")
        dtype_df = pd.DataFrame({
            "column": df.columns,
            "dtype": [str(d) for d in df.dtypes]
        })
        st.dataframe(dtype_df, use_container_width=True)

        st.subheader("Missing Values by Column")
        st.dataframe(missing_summary(df), use_container_width=True)

        with st.expander("View detailed numeric summary statistics"):
            num_df = df.select_dtypes(include=np.number)
            if not num_df.empty:
                st.dataframe(num_df.describe().T, use_container_width=True)
            else:
                st.info("No numeric columns are available in the current dataset.")

        with st.expander("View detailed categorical summary statistics"):
            cat_df = df.select_dtypes(exclude=np.number)
            if not cat_df.empty:
                try:
                    st.dataframe(cat_df.describe(include="all").T, use_container_width=True)
                except Exception:
                    st.write("Categorical summary could not be generated.")
            else:
                st.info("No categorical columns are available at the moment.")

# -----------------------------
# PAGE 2 – CLEANING STUDIO
# -----------------------------
elif menu == "Cleaning Studio":
    df = st.session_state.df

    if df is None:
        st.warning("Please upload a dataset to begin.")
    else:
        section_card(
            "Cleaning Studio",
            "Refine your dataset with guided actions for missing values, duplicates, category consistency, and numeric quality."
        )
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

        compact_section_card(
            "Missing Values",
            "Choose how you want to treat null values and preview the impact before continuing."
        )
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
        st.dataframe(missing_summary(df), use_container_width=True)

        with st.expander("Handle missing values", expanded=True):
            mv_action = st.selectbox(
                "Action",
                [
                    "Drop rows with nulls in selected columns",
                    "Drop columns above missing threshold",
                    "Fill with constant",
                    "Fill numeric with mean",
                    "Fill numeric with median",
                    "Fill with mode",
                    "Fill categorical with most frequent",
                    "Forward fill",
                    "Backward fill"
                ]
            )

            selected_cols = st.multiselect(
                "Select columns",
                list(df.columns),
                default=list(df.columns[:1]) if len(df.columns) else []
            )
            threshold = st.slider("Missing threshold %", 0, 100, 50)
            constant_value = st.text_input("Constant value", value="Unknown")

            if st.button("Apply treatment"):
                try:
                    before = df.copy()
                    push_history()

                    if mv_action == "Drop rows with nulls in selected columns":
                        if not selected_cols:
                            st.error("Select at least one column.")
                        else:
                            df = df.dropna(subset=selected_cols)

                    elif mv_action == "Drop columns above missing threshold":
                        cols_to_drop = [c for c in df.columns if df[c].isna().mean() * 100 > threshold]
                        df = df.drop(columns=cols_to_drop)

                    elif mv_action == "Fill with constant":
                        if not selected_cols:
                            st.error("Select columns.")
                        else:
                            for c in selected_cols:
                                df[c] = df[c].fillna(constant_value)

                    elif mv_action == "Fill numeric with mean":
                        for c in selected_cols:
                            if pd.api.types.is_numeric_dtype(df[c]):
                                df[c] = df[c].fillna(df[c].mean())

                    elif mv_action == "Fill numeric with median":
                        for c in selected_cols:
                            if pd.api.types.is_numeric_dtype(df[c]):
                                df[c] = df[c].fillna(df[c].median())

                    elif mv_action == "Fill with mode":
                        for c in selected_cols:
                            mode_val = df[c].mode(dropna=True)
                            if not mode_val.empty:
                                df[c] = df[c].fillna(mode_val.iloc[0])

                    elif mv_action == "Fill categorical with most frequent":
                        for c in selected_cols:
                            if not pd.api.types.is_numeric_dtype(df[c]):
                                mode_val = df[c].mode(dropna=True)
                                if not mode_val.empty:
                                    df[c] = df[c].fillna(mode_val.iloc[0])

                    elif mv_action == "Forward fill":
                        if selected_cols:
                            df[selected_cols] = df[selected_cols].ffill()

                    elif mv_action == "Backward fill":
                        if selected_cols:
                            df[selected_cols] = df[selected_cols].bfill()

                    st.session_state.df = df
                    add_log("missing_value_action", {
                        "action": mv_action,
                        "threshold": threshold,
                        "constant_value": constant_value
                    }, selected_cols)

                    st.success("Missing value operation applied.")
                    st.write("Before / After preview")
                    st.dataframe(before_after_stats(before, df, [c for c in selected_cols if c in df.columns]), use_container_width=True)
                    st.write(f"Row count before: {len(before)} | after: {len(df)}")

                except Exception as e:
                    st.error(f"Missing value operation failed: {e}")

        st.markdown("<div style='height:14px;'></div>", unsafe_allow_html=True)
        compact_section_card(
            "Duplicates",
            "Identify repeated records by full row or selected keys, then remove them with control."
        )
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

        with st.expander("Detect and remove duplicates", expanded=False):
            dup_subset = st.multiselect("Columns to check duplicates by subset", list(df.columns))
            keep_option = st.selectbox("Keep", ["first", "last"])
            subset_arg = dup_subset if dup_subset else None

            dup_groups = df[df.duplicated(subset=subset_arg, keep=False)]
            st.write("Duplicate rows found:", int(dup_groups.shape[0]))
            if not dup_groups.empty:
                st.dataframe(dup_groups.head(30), use_container_width=True)

            if st.button("Remove duplicates"):
                try:
                    push_history()
                    before_rows = len(df)
                    df = df.drop_duplicates(subset=subset_arg, keep=keep_option)
                    st.session_state.df = df
                    add_log("remove_duplicates", {"keep": keep_option}, dup_subset)
                    st.success(f"Removed {before_rows - len(df)} duplicate rows.")
                except Exception as e:
                    st.error(f"Duplicate removal failed: {e}")

        st.markdown("<div style='height:14px;'></div>", unsafe_allow_html=True)
        compact_section_card(
            "Categorical Data Tools",
            "Standardize labels, apply mappings, group rare categories, or expand them into encoded features."
        )
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

        cat_cols = list(df.select_dtypes(include=["object", "category"]).columns)
        if cat_cols:
            cat_col = st.selectbox("Categorical column", cat_cols)

            cat_action = st.selectbox(
                "Categorical action",
                [
                    "Trim whitespace",
                    "Lower case",
                    "Title case",
                    "Apply mapping dictionary",
                    "Group rare categories into Other",
                    "One-hot encode column"
                ]
            )

            mapping_text = st.text_area(
                "Mapping dictionary as JSON (example: {\"ny\":\"New York\",\"la\":\"Los Angeles\"})",
                value='{}'
            )
            rare_threshold = st.number_input("Rare category frequency threshold", min_value=1, value=5, step=1)

            if st.button("Apply category update"):
                try:
                    push_history()

                    if cat_action == "Trim whitespace":
                        df[cat_col] = df[cat_col].astype(str).str.strip()

                    elif cat_action == "Lower case":
                        df[cat_col] = df[cat_col].astype(str).str.lower()

                    elif cat_action == "Title case":
                        df[cat_col] = df[cat_col].astype(str).str.title()

                    elif cat_action == "Apply mapping dictionary":
                        mapping = json.loads(mapping_text)
                        df[cat_col] = df[cat_col].replace(mapping)

                    elif cat_action == "Group rare categories into Other":
                        freq = df[cat_col].value_counts(dropna=False)
                        rare_vals = freq[freq < rare_threshold].index
                        df[cat_col] = df[cat_col].apply(lambda x: "Other" if x in rare_vals else x)

                    elif cat_action == "One-hot encode column":
                        dummies = pd.get_dummies(df[cat_col], prefix=cat_col, dummy_na=False)
                        df = pd.concat([df.drop(columns=[cat_col]), dummies], axis=1)

                    st.session_state.df = df
                    add_log("categorical_action", {"action": cat_action}, [cat_col])
                    st.success("Categorical transformation applied.")
                except Exception as e:
                    st.error(f"Categorical action failed: {e}")
        else:
            st.info("No categorical columns are available at the moment.")

        st.markdown("<div style='height:14px;'></div>", unsafe_allow_html=True)
        compact_section_card(
            "Numeric Cleaning",
            "Inspect unusual values and decide whether to keep, remove, or cap them safely."
        )
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

        numeric_cols = list(df.select_dtypes(include=np.number).columns)
        if numeric_cols:
            out_col = st.selectbox("Numeric column for outlier check", numeric_cols)
            out_action = st.selectbox("Outlier action", ["Do nothing", "Remove outlier rows", "Cap/Winsorize at quantiles"])
            lower_q = st.slider("Lower quantile", 0.00, 0.20, 0.01, 0.01)
            upper_q = st.slider("Upper quantile", 0.80, 1.00, 0.99, 0.01)

            q1 = df[out_col].quantile(0.25)
            q3 = df[out_col].quantile(0.75)
            iqr = q3 - q1
            low = q1 - 1.5 * iqr
            high = q3 + 1.5 * iqr
            outlier_mask = (df[out_col] < low) | (df[out_col] > high)
            st.write(f"Detected outliers in {out_col}: {int(outlier_mask.sum())}")

            if st.button("Apply numeric treatment"):
                try:
                    push_history()
                    before_rows = len(df)

                    if out_action == "Remove outlier rows":
                        df = df[~outlier_mask].copy()

                    elif out_action == "Cap/Winsorize at quantiles":
                        lo = df[out_col].quantile(lower_q)
                        hi = df[out_col].quantile(upper_q)
                        df[out_col] = df[out_col].clip(lower=lo, upper=hi)

                    st.session_state.df = df
                    add_log("outlier_action", {
                        "action": out_action,
                        "lower_quantile": lower_q,
                        "upper_quantile": upper_q
                    }, [out_col])

                    st.success("Outlier action applied.")
                    st.write(f"Rows before: {before_rows} | after: {len(df)}")
                except Exception as e:
                    st.error(f"Outlier action failed: {e}")
        else:
            st.info("No numeric columns are available in the current dataset.")

# -----------------------------
# PAGE 3 – TRANSFORMATIONS
# -----------------------------
elif menu == "Transformations":
    df = st.session_state.df

    if df is None:
        st.warning("Please upload a dataset to begin.")
    else:
        section_card(
            "Transformations",
            "Reshape and enrich your data through parsing, scaling, renaming, calculated fields, and binning."
        )
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

        compact_section_card(
            "Data Types & Parsing",
            "Convert columns into cleaner numeric, categorical, string, or datetime formats."
        )
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

        col_type = st.selectbox("Column to convert", list(df.columns))
        target_type = st.selectbox("Convert to", ["numeric", "string", "category", "datetime"])
        dt_format = st.text_input("Datetime format (optional)", value="")

        if st.button("Apply type conversion"):
            try:
                push_history()

                if target_type == "numeric":
                    df[col_type] = safe_numeric_clean(df[col_type])
                elif target_type == "string":
                    df[col_type] = df[col_type].astype("string")
                elif target_type == "category":
                    df[col_type] = df[col_type].astype("category")
                elif target_type == "datetime":
                    if dt_format.strip():
                        df[col_type] = pd.to_datetime(df[col_type], format=dt_format, errors="coerce")
                    else:
                        df[col_type] = pd.to_datetime(df[col_type], errors="coerce")

                st.session_state.df = df
                add_log("convert_type", {"target_type": target_type, "datetime_format": dt_format}, [col_type])
                st.success("Type conversion successful.")
            except Exception as e:
                st.error(f"The conversion step could not be completed: {e}")

        st.markdown("<div style='height:14px;'></div>", unsafe_allow_html=True)
        compact_section_card(
            "Normalization & Scaling",
            "Standardize numeric columns for cleaner comparison and downstream analysis."
        )
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

        num_cols = list(df.select_dtypes(include=np.number).columns)
        if num_cols:
            scale_cols = st.multiselect("Columns for scaling", num_cols)
            scale_method = st.selectbox("Scaling method", ["Min-Max", "Z-score"])

            if st.button("Apply scaling method"):
                if not scale_cols:
                    st.error("Select at least one numeric column.")
                else:
                    try:
                        push_history()
                        before = df[scale_cols].describe().T.copy()

                        for c in scale_cols:
                            if scale_method == "Min-Max":
                                denom = df[c].max() - df[c].min()
                                if denom != 0:
                                    df[c] = (df[c] - df[c].min()) / denom
                            else:
                                std = df[c].std()
                                if std != 0:
                                    df[c] = (df[c] - df[c].mean()) / std

                        after = df[scale_cols].describe().T.copy()
                        st.session_state.df = df
                        add_log("scaling", {"method": scale_method}, scale_cols)
                        st.success("Scaling applied.")
                        st.write("Before stats")
                        st.dataframe(before, use_container_width=True)
                        st.write("After stats")
                        st.dataframe(after, use_container_width=True)
                    except Exception as e:
                        st.error(f"The scaling step could not be completed: {e}")
        else:
            st.info("No numeric columns are available in the current dataset.")

        st.markdown("<div style='height:14px;'></div>", unsafe_allow_html=True)
        compact_section_card(
            "Column Operations",
            "Rename, remove, derive, and group columns to create a more analysis-ready structure."
        )
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

        rename_col = st.selectbox("Column to rename", list(df.columns))
        new_name = st.text_input("New column name")
        if st.button("Rename selected column"):
            if not new_name.strip():
                st.error("Enter a new column name.")
            elif new_name in df.columns:
                st.error("Column name already exists.")
            else:
                push_history()
                df = df.rename(columns={rename_col: new_name})
                st.session_state.df = df
                add_log("rename_column", {"new_name": new_name}, [rename_col])
                st.success("Column renamed.")

        drop_cols = st.multiselect("Columns to drop", list(df.columns))
        if st.button("Remove selected columns"):
            if not drop_cols:
                st.error("Select at least one column.")
            else:
                push_history()
                df = df.drop(columns=drop_cols)
                st.session_state.df = df
                add_log("drop_columns", {}, drop_cols)
                st.success("Columns dropped.")

        st.subheader("Create New Column with Formula")
        new_formula_col = st.text_input("New calculated column name", value="new_feature")
        st.caption("Use column names directly, for example: price / quantity or np.log(sales + 1)")
        formula = st.text_input("Formula")

        if st.button("Create calculated feature"):
            try:
                if not formula.strip():
                    st.error("Enter a formula.")
                else:
                    push_history()
                    local_dict = {c: df[c] for c in df.columns}
                    local_dict["np"] = np
                    local_dict["pd"] = pd
                    df[new_formula_col] = eval(formula, {"__builtins__": {}}, local_dict)
                    st.session_state.df = df
                    add_log("create_formula_column", {"formula": formula}, [new_formula_col])
                    st.success("Calculated column created.")
            except Exception as e:
                st.error(f"Formula failed: {e}")

        st.subheader("Binning")
        bin_cols = list(df.select_dtypes(include=np.number).columns)
        if bin_cols:
            bin_col = st.selectbox("Numeric column to bin", bin_cols)
            bin_method = st.selectbox("Binning method", ["Equal-width", "Quantile"])
            bins = st.slider("Number of bins", 2, 10, 4)
            bin_new_col = st.text_input("Binned column name", value=f"{bin_col}_binned")

            if st.button("Create binned column"):
                try:
                    push_history()
                    if bin_method == "Equal-width":
                        df[bin_new_col] = pd.cut(df[bin_col], bins=bins)
                    else:
                        df[bin_new_col] = pd.qcut(df[bin_col], q=bins, duplicates="drop")
                    st.session_state.df = df
                    add_log("binning", {"method": bin_method, "bins": bins}, [bin_col, bin_new_col])
                    st.success("Binning applied.")
                except Exception as e:
                    st.error(f"Binning failed: {e}")

# -----------------------------
# PAGE 4 – VALIDATION
# -----------------------------
elif menu == "Validation":
    df = st.session_state.df

    if df is None:
        st.warning("Please upload a dataset to begin.")
    else:
        section_card(
            "Validation Rules",
            "Check your dataset against simple quality rules and review any records that violate them."
        )
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

        rule_type = st.selectbox(
            "Validation rule",
            ["Numeric range check", "Allowed categories list", "Non-null constraint"]
        )

        violations = pd.DataFrame()

        if rule_type == "Numeric range check":
            num_cols = list(df.select_dtypes(include=np.number).columns)
            if num_cols:
                col = st.selectbox("Numeric column", num_cols)
                min_val = st.number_input("Minimum allowed value", value=float(df[col].min()) if not df[col].dropna().empty else 0.0)
                max_val = st.number_input("Maximum allowed value", value=float(df[col].max()) if not df[col].dropna().empty else 0.0)

                if st.button("Check numeric rules"):
                    violations = df[(df[col] < min_val) | (df[col] > max_val)].copy()
                    if not violations.empty:
                        violations["violation_reason"] = f"{col} outside [{min_val}, {max_val}]"
                    st.session_state.violations = violations
                    st.success(f"Found {len(violations)} violations.")
            else:
                st.info("No numeric columns are available in the current dataset.")

        elif rule_type == "Allowed categories list":
            cat_cols = list(df.select_dtypes(include=["object", "category"]).columns)
            if cat_cols:
                col = st.selectbox("Categorical column", cat_cols)
                allowed_text = st.text_input("Allowed values (comma-separated)", value="A,B,C")

                if st.button("Check allowed categories"):
                    allowed = [x.strip() for x in allowed_text.split(",") if x.strip()]
                    violations = df[~df[col].isin(allowed)].copy()
                    if not violations.empty:
                        violations["violation_reason"] = f"{col} not in allowed list"
                    st.session_state.violations = violations
                    st.success(f"Found {len(violations)} violations.")
            else:
                st.info("No categorical columns are available at the moment.")

        elif rule_type == "Non-null constraint":
            cols = st.multiselect("Columns that must not be null", list(df.columns))
            if st.button("Check required fields"):
                if not cols:
                    st.error("Select at least one column.")
                else:
                    violations = df[df[cols].isna().any(axis=1)].copy()
                    if not violations.empty:
                        violations["violation_reason"] = f"Null detected in required columns: {', '.join(cols)}"
                    st.session_state.violations = violations
                    st.success(f"Found {len(violations)} violations.")

        st.subheader("Violations Table")
        if isinstance(st.session_state.violations, pd.DataFrame) and not st.session_state.violations.empty:
            st.dataframe(st.session_state.violations, use_container_width=True)
        else:
            st.info("No validation issues are currently available to display.")

# -----------------------------
# PAGE 5 – VISUALIZATION
# -----------------------------
elif menu == "Visualization":
    df = st.session_state.df

    if df is None:
        st.warning("Please upload a dataset to begin.")
    else:
        section_card(
            "Visualization Builder",
            "Create cleaner, more readable charts with filters, aggregation, and visual exploration controls."
        )
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

        viz_df = df.copy()

        st.subheader("Filters")
        filter_cat_cols = list(viz_df.select_dtypes(include=["object", "category"]).columns)
        if filter_cat_cols:
            fcat = st.selectbox("Filter by category column (optional)", ["None"] + filter_cat_cols)
            if fcat != "None":
                options = list(viz_df[fcat].dropna().astype(str).unique())
                selected_vals = st.multiselect("Select category values", options, default=options[:min(5, len(options))])
                if selected_vals:
                    viz_df = viz_df[viz_df[fcat].astype(str).isin(selected_vals)]

        filter_num_cols = list(viz_df.select_dtypes(include=np.number).columns)
        if filter_num_cols:
            fnum = st.selectbox("Filter by numeric range (optional)", ["None"] + filter_num_cols)
            if fnum != "None" and not viz_df[fnum].dropna().empty:
                lo = float(viz_df[fnum].min())
                hi = float(viz_df[fnum].max())
                selected_range = st.slider("Numeric range", min_value=lo, max_value=hi, value=(lo, hi))
                viz_df = viz_df[(viz_df[fnum] >= selected_range[0]) & (viz_df[fnum] <= selected_range[1])]

        chart = st.selectbox(
            "Chart type",
            ["Histogram", "Box Plot", "Scatter Plot", "Line Chart", "Bar Chart", "Correlation Heatmap"]
        )

        fig, ax = plt.subplots(figsize=(8, 5))

        try:
            if chart == "Histogram":
                num_cols = list(viz_df.select_dtypes(include=np.number).columns)
                if num_cols:
                    col = st.selectbox("Numeric column", num_cols)
                    bins = st.slider("Bins", 5, 50, 20)
                    ax.hist(viz_df[col].dropna(), bins=bins)
                    ax.set_title(f"Histogram of {col}")
                    ax.set_xlabel(col)
                    ax.set_ylabel("Frequency")
                else:
                    st.info("No numeric columns are available in the current dataset.")

            elif chart == "Box Plot":
                num_cols = list(viz_df.select_dtypes(include=np.number).columns)
                if num_cols:
                    col = st.selectbox("Numeric column", num_cols)
                    ax.boxplot(viz_df[col].dropna())
                    ax.set_title(f"Box Plot of {col}")
                else:
                    st.info("No numeric columns are available in the current dataset.")

            elif chart == "Scatter Plot":
                num_cols = list(viz_df.select_dtypes(include=np.number).columns)
                if len(num_cols) >= 2:
                    x = st.selectbox("X axis", num_cols, key="scatter_x")
                    y = st.selectbox("Y axis", num_cols, key="scatter_y")
                    ax.scatter(viz_df[x], viz_df[y])
                    ax.set_title(f"{y} vs {x}")
                    ax.set_xlabel(x)
                    ax.set_ylabel(y)
                else:
                    st.info("Need at least two numeric columns.")

            elif chart == "Line Chart":
                x_candidates = list(viz_df.columns)
                y_candidates = list(viz_df.select_dtypes(include=np.number).columns)
                if y_candidates:
                    x = st.selectbox("X axis", x_candidates, key="line_x")
                    y = st.selectbox("Y axis", y_candidates, key="line_y")
                    plot_df = viz_df[[x, y]].dropna().sort_values(by=x)
                    ax.plot(plot_df[x], plot_df[y])
                    ax.set_title(f"{y} over {x}")
                    ax.set_xlabel(x)
                    ax.set_ylabel(y)
                    plt.xticks(rotation=45)
                else:
                    st.info("No numeric y-axis column available.")

            elif chart == "Bar Chart":
                cat_cols = list(viz_df.select_dtypes(include=["object", "category"]).columns)
                num_cols = list(viz_df.select_dtypes(include=np.number).columns)
                if cat_cols and num_cols:
                    x = st.selectbox("Category column", cat_cols)
                    y = st.selectbox("Value column", num_cols)
                    agg = st.selectbox("Aggregation", ["mean", "sum", "median", "count"])
                    top_n = st.slider("Top N categories", 3, 30, 10)

                    grouped = aggregate_for_bar(viz_df, x, y, agg).head(top_n)
                    ax.bar(grouped.index.astype(str), grouped.values)
                    ax.set_title(f"{agg.title()} of {y} by {x}")
                    ax.set_xlabel(x)
                    ax.set_ylabel(f"{agg}({y})")
                    plt.xticks(rotation=45)
                else:
                    st.info("Need at least one categorical and one numeric column.")

            elif chart == "Correlation Heatmap":
                corr = viz_df.corr(numeric_only=True)
                if corr.shape[0] >= 2:
                    cax = ax.matshow(corr)
                    fig.colorbar(cax)
                    ax.set_xticks(range(len(corr.columns)))
                    ax.set_yticks(range(len(corr.columns)))
                    ax.set_xticklabels(corr.columns, rotation=90)
                    ax.set_yticklabels(corr.columns)
                    ax.set_title("Correlation Heatmap", pad=20)
                else:
                    st.info("Need at least two numeric columns.")

            st.pyplot(fig)

        except Exception as e:
            st.error(f"Visualization failed: {e}")

# -----------------------------
# PAGE 6 – INSIGHTS
# -----------------------------
elif menu == "Insights":
    df = st.session_state.df

    if df is None:
        st.warning("Please upload a dataset to begin.")
    else:
        section_card(
            "Insights",
            "Generate a quick, AI-style summary of key dataset patterns, missing values, and strong correlations."
        )
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

        enable_ai = st.checkbox("Enable AI-style assistant summaries", value=True)
        st.caption("This module is optional and heuristic-based. Review outputs manually.")

        if enable_ai:
            numeric = df.select_dtypes(include=np.number)

            st.subheader("Dataset Summary")
            st.write(f"Rows: {df.shape[0]}")
            st.write(f"Columns: {df.shape[1]}")
            st.write(f"Missing values: {int(df.isna().sum().sum())}")
            st.write(f"Duplicate rows: {int(df.duplicated().sum())}")

            if not numeric.empty:
                st.subheader("Numeric Observations")
                for col in numeric.columns:
                    mean = numeric[col].mean()
                    std = numeric[col].std()
                    st.write(f"{col}: mean = {round(mean, 2)}, std = {round(std, 2)}")

                st.subheader("Strong Correlations")
                corr = numeric.corr()
                shown = set()
                found = False
                for c1 in corr.columns:
                    for c2 in corr.columns:
                        if c1 != c2 and abs(corr.loc[c1, c2]) > 0.7:
                            pair = tuple(sorted([c1, c2]))
                            if pair not in shown:
                                st.write(f"Strong correlation detected between {pair[0]} and {pair[1]}: {round(corr.loc[c1, c2], 2)}")
                                shown.add(pair)
                                found = True
                if not found:
                    st.write("No strong correlations above |0.70| detected.")
            else:
                st.info("No numeric columns are available in the current dataset.")
        else:
            st.info("AI-style insights are disabled.")

# -----------------------------
# PAGE 7 – EXPORT
# -----------------------------
elif menu == "Export":
    df = st.session_state.df

    if df is None:
        st.warning("Please upload a dataset to begin.")
    else:
        section_card(
            "Export & Report",
            "Download your refined dataset, save the transformation recipe, and export quality-check results."
        )
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

        csv_data = df.to_csv(index=False).encode("utf-8")
        xlsx_data = export_excel_bytes(df)

        st.download_button(
            "Download Clean Dataset (CSV)",
            data=csv_data,
            file_name="clean_dataset.csv",
            mime="text/csv"
        )

        st.download_button(
            "Download Clean Dataset (Excel)",
            data=xlsx_data,
            file_name="clean_dataset.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

        report = {
            "transformations": st.session_state.log,
            "timestamp": str(datetime.now()),
            "final_shape": {
                "rows": int(df.shape[0]),
                "columns": int(df.shape[1])
            }
        }

        report_json = json.dumps(report, indent=4)
        st.download_button(
            "Download Transformation Recipe (JSON)",
            data=report_json,
            file_name="transformation_recipe.json",
            mime="application/json"
        )

        if isinstance(st.session_state.violations, pd.DataFrame) and not st.session_state.violations.empty:
            violation_csv = st.session_state.violations.to_csv(index=False).encode("utf-8")
            st.download_button(
                "Download Violations Table (CSV)",
                data=violation_csv,
                file_name="validation_violations.csv",
                mime="text/csv"
            )

        st.subheader("Transformation Log")
        if st.session_state.log:
            st.dataframe(pd.DataFrame(st.session_state.log), use_container_width=True)
        else:
            st.info("No transformation steps recorded yet.")
