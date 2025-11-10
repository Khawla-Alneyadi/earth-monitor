import streamlit as st
import time

# --- Page setup ---
st.set_page_config(page_title="Earth Monitor", layout="wide")

# --- Sidebar with environmental layers ---
st.sidebar.title("Data Layers")
layers = [
    "Mountains", "Forest", "Vegetation", "Flood", "Desert",
    "Urban", "Sea", "Temperature", "Soil Moisture", "Water"
]
selected_layers = [layer for layer in layers if st.sidebar.checkbox(layer)]

st.sidebar.markdown("---")
st.sidebar.write("Selected Layers:")
st.sidebar.write(", ".join(selected_layers) if selected_layers else "None")

# --- Navigation (main buttons) ---
st.sidebar.markdown("---")
page = st.sidebar.radio("Navigation", ["🌍 Dashboard", "📊 Change Detection", "🎥 Time-Lapse"])

# --- Dashboard Page ---
if page == "🌍 Dashboard":
    st.title("🌍 Earth Monitor Dashboard")
    st.write("""
    This page serves as the **main interface** of the system.
    Users can select environmental layers (e.g., Forest, Water, Urban), choose a location, 
    and select a specific year from the timeline below to explore **historical satellite imagery**.
    """)

    # Earth image display
    st.image("https://upload.wikimedia.org/wikipedia/commons/9/97/The_Earth_seen_from_Apollo_17.jpg", use_container_width=True)

    st.slider("Zoom Level", 0, 100, 50)
    st.slider("Select Year", 2000, 2030, 2012)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("📈 Change Detection"):
            st.session_state.page = "📊 Change Detection"
            st.experimental_rerun()
    with col2:
        if st.button("🎥 Video Mode"):
            st.session_state.page = "🎥 Time-Lapse"
            st.experimental_rerun()

    st.markdown("### 📄 Next Log Report")
    st.info("This section will later display the auto-generated report summarizing detected changes.")

# --- Change Detection Page ---
elif page == "📊 Change Detection":
    st.title("📊 Change Detection Analysis")
    st.write("""
    This page compares **two time periods** to detect changes between them. 
    It displays before-and-after maps and provides an **analysis summary** of environmental variations.
    """)

    before, after = st.columns(2)
    with before:
        st.subheader("Before (Jan 1, 2020)")
        st.image("https://earthobservatory.nasa.gov/ContentFeature/BlueMarble/Images/land_ocean_ice_2048.jpg", use_container_width=True)
    with after:
        st.subheader("After (Dec 31, 2024)")
        st.image("https://eoimages.gsfc.nasa.gov/images/imagerecords/74000/74192/world.topo.bathy.200412.3x21600x10800.jpg", use_container_width=True)

    st.markdown("### 🔍 Change Analysis Summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("Overall Change", "12.5%", delta="Significant increase detected")
    col2.metric("Time Span", "5 years")
    col3.metric("Layers Analyzed", len(selected_layers) if selected_layers else 10)

    st.markdown("#### Detailed Analysis Summary")
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
    st.write("""
    This page allows users to **visualize environmental changes over time** through an animated time-lapse.
    The user can set a date range, select data layers, and adjust playback speed to observe long-term transformations on Earth.
    """)

    start_year, end_year = st.slider("Select Date Range", 2000, 2030, (2015, 2025))
    speed = st.select_slider("Playback Speed", options=["0.5x", "1x", "2x", "4x"], value="1x")

    st.info(f"Playing time-lapse from **{start_year}** to **{end_year}** at {speed} speed.")

    st.image("https://eoimages.gsfc.nasa.gov/images/imagerecords/144000/144288/world.topo.200412.3x21600x10800.jpg", use_container_width=True)
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        progress.progress(i + 1)
    st.success("Time-lapse playback complete ✅")


