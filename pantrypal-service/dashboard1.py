import streamlit as st
import requests
import pandas as pd
from datetime import datetime

st.set_page_config(page_title='PantryPal Dashboard', layout='wide', page_icon='🧊')

# Use the EC2 public IP where FastAPI is running
FASTAPI_URL = "http://3.110.135.117:8000"

left, right = st.columns([1.5, 2], gap="large")

with left:
    st.title("PantryPal CRUD Demo")
    st.markdown(f"**Date:** {datetime.now().strftime('%A, %d %B %Y, %I:%M %p')}")
    st.header("Add a Grocery Item")
    name = st.text_input("Item Name", key="name")
    qty = st.number_input("Quantity", min_value=1, value=1, step=1, key="qty")
    add_result = st.empty()
    if st.button("Add Item"):
        resp = requests.post(f"{FASTAPI_URL}/items", json={"name": name, "quantity": qty})
        if resp.status_code in (200, 201):
            add_result.success("Item added!")
        else:
            add_result.error(f"Error: {resp.text}")

    st.header("Fetch/Delete by ID")
    item_id = st.text_input("Item ID", key="itemid")
    ops = st.selectbox("Choose Action", ["None", "Fetch", "Delete"])
    action_result = st.empty()
    if st.button("Go", key="go"):
        if ops == "Fetch" and item_id:
            resp = requests.get(f"{FASTAPI_URL}/items/{item_id}")
            if resp.status_code == 200:
                item = resp.json()
                action_result.info(f"Fetched: {item.get('name')}, Qty: {item.get('quantity')}")
            else:
                action_result.warning(f"Not found: {resp.text}")
        elif ops == "Delete" and item_id:
            resp = requests.delete(f"{FASTAPI_URL}/items/{item_id}")
            if resp.status_code == 200:
                action_result.success("Deleted item.")
            else:
                action_result.error(f"Delete failed: {resp.text}")
        else:
            action_result.info("Please enter a valid item ID and action.")

with right:
    st.header("\U0001F5C4 Pantry Database: Live")
    resp = requests.get(f"{FASTAPI_URL}/items")
    if resp.status_code == 200 and resp.json():
        data = resp.json()
        df = pd.DataFrame(data)
        st.dataframe(df, height=500)
    else:
        st.write("Pantry is empty.")
