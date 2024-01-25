
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

df= pd.read_csv('final_customer_data_with_recommendations.csv')

# Add a multiselect widget to select rows based on the index
customer= sorted(df.User_Id.unique())
selected_indices = st.multiselect('Select a customer:', options=customer)

# Subset the dataframe with the selected indices
selected_rows = df.loc[df['User_Id'].isin(selected_indices)]

# Display the selected data
st.write('Recomended merchants for selected customer are:')
st.column_config.Column(width="large")
st.dataframe(selected_rows.drop('User_Id', axis =1), hide_index=True)
