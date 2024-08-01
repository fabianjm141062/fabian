import streamlit as st

st.title('Aplikasi Load Settlement')

angka1 = st.number_input('Angka 1')
angka2 = st.number_input('Angka 2')

if st.button('tambahkan'):
    st.text(angka1+angka2)