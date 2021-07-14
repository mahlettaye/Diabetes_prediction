import app1
import app2
import streamlit as st
PAGES = {
    "Data Overview": app1,
    "Readmission Prediction": app2
}
st.sidebar.title('Navigation')
st.title('Welcome to Streamlit demo')
st.write("Select \'Data Overview\' to see dataset information")
st.write("Select \'Readmission Prediction\' to get prediction about readmittion")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()

