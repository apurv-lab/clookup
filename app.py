import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv("TAR_2105.csv", dtype=str)

st.title("Customer Lookup Tool")

# User input for Customer number
c1_input = st.text_input("Enter Dealer Number/Code:")

# Search and display result
if c1_input:
    result = df[df["Customer"] == c1_input]
    if not result.empty:
        st.success(f"Dealer Name: {result.iloc[0]['Customer Name']}")
        st.info(f"Total Outstanding: ₹ {result.iloc[0]['Total Outstanding']}")
    else:
        st.warning("Customer not found. Please check the number.")
