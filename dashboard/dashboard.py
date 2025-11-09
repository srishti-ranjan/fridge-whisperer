import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="Fridge-Whisperer Dashboard", layout="wide", page_icon="🧊")

# Use environment variables for service URLs (Docker-friendly)
# Falls back to EC2 IPs if not set
PANTRYPAL_URL = os.getenv("PANTRYPAL_URL", "http://localhost:8000")
SMARTSUGGEST_URL = os.getenv("SMARTSUGGEST_URL", "http://localhost:8001")

# Sidebar for controls
with st.sidebar:
    st.title("Fridge-Whisperer Controls")
    st.markdown(f"**{datetime.now().strftime('%A, %d %B %Y, %I:%M %p')}**")

    st.header("Pantry Management")
    add_name = st.text_input("Item Name", key="add_name")
    add_qty = st.number_input("Quantity", min_value=1, value=1, step=1, key="add_qty")
    if st.button("Add Pantry Item"):
        try:
            resp = requests.post(f"{PANTRYPAL_URL}/items", json={"name": add_name, "quantity": add_qty})
            if resp.status_code in (200, 201):
                st.success("Item added!")
            else:
                st.error(f"Error: {resp.text}")
        except Exception as e:
            st.error(f"Failed to connect: {e}")

    st.subheader("Fetch/Delete Pantry Item")
    item_id = st.text_input("Item ID", key="itemid")
    action = st.selectbox("Action", ["None", "Fetch", "Delete"])
    if st.button("Do Action", key="action"):
        try:
            if action == "Fetch" and item_id:
                r = requests.get(f"{PANTRYPAL_URL}/items/{item_id}")
                if r.status_code == 200:
                    itm = r.json()
                    st.info(f"Fetched: {itm.get('name')} (Qty {itm.get('quantity')})")
                else:
                    st.warning(f"Not found: {r.text}")
            elif action == "Delete" and item_id:
                r = requests.delete(f"{PANTRYPAL_URL}/items/{item_id}")
                if r.status_code in (200, 204):
                    st.success("Deleted item.")
                else:
                    st.error(f"Delete failed: {r.text}")
        except Exception as e:
            st.error(f"Failed to connect: {e}")

    st.header("SmartSuggest: Add or Query Recipes")
    # Fetch available pantry items for selection
    pantry_items = []
    try:
        pantry_resp = requests.get(f"{PANTRYPAL_URL}/items")
        if pantry_resp.status_code == 200 and pantry_resp.json():
            pantry_items = [item['name'] for item in pantry_resp.json()]
    except Exception:
        pass

    st.subheader("Suggest Recipe by Items (Exact Match)")
    selected_items = st.multiselect("Select items for suggestion:", pantry_items, key="suggest_select")
    if st.button("Get Recipe Suggestion") and selected_items:
        try:
            input_str = ",".join(selected_items)
            r = requests.post(f"{SMARTSUGGEST_URL}/query", json={"input_items": input_str})
            if r.status_code == 200 and r.json():
                suggestions = r.json()
                st.success(f"Suggested recipe(s): {suggestions.get('suggested_items', '')}")
            else:
                st.warning("No matching recipe found.")
        except Exception as e:
            st.error(f"Failed to connect: {e}")

    # Add new recipe suggestion form
    with st.form("add_rec_suggest_form"):
        st.subheader("Add New Recipe Suggestion (All Fields)")
        input_items = st.text_input("Input items (comma-separated)", key="input_items")
        suggested_items = st.text_input("Recipe/Food name", key="suggested_items")
        score = st.number_input("Score", min_value=0.0, value=1.0, step=0.1, key="score")
        submit_rec = st.form_submit_button("Add Recipe Suggestion")
    if submit_rec:
        try:
            payload = {
                "input_items": input_items,
                "suggested_items": suggested_items,
                "score": score
            }
            r = requests.post(f"{SMARTSUGGEST_URL}/suggestions/", json=payload)
            if r.status_code in (200, 201):
                st.success("Suggestion added!")
            else:
                st.error(f"Error: {r.text}")
        except Exception as e:
            st.error(f"Failed to connect: {e}")

# Main Panel: Live pantry & suggestions tables side by side
col1, col2 = st.columns(2, gap="large")

with col1:
    st.header("\U0001F4CA Pantry Database: Live")
    try:
        resp = requests.get(f"{PANTRYPAL_URL}/items")
        if resp.status_code == 200 and resp.json():
            df = pd.DataFrame(resp.json())
            st.dataframe(df, height=400)
        else:
            st.write("Pantry is empty.")
    except Exception as e:
        st.write(f"Failed to fetch pantry: {e}")

with col2:
    st.header("\U0001F372 SmartSuggest Table: Live")
    try:
        resp = requests.get(f"{SMARTSUGGEST_URL}/suggestions/")
        if resp.status_code == 200 and resp.json():
            df_sugg = pd.DataFrame(resp.json())
            st.dataframe(df_sugg, height=400)
        else:
            st.write("No suggestions in DB yet.")
    except Exception as e:
        st.write(f"Failed to fetch suggestions: {e}")
