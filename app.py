import streamlit as st
import pickle
import pandas as pd

# Kaydedilen modeli yükleyin
with open('kmeans_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Başlık
st.title("Şarap Kümeleme Uygulaması")

# Kullanıcıdan girdi al
st.header("Şarap Özelliklerini Girin")
alcohol = st.number_input("Alcohol")
malic_acid = st.number_input("Malic Acid")
ash = st.number_input("Ash")
ash_alcalinity = st.number_input("Ash Alcalinity")
magnesium = st.number_input("Magnesium", min_value=0, max_value=200, step=1)
total_phenols = st.number_input("Total Phenols")
flavanoids = st.number_input("Flavanoids")
nonflavanoid_phenols = st.number_input("Nonflavanoid Phenols")
proanthocyanins = st.number_input("Proanthocyanins")
color_intensity = st.number_input("Color Intensity")
hue = st.number_input("Hue")
od280 = st.number_input("OD280/OD315 of diluted wines")
proline = st.number_input("Proline", min_value=0, step=1)

# Girilen değerleri bir DataFrame olarak oluştur
data = {
    'Alcohol': [alcohol],
    'Malic_Acid': [malic_acid],
    'Ash': [ash],
    'Ash_Alcanity': [ash_alcalinity],
    'Magnesium': [magnesium],
    'Total_Phenols': [total_phenols],
    'Flavanoids': [flavanoids],
    'Nonflavanoid_Phenols': [nonflavanoid_phenols],
    'Proanthocyanins': [proanthocyanins],
    'Color_Intensity': [color_intensity],
    'Hue': [hue],
    'OD280': [od280],
    'Proline': [proline]
}
input_df = pd.DataFrame(data)

# Tahmin yap
if st.button("Şarabı Kümele"):
    prediction = model.predict(input_df)
    st.write(f"Bu şarap, {prediction[0] + 1}. kümeye ait.")
