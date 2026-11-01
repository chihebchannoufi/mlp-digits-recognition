# app.py
import streamlit as st
import joblib
from sklearn.datasets import load_digits
from PIL import Image, ImageOps
import numpy as np

# Charger le dictionnaire contenant le scaler et le modèle
paquet = joblib.load('modele_et_scaler.pkl')
scaler = paquet['scaler']
modele = paquet['modele']

digits = load_digits()

# Titre de l'application
st.title("Reconnaissance de Chiffres")
st.write("Bienvenue ! Cette application utilise un réseau de neurones multicouches.")

# --- PARTIE 1 : Tester une image du dataset existant ---
st.subheader("1. Tester une image du dataset")
index = st.slider("Choisissez un numéro d'image (entre 0 et 1796) :", 0, len(digits.data) - 1, 0)

image_plate = digits.images[index] / 16.0
st.image(image_plate, width=150, caption=f"Le vrai chiffre est : {digits.target[index]}")

image_vector = digits.data[index].reshape(1, -1)
image_vector_scaled = scaler.transform(image_vector)
prediction = modele.predict(image_vector_scaled)[0]

st.write(f"### Le modèle a prédit : **{prediction}**")

if prediction == digits.target[index]:
    st.success("C'est une bonne prédiction !")
else:
    st.error("Oups, le modèle s'est trompé.")

# --- PARTIE 2 : Permettre à l'utilisateur d'importer sa propre image ---
st.markdown("---")
st.subheader("2. Ou téléchargez votre propre image de chiffre")

uploaded_file = st.file_uploader("Choisissez une image (format PNG, JPG, JPEG)...", type=["png", "jpg", "jpeg"])

# Option pour inverser les couleurs si l'image a un fond blanc
inverser_couleurs = st.checkbox("Inverser les couleurs de l'image (Fond blanc -> Fond noir)", value=True)

if uploaded_file is not None:
    # Ouvrir l'image et la convertir en niveaux de gris
    img = Image.open(uploaded_file).convert('L')

    # Inverser si la case est cochée
    if inverser_couleurs:
        img = ImageOps.invert(img)

    # Redimensionner en 8x8 pixels
    img_resized = img.resize((8, 8), Image.Resampling.LANCZOS)

    # Afficher l'aperçu de ce que le modèle voit réellement
    st.image(img_resized, width=150, caption="Ce que voit le modèle (grille 8x8)")

    # Convertir en tableau numpy et normaliser entre 0 et 16
    img_array = np.array(img_resized, dtype=float)
    img_array = img_array / 255.0 * 16.0

    # Aplatir et prédire
    image_user_vector = img_array.reshape(1, -1)
    image_user_scaled = scaler.transform(image_user_vector)
    pred_user = modele.predict(image_user_scaled)[0]

    st.write(f"### Le modèle a prédit pour votre image : **{pred_user}**")