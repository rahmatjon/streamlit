import streamlit as st
import plotly.express as px
import pandas as pd

# Load the Gapminder dataset
df = px.data.gapminder()

# Streamlit App Title
st.title("🌍 Gapminder Data Visualization")

# Sidebar: User Controls
st.sidebar.header("Filters")

# Select Continents
continents = df['continent'].unique().tolist()
selected_continents = st.sidebar.multiselect("Select Continent(s):", continents, default=continents)

# Select Year Range
year_range = st.sidebar.slider("Select Year Range:", int(df['year'].min()), int(df['year'].max()), (1952, 2007))

# Filter the data based on user selection
filtered_df = df[(df['continent'].isin(selected_continents)) & (df['year'].between(year_range[0], year_range[1]))]

# Create an animated Scatter Plot
fig = px.scatter(
    filtered_df, 
    x="gdpPercap", 
    y="lifeExp", 
    size="pop", 
    color="continent", 
    animation_frame="year", 
    animation_group="country",
    log_x=True, 
    size_max=60, 
    title="GDP vs Life Expectancy (Animated over Time)"
)

# Display the interactive plot
st.plotly_chart(fig)

# Show Data Table
if st.checkbox("Show Data Table"):
    st.write(filtered_df)
