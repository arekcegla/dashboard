
import streamlit as st

st.set_page_config(page_title="Production Dashboard", layout="wide")

st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to section:", ["Overview", "Production KPIs", "Quality Metrics", "Maintenance"])

st.title("📊 Production Dashboard")

def show_section(title, iframe_url):
    with st.expander(title, expanded=False):
        st.markdown(f'<iframe title="{title}" width="100%" height="600" src="{iframe_url}" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)

if section == "Overview":
    show_section("Overview - Power BI Report", "https://app.powerbi.com/view?r=PLACEHOLDER_OVERVIEW")
elif section == "Production KPIs":
    show_section("Production KPIs - Power BI Report", "https://app.powerbi.com/view?r=PLACEHOLDER_KPI")
elif section == "Quality Metrics":
    show_section("Quality Metrics - Power BI Report", "https://app.powerbi.com/view?r=PLACEHOLDER_QUALITY")
elif section == "Maintenance":
    show_section("Maintenance - Power BI Report", "https://app.powerbi.com/view?r=PLACEHOLDER_MAINTENANCE")
