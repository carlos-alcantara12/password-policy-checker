"""Interface web do Password Policy Checker."""

import streamlit as st

from password_checker import analisar_senha


st.set_page_config(
    page_title="Password Policy Checker",
    page_icon="🔐",
    layout="centered",
)

st.title("Password Policy Checker")
st.write(
    "Educational project that checks whether a password follows a basic policy. "
    "The password is not saved or sent anywhere by this application."
)

senha = st.text_input("Password", type="password")
botao_analisar = st.button("Check password", type="primary")

if botao_analisar:
    if not senha:
        st.warning("Enter a password before starting the analysis.")
    else:
        resultado = analisar_senha(senha)

        st.subheader(f"Classification: {resultado['classification']}")
        st.progress(resultado["score"] / 6)
        st.caption(f"Score: {resultado['score']}/6 criteria")

        st.subheader("Criteria")
        for criterio, aprovado in resultado["criteria"].items():
            if aprovado:
                st.success(criterio)
            else:
                st.error(criterio)

        if resultado["recommendations"]:
            st.subheader("Recommendations")
            for recomendacao in resultado["recommendations"]:
                st.write(f"- {recomendacao}")
        else:
            st.success("The password meets every rule in this basic policy.")

st.divider()
st.caption(
    "Meeting these rules does not guarantee that a password is secure. "
    "Do not test a real password in educational applications."
)
