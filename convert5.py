import streamlit as st

st.title("Converter Representasi Data")

with st.form("converter"):
    teks = st.text_input("Masukkan teks")
    submit = st.form_submit_button("Convert")

    if submit:
        biner = ' '.join(format(ord(h), '08b') for h in teks)
        desimal = ' '.join(str(ord(h)) for h in teks)
        oktal = ' '.join(format(ord(h), 'o') for h in teks)
        hexa = ' '.join(format(ord(h), 'X') for h in teks)

        st.write("Biner:", biner)
        st.write("Desimal:", desimal)
        st.write("Oktal:", oktal)
        st.write("Hexa:", hexa)