import streamlit as st
import pandas as pd

# Load captured packet data
st.title("Network Traffic Analyzer")

try:
    df = pd.read_csv("packet_log.csv")
except FileNotFoundError:
    st.error("packet_log.csv not found. Please run the packet sniffer first.")
    st.stop()

# Show raw data
st.subheader("Captured Packet Data")
st.dataframe(df)

# Show top source IPs
st.subheader("Top Source IPs")
top_src = df['source'].value_counts().head(10)
st.bar_chart(top_src)

# Show protocol distribution
st.subheader("Protocol Usage")
proto_counts = df['protocol'].value_counts()
st.bar_chart(proto_counts)
