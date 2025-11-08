import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# --- Layout setup ---
st.set_page_config(page_title='PantryPal Dashboard', layout='wide', page_icon='🧊')

left, right = st.columns([1.5, 2], gap="large")

with left:
    st.title("PantryPal CRUD Demo")
    st.markdown(f"**Date:** {datetime.now().strftime('%A, %d %B %Y, %I:%M %p')}")
    st.header("Add a Grocery Item")
    name = st.text_input("Item Name", key="name")
    qty = st.number_input("Quantity", min_value=1, value=1, step=1, key="qty")
    if st.button("Add Item"):
        resp = requests.post("http://localhost:8000/items", json={"name": name, "quantity": qty})
        if resp.status_code == 200:
            st.success("Item added!")
        else:
            st.error(f"Error: {resp.text}")

    st.header("Fetch/Remove by ID")
    item_id = st.text_input("Item ID", key="itemid")
    ops = st.selectbox("Choose Action", ["None", "Fetch", "Delete"])
    if st.button("Go", key="go"): 
        if ops == "Fetch":
            resp = requests.get(f"http://localhost:8000/items/{item_id}")
            if resp.status_code == 200:
                item = resp.json()
                st.info(f"Fetched: {item['name']}, Qty: {item['quantity']}")
            else:
                st.warning(f"Not found: {resp.text}")
        elif ops == "Delete":
            resp = requests.delete(f"http://localhost:8000/items/{item_id}")
            if resp.status_code == 200:
                st.success("Deleted item.")
            else:
                st.error(f"Delete failed: {resp.text}")

    st.header("All Items (View)")
    resp = requests.get("http://localhost:8000/items")  # All pantry items
    if resp.status_code == 200 and resp.json():
        data = resp.json()
        df = pd.DataFrame(data)
        st.dataframe(df.style.applymap(
            lambda v: 'background-color: #FBEEC1' if isinstance(v, int) and v < 3 else '', subset=['quantity'])
        )
    else:
        st.write("No items found.")

with right:
    st.header("📊 Pantry Database: Live")
    # Optionally auto-refresh display each time app reruns
    resp = requests.get("http://localhost:8000/items")
    if resp.status_code == 200 and resp.json():
        data = resp.json()
        df = pd.DataFrame(data)
        st.dataframe(df, height=500)
    else:
        st.write("Pantry is empty.")
