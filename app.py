import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Netflix Data Visualization Dashboard")

# Sample Netflix Data
data = {
    "title": [
        "Stranger Things",
        "Money Heist",
        "Wednesday",
        "Extraction",
        "Dark",
        "Squid Game",
        "Narcos",
        "The Witcher"
    ],

    "type": [
        "TV Show",
        "TV Show",
        "TV Show",
        "Movie",
        "TV Show",
        "TV Show",
        "TV Show",
        "TV Show"
    ],

    "release_year": [
        2016,
        2017,
        2022,
        2020,
        2017,
        2021,
        2015,
        2019
    ],

    "rating": [
        "TV-14",
        "TV-MA",
        "TV-14",
        "R",
        "TV-MA",
        "TV-MA",
        "TV-MA",
        "TV-14"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Show Dataset
st.subheader("Dataset Preview")
st.write(df)

# Movies vs TV Shows
st.subheader("Movies vs TV Shows")

type_counts = df["type"].value_counts()

fig1, ax1 = plt.subplots()

ax1.pie(
    type_counts.values,
    labels=type_counts.index,
    autopct="%1.1f%%"
)

st.pyplot(fig1)

# Ratings Distribution
st.subheader("Ratings Distribution")

rating_counts = df["rating"].value_counts()

fig2, ax2 = plt.subplots()

ax2.bar(
    rating_counts.index,
    rating_counts.values
)

st.pyplot(fig2)

# Release Year Trend
st.subheader("Release Year Trend")

year_counts = df["release_year"].value_counts().sort_index()

fig3, ax3 = plt.subplots()

ax3.plot(
    year_counts.index,
    year_counts.values
)

st.pyplot(fig3)