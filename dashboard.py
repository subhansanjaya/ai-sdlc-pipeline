import json
from pathlib import Path

import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="AI SDLC Pipeline Dashboard",
    layout="wide",
)

st.title(
    "AI SDLC Pipeline Dashboard"
)

# -------------------------
# Audit Logs
# -------------------------

audit_file = Path(
    "generated/audit/audit_log.jsonl"
)

if audit_file.exists():

    records = []

    for line in audit_file.read_text().splitlines():

        records.append(
            json.loads(line)
        )

    st.header(
        "Audit Events"
    )

    st.dataframe(
        pd.DataFrame(records)
    )

else:

    st.warning(
        "No audit logs found."
    )

# -------------------------
# Evaluation Metrics
# -------------------------

metrics_file = Path(
    "generated/evaluation_metrics.json"
)

if metrics_file.exists():

    metrics = json.loads(
        metrics_file.read_text()
    )

    st.header(
        "Evaluation Metrics"
    )

    st.json(
        metrics
    )

else:

    st.warning(
        "No evaluation metrics found."
    )