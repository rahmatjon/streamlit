import streamlit as st
import plotly.express as px
import pandas as pd

# Load the Iris dataset
df = px.data.iris()

# Streamlit App
st.title("Iris Dataset Visualization")

# Dropdowns for selecting X and Y axes
x_axis = st.selectbox("Select X-axis:", df.columns[:-1])
y_axis = st.selectbox("Select Y-axis:", df.columns[:-1])

# Create a scatter plot
fig = px.scatter(df, x=x_axis, y=y_axis, color="species", 
                 title="Iris Dataset Scatter Plot")

# Display the plot
st.plotly_chart(fig)
