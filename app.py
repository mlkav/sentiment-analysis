import streamlit as st
import joblib
import re
import string

# Load model
model = joblib.load('models/Random_Forest_SMOTE.pkl')

# Preprocessing
def preprocess_text(text):
    text = text.lower()               # Mengubah teks menjadi huruf kecil
    text = re.sub(r'@\w+', '', text)  # Hapus mention
    text = re.sub(r'#\w+', '', text)  # Hapus hashtag
    text = re.sub(r'https?://\S+|www.\S+', '', text)  # Hapus URL
    text = re.sub(r'<.*?>', '', text) # Hapus tag HTML
    text = re.sub(r'\d+', '', text)   # Hapus angka
    text = re.sub(r'[\u00B2\u00B3\u00B9\u2070-\u2079]', '', text)  # Hapus superscript
    text = text.replace('\n', ' ')    # Ganti baris baru dengan spasi
    text = re.sub(r'[{}]'.format(re.escape(string.punctuation)), ' ', text) # Mengganti tanda baca dengan spasi
    text = text.strip()               # Hapus spasi tambahan di awal dan akhir
    text = re.sub(r'\s+', ' ', text)  # Hapus spasi ganda
    return text

st.title('Aplikasi Prediksi Sentimen')

st.sidebar.title("About Me")
st.sidebar.write("Name            : Maulana Kavaldo")
st.sidebar.markdown("ID Dicoding\t: [maulanakavaldo](https://www.dicoding.com/users/maulanakavaldo/).")
st.sidebar.markdown("Reach out me : [LinkedIn](https://www.linkedin.com/in/maulana-kavaldo/) / [Github](https://github.com/maulanakavaldo)")

# Input teks
user_input = st.text_area('Masukkan teks untuk analisis sentimen:', '',  height=200)

def style_prediction(prediction):
    if prediction == 1:
        return '<p style="color:green; font-size:24px; font-weight:bold; text-align:center; letter-spacing:2px;">Positif</p>'
    elif prediction == 2:
        return '<p style="color:blue; font-size:24px; font-weight:bold; text-align:center; letter-spacing:2px;">Netral</p>'
    else:
        return '<p style="color:red; font-size:24px; font-weight:bold; text-align:center; letter-spacing:2px;">Negatif</p>'

# Prediksi
if st.button('Prediksi'):
    if user_input:
        user_input_cleaned = preprocess_text(user_input)
        user_input_vectorized = model.named_steps['tfidf'].transform([user_input_cleaned])
        prediction = model.named_steps['classifier'].predict(user_input_vectorized)
        st.markdown(style_prediction(prediction[0]), unsafe_allow_html=True)
    else:
        st.write('Harap masukkan teks untuk dianalisis.')