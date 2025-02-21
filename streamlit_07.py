import streamlit as st
import plotly.express as px
import pandas as pd

# Load dataset
df = px.data.gapminder()

# Streamlit App Title
st.title("🌍 Gapminder Interactive Dashboard")

# Sidebar: Filters
st.sidebar.header("Filters")

# Select Continents
continents = df['continent'].unique().tolist()
selected_continents = st.sidebar.multiselect("Select Continent(s):", continents, default=continents)

# Select Year Range
year_range = st.sidebar.slider("Select Year Range:", int(df['year'].min()), int(df['year'].max()), (1952, 2007))

# Filter Data
filtered_df = df[(df['continent'].isin(selected_continents)) & (df['year'].between(year_range[0], year_range[1]))]

# Scatter Plot: GDP vs Life Expectancy (Animated)
st.subheader("📊 GDP vs Life Expectancy (Animated)")
fig1 = px.scatter(
    filtered_df, 
    x="gdpPercap", 
    y="lifeExp", 
    size="pop", 
    color="continent", 
    animation_frame="year", 
    animation_group="country",
    log_x=True, 
    size_max=60, 
    title="GDP vs Life Expectancy Over Time"
)
st.plotly_chart(fig1)

# Histogram: Life Expectancy Distribution
st.subheader("📈 Life Expectancy Distribution")
fig2 = px.histogram(filtered_df, x="lifeExp", nbins=30, color="continent", barmode="overlay")
st.plotly_chart(fig2)

# Bar Chart: Top 10 Countries by GDP (Latest Year in Range)
st.subheader("💰 Top 10 Countries by GDP")
latest_year = filtered_df["year"].max()
top_countries = filtered_df[filtered_df["year"] == latest_year].nlargest(10, "gdpPercap")
fig3 = px.bar(top_countries, x="country", y="gdpPercap", color="continent", title=f"Top 10 Countries by GDP ({latest_year})")
st.plotly_chart(fig3)

# Line Chart: Life Expectancy Trend
st.subheader("📊 Life Expectancy Trends")
fig4 = px.line(filtered_df, x="year", y="lifeExp", color="country", title="Life Expectancy Over Time")
st.plotly_chart(fig4)

# Show Data Table
if st.checkbox("Show Data Table"):
    st.write(filtered_df)
