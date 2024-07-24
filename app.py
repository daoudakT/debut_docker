import streamlit as st
import pandas as pd

st.title(f"Bienvenue sur ma page d'importation de données.")

uploaded_file = st.file_uploader("clic ici pour importer ta données", type=["csv"])

# Vérifier si un fichier a été téléchargé
if uploaded_file is not None:
    # Lire le fichier CSV en DataFrame
    df = pd.read_csv(uploaded_file)

    # Afficher le DataFrame
    st.write("Aperçu du fichier CSV :")
    st.write(df)
else:
    st.write("Veuillez télécharger un fichier CSV.")