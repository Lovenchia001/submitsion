import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
@st.cache_resource
def load_data():
    data = pd.read_csv("D:/submission/dashboard/all_data.csv")
    return data

data = load_data()

# Sidebar
st.sidebar.title("Dashboard Menu")
selected_page = st.sidebar.radio("Select a page", ["Home", "Day Data", "Hour Data"])

# Content
st.title("Bike Rental Analysis Dashboard")

if selected_page == "Home":
    st.write("Welcome to the Bike Rental Analysis Dashboard!")
    st.write("Use the sidebar to navigate to different sections.")
elif selected_page == "Day Data":
    st.subheader("Day Data")
    st.write(data)

    # Display summary statistics
    st.subheader("Summary Statistics for Day Data")
    st.write(data.describe())

    # Visualization 1
    st.subheader("Distribution of Bike Rentals by Month")
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Month', y='Count', data=data, estimator='sum', ci=None, palette='muted')
    plt.title('Distribution of Bike Rentals by Month')
    plt.xlabel('Month')
    plt.ylabel('Total Bike Rentals')
    st.pyplot()

    # Visualization 2
    st.subheader("Relationship between Weather Situation and Bike Rentals")
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='WeatherSituation', y='Count', data=data, palette='viridis')
    plt.title('Relationship between Weather Situation and Bike Rentals')
    plt.xlabel('Weather Situation')
    plt.ylabel('Bike Rentals')
    st.pyplot()

elif selected_page == "Hour Data":
    st.subheader("Hour Data")
    st.write(data)

    # Display summary statistics
    st.subheader("Summary Statistics for Hour Data")
    st.write(data.describe())

    # Check if 'Hour' is a valid column name
if 'Hour' in data.columns:
    # Display summary statistics
    st.subheader("Summary Statistics for Hour Data")
    st.write(data.describe())

    # Visualization 1
    st.subheader("Distribution of Bike Rentals by Hour")
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Hour', y='Count', data=data, estimator='sum', ci=None, palette='muted')
    plt.title('Distribution of Bike Rentals by Hour')
    plt.xlabel('Hour')
    plt.ylabel('Total Bike Rentals')
    st.pyplot()
else:
    st.warning("The column 'Hour' does not exist in the dataset.")


    # Visualization 2
    st.subheader("Relationship between Weather Situation and Bike Rentals")
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='WeatherSituation', y='Count', data=data, palette='viridis')
    plt.title('Relationship between Weather Situation and Bike Rentals')
    plt.xlabel('Weather Situation')
    plt.ylabel('Bike Rentals')
    st.pyplot()
