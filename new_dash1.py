import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.set_page_config(layout="wide", page_title="UTM Production Dashboard Basia, das ist nurTest")

col_logo, col_title = st.columns([1, 5])
with col_logo:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Mueller_logo.svg/2560px-Mueller_logo.svg.png", width=100)
with col_title:
    st.markdown("<h1 style='text-align: center;'>UTM Production Dashboard</h1>", unsafe_allow_html=True)

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 1.1: Production Data - Fastec")
    with st.container(border=True):
        data = np.random.rand(6, 6)
        fig, ax = plt.subplots()
        sns.heatmap(data, annot=True, fmt=".1f", cmap="YlGnBu", ax=ax)
        st.pyplot(fig)

with col2:
    st.markdown("### 1.2: TOP Breakdown")
    with st.container(border=True):
        labels = ['Motor', 'Sensor', 'PLC', 'Conveyor', 'Other']
        values = [40, 25, 15, 10, 10]
        sorted_indices = np.argsort(values)[::-1]
        sorted_labels = [labels[i] for i in sorted_indices]
        sorted_values = [values[i] for i in sorted_indices]
        cum_values = np.cumsum(sorted_values)
        fig, ax1 = plt.subplots()
        ax1.bar(sorted_labels, sorted_values, color='skyblue')
        ax2 = ax1.twinx()
        ax2.plot(sorted_labels, cum_values, color='red', marker='o')
        ax1.set_ylabel("Frequency")
        ax2.set_ylabel("Cumulative")
        st.pyplot(fig)

with col3:
    st.markdown("### 1.3: FIELD NO. 3")
    with st.container(border=True):
        labels = ['Line A', 'Line B', 'Line C']
        sizes = [45, 30, 25]
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)

col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("### 2.1: SAC Data")
    with st.container(border=True):
        x = np.arange(10)
        y = np.random.randint(50, 100, size=10)
        fig, ax = plt.subplots()
        ax.plot(x, y, marker='o')
        ax.set_title("Line Chart")
        st.pyplot(fig)

with col5:
    st.markdown("### 2.2: FIELD NO. 5")
    with st.container(border=True):
        categories = ['Shift A', 'Shift B', 'Shift C']
        values = [80, 65, 90]
        fig, ax = plt.subplots()
        ax.bar(categories, values, color='orange')
        ax.set_title("Bar Chart")
        st.pyplot(fig)

with col6:
    st.markdown("### 2.3: Share drive data")
    with st.container(border=True):
        table_data = {
            "Machine": ["Line A", "Line B", "Line C", "Line D"],
            "Status": ["Running", "Stopped", "Running", "Maintenance"],
            "Color": ["🟢", "🔴", "🟢", "🔵"],
            "Efficiency (%)": [95, 60, 88, 70],
            "Downtime (min)": [5, 45, 10, 30],
            "Operator": ["John", "Anna", "Mike", "Sara"]
        }
        df = pd.DataFrame(table_data)
        st.dataframe(df, use_container_width=True)
