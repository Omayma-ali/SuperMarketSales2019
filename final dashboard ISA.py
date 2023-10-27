#importing libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib .pyplot as plt
import seaborn as sns
import plotly.express as px

#naming page
st.set_page_config(page_title="SuperMarketSales2019", page_icon=":computer:", layout='wide')

#Loading data
df = pd.read_csv('SuperMarketSales2019.csv')

# dashboard title
st.title("Supermarket Sales 2019 Dasboard")

product_line = st.sidebar.checkbox("Day", df['Product line'].unique())
month = st.sidebar.checkbox("Product Line", df['month'].unique())
week = st.sidebar.checkbox("Product Line", df['Days'].unique())
hour = st.sidebar.checkbox("Product Line", df['Hour'].unique())