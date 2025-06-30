#!/usr/bin/env python
"""Streamlit-basierte Benutzeroberfl\u00e4che f\u00fcr das GENXAIS-Framework."""

import streamlit as st

try:
    from genxais_sdk import GENXAISFramework
    from genxais_sdk.storage import MongoDBConnector
except ImportError:
    GENXAISFramework = None
    MongoDBConnector = None

st.set_page_config(page_title="GENXAIS Stream UI", layout="wide")
st.title("GENXAIS Stream UI")

if GENXAISFramework:
    framework = GENXAISFramework()
else:
    st.warning("GENXAIS SDK nicht verf\u00fcgbar. Platzhalter-Modus aktiv.")
    class DummyFramework:
        def __init__(self):
            self.mode = "VAN"
        def set_mode(self, mode):
            self.mode = mode
        def get_mode(self):
            return self.mode
        def start_cycle(self, mode):
            pass
    framework = DummyFramework()

modes = ["VAN", "PLAN", "CREATE", "IMPLEMENT", "REFLECT", "ARCHIVE"]
current_mode = framework.get_mode()
selected_mode = st.sidebar.selectbox("Modus w\u00e4hlen", modes, index=modes.index(current_mode))

if st.sidebar.button("Modus setzen"):
    framework.set_mode(selected_mode)
    st.sidebar.success(f"Modus auf {selected_mode} gesetzt")

st.sidebar.markdown("---")
if st.sidebar.button("Cycle starten"):
    if hasattr(framework, "start_cycle"):
        framework.start_cycle(selected_mode)
    st.sidebar.success("Cycle gestartet")

st.header("Logs")
log_output = st.empty()

if MongoDBConnector:
    try:
        connector = MongoDBConnector()
        collection = connector.get_collection("logs")
        logs = list(collection.find().sort("_id", -1).limit(10))
        for log in logs:
            log_output.write(f"[{log.get('phase', '')}] {log.get('message', '')}")
    except Exception as exc:
        st.error(f"Fehler beim Laden der Logs: {exc}")
else:
    st.info("Keine Datenbankverbindung verf\u00fcgbar")
