import streamlit as st
import time

st.set_page_config(page_title="Earth Monitor", layout="wide")

# --- Sidebar (Data Layers) ---
st.sidebar.title("Data Layers")
layers = [
    "Mountains", "Forest", "Vegetation", "Flood", "Desert",
    "Urban", "Sea", "Temperature", "Soil Moisture", "Water"
]
selected_layers = [layer for layer in layers if st.sidebar.checkbox(layer)]

st.sidebar.markdown("---")
st.sidebar.write("Selected Layers:")
st.sidebar.write(", ".join(selected_layers) if selected_layers else "None")

# --- Navigation Menu ---
st.sidebar.markdown("---")
page = st.sidebar.radio("Navigation", ["🌍 Dashboard", "📈 Change Detection", "🎥 Time-Lapse"])

# --- Main Page: Dashboard ---
if page == "🌍 Dashboard":
    st.title("🌍 Earth Monitor")
    st.markdown("Use the AI-powered global monitoring tool to visualize and analyze environmental changes.")

    col1, col2 = st.columns([3, 1])
    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/9/97/The_Earth_seen_from_Apollo_17.jpg", use_container_width=True)
    with col2:
        st.markdown("### Quick Actions")
        st.button("Change Detection 🔄")
        st.button("Video Mode ▶️")
        st.button("Next Log Report 📄")

    st.slider("Zoom Level", 0, 100, 50)
    st.date_input("Select Date", value=None)

# --- Change Detection Page ---
elif page == "📈 Change Detection":
    st.title("📈 Change Detection Analysis")
    st.write("Compare environmental changes over time using satellite-based AI models.")

    before, after = st.columns(2)
    with before:
        st.subheader("Before (Jan 1, 2020)")
        st.image("https://earthobservatory.nasa.gov/ContentFeature/BlueMarble/Images/land_ocean_ice_2048.jpg", use_container_width=True)
    with after:
        st.subheader("After (Dec 31, 2024)")
        st.image("https://eoimages.gsfc.nasa.gov/images/imagerecords/74000/74192/world.topo.bathy.200412.3x21600x10800.jpg", use_container_width=True)

    st.markdown("### 🔍 Change Analysis Summary")
    st.metric("Overall Change", "12.5%", delta="Significant increase detected")
    st.metric("Time Span", "5 years")

    st.markdown("#### Detailed Breakdown")
    st.write("""
    - Forest cover: **-12.3%**
    - Urban expansion: **+8.7%**
    - Water bodies: **-3.2%**
    - Temperature: **+1.5°C**
    - Vegetation density: **-7.8%**
    - Desert area: **+5.4%**
    """)

# --- Time-Lapse Page ---
elif page == "🎥 Time-Lapse":
    st.title("🎥 Environmental Time-Lapse Mode")
    st.write("Watch environmental changes over time between selected years.")

    start_year, end_year = st.slider("Select Date Range", 2000, 2030, (2020, 2025))
    speed = st.select_slider("Playback Speed", options=["0.5x", "1x", "2x", "4x"], value="1x")

    st.info(f"Playing time-lapse from **{start_year}** to **{end_year}** at {speed} speed.")

    st.image("https://eoimages.gsfc.nasa.gov/images/imagerecords/144000/144288/world.topo.200412.3x21600x10800.jpg", use_container_width=True)
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.03)
        progress.progress(i + 1)
    st.success("Time-lapse complete ✅")

