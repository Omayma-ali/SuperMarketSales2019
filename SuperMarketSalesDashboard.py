import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Setting page configuration
st.set_page_config(page_title="SuperMarketSales2019", page_icon="💹", layout='wide')

# Loading data
df = pd.read_csv('SuperMarketSales2019.csv')

# Dashboard title
#st.title("Supermarket Sales 2019 Dashboard")

# Sidebar checkboxes for filtering
product_line = st.sidebar.selectbox("Product Line", list(df['Product line'].unique()))
month = st.sidebar.selectbox("Month", list(df['month'].unique()))
week = st.sidebar.selectbox("Week", list(df['Days'].unique()))
hour = st.sidebar.selectbox("Hour", list(df['Hours'].unique()))

# Applying filters
if product_line:
    df = df[df['Product line']==product_line]
if month:
    df = df[df['month']==month]
if week:
    df = df[df['Days']==week]
if hour:
    df = df[df['Hours']==hour]

# Information Cards
card1, card2, card3, card4 = st.columns(4)
card1.metric("Total Sales", round(df['Total'].sum()))
card2.metric("Gross Margin AVG.", round(df['gross margin percentage'].mean()))
card3.metric("Taxes", round(df['Tax 5%'].sum()))
card4.metric("Rating", round(df['Rating'].sum()))

# Data visuals
visual1, visual2 = st.columns(2)
with visual1:
    st.subheader('Total Sales Per Branch')
    fig = px.bar(data_frame=df, x='City', y='Total', color='Gender', template='plotly_dark')
    st.plotly_chart(fig, use_container_width=True)

with visual2:
    st.subheader('Quantities Per Branch')
    fig = px.pie(data_frame=df, names='City', values=df['Quantity'], template='plotly_dark')
    fig.update_traces(text=df['City'], textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

visual3, visual4 = st.columns(2)
with visual3:
    st.subheader('Total Sales Per Payment')
    fig = px.pie(data_frame=df, names='Payment', values=df['Total'], template='plotly_dark')
    fig.update_traces(text=df['Payment'], textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

with visual4:
    st.subheader('Total Sales Per Customer type')
    fig = px.bar(data_frame=df, x='Customer type', y='Total', color='Gender', template='plotly_dark')
    st.plotly_chart(fig, use_container_width=True)
