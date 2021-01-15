import streamlit as st

st.header('Streamlit demo')

st.subheader('Streamlit Sharing')

st.write('Quick test of deploying streamlit using a public github repo')

x = st.selectbox('Pick a card any card', ['None', 'A', 'B', 'C'])

if x != 'None':
    st.write(f'You picked {x}. Great choice!')

