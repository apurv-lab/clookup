import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv("TAR_2005.csv", dtype=str)

st.title("Customer Lookup Tool")

# User input for Customer number
c1_input = st.text_input("Enter Customer Number (C1):")

# Search and display result
if c1_input:
    result = df[df["Customer"] == c1_input]
    if not result.empty:
        st.success(f"Customer Name (C2): {result.iloc[0]['Customer Name']}")
        st.info(f"Total Outstanding (C3): ₹ {result.iloc[0]['Total Outstanding']}")
    else:
        st.warning("Customer not found. Please check the number.")
