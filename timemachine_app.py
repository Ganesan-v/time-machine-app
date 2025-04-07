# Save as: timemachine_app.py

import asyncio
import sys

if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="Python Time Machine", page_icon="🕰️")

st.title("🌀 Python Time Machine")

# Show current date and time
now = datetime.now()
st.write("**Current date and time:**", now.strftime("%Y-%m-%d %H:%M:%S"))

# Select direction
direction = st.radio("Choose time travel direction:", ["Forward", "Backward"])

# Input time units
days = st.number_input("Days", min_value=0, max_value=10000, value=0)
hours = st.number_input("Hours", min_value=0, max_value=23, value=0)
minutes = st.number_input("Minutes", min_value=0, max_value=59, value=0)

# Travel button
if st.button("🚀 Time Travel"):
    delta = timedelta(days=days, hours=hours, minutes=minutes)
    if direction == "Forward":
        new_time = now + delta
    else:
        new_time = now - delta

    st.success(f"You traveled **{direction.lower()}** in time!")
    st.write("**New date and time:**", new_time.strftime("%Y-%m-%d %H:%M:%S"))

    # Simple visual timeline
    st.markdown("### 🕒 Timeline")
    st.write("🔵", "**Now**:", now.strftime("%Y-%m-%d %H:%M:%S"))
    st.write("➡️")
    st.write("🔴", "**New Time**:", new_time.strftime("%Y-%m-%d %H:%M:%S"))
