import streamlit as st

# Page configuration
st.set_page_config(layout="wide", page_title="UTM Production Dashboard")

# Top bar with logo and company name
col_logo, col_title, col_spacer = st.columns([1, 4, 1])
with col_logo:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Mueller_logo.svg/2560px-Mueller_logo.svg.png", width=100)
with col_title:
    st.markdown("<h1 style='text-align: center;'>UTM Production Dashboard</h1>", unsafe_allow_html=True)

st.markdown("---")

# First row
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("1.1: Production Data - Fastec")
    st.info("This section will display real-time production data from FASTEC.")

with col2:
    st.subheader("1.2: TOP Breakdown")
    st.info("This section will show the most frequent breakdowns or downtime causes.")

with col3:
    st.subheader("1.3: FIELD NO. 3")
    st.info("Placeholder for additional production metric or visualization.")

# Second row
col4, col5, col6 = st.columns(3)

with col4:
    st.subheader("2.1: FIELD NO. 4")
    st.info("Placeholder for quality metrics or alerts.")

with col5:
    st.subheader("2.2: FIELD NO. 5")
    st.info("Placeholder for maintenance KPIs or MTTR/MTBF.")

with col6:
    st.subheader("2.3: FIELD NO. 6")
    st.info("Placeholder for documentation links or shift summary.")
