import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the Iris dataset from Seaborn
iris = sns.load_dataset('iris')

# Add a title and a brief explanation
st.title('Iris Dataset Explorer')
st.markdown("""
This is a simple Streamlit app to demonstrate how to create interactive data visualizations with Python.""")

# Sidebar for user interaction
st.sidebar.header('Feature Selection')
# Multi-select for choosing species
species = st.sidebar.multiselect(
    'Select species',
    iris['species'].unique(),
    default=iris['species'].unique()
)
# Radio button to choose plot type
plot_type = st.sidebar.radio('Select plot type', ['Single Plot', 'Pair Plot'])
# Conditional selectboxes for single plot
if plot_type == 'Single Plot':
    x_feature = st.sidebar.selectbox('Select X-axis feature', iris.columns[:-1])
    y_feature = st.sidebar.selectbox('Select Y-axis feature', iris.columns[:-1])
# Checkbox to show raw data
show_raw_data = st.sidebar.checkbox('Show raw data')

# Filter the dataset based on selected species
filtered_iris = iris[iris['species'].isin(species)]

# Display the visualization
st.subheader('Visualization')
if plot_type == 'Single Plot':
    # Create a single scatter plot
    fig, ax = plt.subplots()
    sns.scatterplot(data=filtered_iris, x=x_feature, y=y_feature, hue='species', ax=ax)
    ax.set_title(f'{x_feature} vs {y_feature}')
    st.pyplot(fig)
else:
    # Create a pair plot for all features
    pair_fig = sns.pairplot(filtered_iris, hue='species')
    st.pyplot(pair_fig.fig)

# Show raw data if the checkbox is selected
if show_raw_data:
    st.subheader('Raw Data')
    st.write(filtered_iris)
