
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.cache_data

df= pd.read_excel('final_customer_data_with_recommendations.xlsx')

# Add a multiselect widget to select rows based on the index
customer= sorted(df.User_Id.unique())
selected_indices = st.multiselect('Select customer:', options=customer)

# Subset the dataframe with the selected indices
selected_rows = df.loc[df['User_Id'].isin(selected_indices)]

# Display the selected data
st.write('Selected customer:')
st.column_config.Column(width="large")
st.dataframe(selected_rows.drop('User_Id', axis =1), hide_index=True)
