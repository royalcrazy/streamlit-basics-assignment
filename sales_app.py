import streamlit as st
import pandas as pd

st.title("Sales Summary Dashboard")
st.subheader("An interactive view of sales performance by category")

data = {
    'Product': ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Phone', 'Tablet', 'Charger'],
    'Category': ['Electronics', 'Accessories', 'Electronics', 'Accessories', 'Electronics', 'Electronics', 'Accessories'],
    'Sales': [1200, 50, 300, 80, 900, 600, 40]
}
df = pd.DataFrame(data)

categories = df['Category'].unique()
selected_category = st.sidebar.selectbox("Select a Category", categories)

filtered_df = df[df['Category'] == selected_category]

st.write(f"### Showing results for: {selected_category}")
st.dataframe(filtered_df)

st.line_chart(filtered_df.set_index('Product')['Sales'])