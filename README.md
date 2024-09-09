![created](https://img.shields.io/badge/created-28/07/2024-blue)
[![Open Scraping](https://img.shields.io/badge/Open_Scraping!-blue?logo=jupyter)](/sentiment-analysis/scraping.html)
[![Open Notebook](https://img.shields.io/badge/Open_Notebook!-blue?logo=jupyter)](/sentiment-analysis/notebook.html)
<a href="https://sentiment-analysis-shopee.streamlit.app/" target="_blank">
  <img src="https://img.shields.io/badge/Open_Prototype!-blue?logo=railway" alt="Prototype">
</a>
<a href="https://www.linkedin.com/in/maulana-kavaldo/" target="_blank">
  <img src="https://img.shields.io/badge/LinkedIn-blue?logo=linkedin" alt="LinkedIn">
</a>
<a href="https://www.dicoding.com/users/mkavaldo/academies" target="_blank">
  <img src="https://img.shields.io/badge/Dicoding_Profile-blue?logo=browser" alt="Dicoding Profile">
</a>

---

# Sentiment Analysis App Review (Shopee Singapore)

<div style="text-align: center;">
  <img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*8ZN0Y93fGuq-hoYHCVuutw.png" alt="Deskripsi Gambar" style="max-width: 100%; height: auto;">
</div>

## Latar Belakang:
Shopee adalah salah satu platform e-commerce terkemuka di Asia Tenggara, termasuk di Singapura. Aplikasi Shopee Singapore mendapatkan berbagai ulasan dari pengguna yang mencerminkan kepuasan dan ketidakpuasan mereka terhadap layanan yang diberikan. Memahami sentimen dari ulasan pengguna sangat penting bagi Shopee untuk meningkatkan kualitas layanan, mengidentifikasi masalah yang ada, serta memperbaiki pengalaman pengguna.

## Permasalahan Bisnis:
Bagaimana Shopee dapat secara efektif memahami, menganalisis dan memprediksi sentimen dari ulasan pengguna aplikasi di Singapura?

## Tujuan Proyek:
1. Mengumpulkan dan memproses data ulasan pengguna aplikasi Shopee Singapore.
2. Melakukan analisis sentimen untuk mengklasifikasikan ulasan menjadi sentimen positif, negatif, atau netral.
3. Membangun model prediktif yang akurat untuk memprediksi sentimen ulasan berdasarkan teks review.
4. Mengembangkan aplikasi berbasis web menggunakan Streamlit untuk memprediksi sentimen ulasan berdasarkan input teks.

## Cakupan Proyek
- Scraping data reviews aplikasi Shopee Singapore dengan bantuan library <a href='https://pypi.org/project/google-play-scraper/' target="_blank">google-play-scraper</a>.
- Text preprocessing
- Labelling dengan metode keyword dan score
- Sampling dengan SMOTE dan Random Under Sampling
- Modelling untuk memprediksi sentiment. Model yang digunakan:
    - Logistic Regression
    - Random Forest
    - Decission Tree
    - SVM
    - LSTM
    - BI LSTM
    - GRU
- Membuat aplikasi dengan streamlit untuk memprediksi inputan teks review

## Dataset
Dataset diperoleh melalui scraping dari Google Play Store. 
File `scraping.ipynb` berisi kode untuk melakukan scraping dengan menggunakan library <a href='https://pypi.org/project/google-play-scraper/' target="_blank">google-play-scraper</a> dan hasil scraping dieksport kedalam format .csv.

## Setup environment:

Direkomendasikan untuk dijalankan di Google Colab

- Upload file `notebook.ipynb` dan `scraping.ipynb` ke Google Colab atau akses 
<a href='https://colab.research.google.com/github/maulanakavaldo/sentiment-analysis/blob/main/notebook.ipynb' target="_blank">notebook.ipynb</a>
<a href='https://colab.research.google.com/github/maulanakavaldo/sentiment-analysis/blob/main/scraping.ipynb' target="_blank">scraping.ipynb</a>
- Sesuaikan **BaseDir** dengan kode yang sudah ada atau sesuaikan dengan keinginanmu
- Lakukan **run all** pada project


## Run Steamlit Prediction Apps
<div style='text-align:center;'>
    <img src="assets/sentiment-prediction.gif" alt="sentiment-prediction-preview" height="500">
</div>

1. Dijalankan di local
    - Pastikan terhubung ke internet untuk dapat melakukan install module (library) 
    - Buka cmd atau powershell as administrator

    ```bash
    pip install -r requirements.txt
    ```
    Untuk menjalankan aplikasi ini, kamu harus masuk ke folder (_directory_) yang sesuai dengan file `app.py` berada, kemudian masukkan command berikut dan tekan Enter:
    ```bash
    streamlit run app.py
    ```
 2. Akses secara online: <a href="https://sentiment-analysis-shopee.streamlit.app/" target='_blank'>Sentiment Prediction App</a> 

 ## Conclusion
- Berdasarkan analisa data, secara keseluruhan Aplikasi Shopee di Singapore lebih dominan mendapatkan score bintang 5. Ini menunjukkan bahwa pengguna aplikasi Shoope di negara tersebut sangat puas dengan layanan yang diberikan.
- Berdasarkan beberapa percobaan, model terbaik yang dihasilkan yaitu:
    - Model              : Random Forest dengan SMOTE
    - Akurasi            : > 99 %
    - Validasi akurasi   : > 97 %
- Model deep learning yang terbaik:
    - Model              : BILSTM
    - Akurasi            : 99.83 %
    - Validasi akurasi   : 99.66 %

   Model tersebut dapat digunakan untuk memprediksi review dimasa mendatang.
- Aplikasi streamlit mampu memprediksi review dari inputan user

## Saran
- Menggunakan metode lain untuk labelling seperti BERT atau yang lainnya
- Melakukan eksperimen lebih lanjut dengan menggunakan model machine learning atau deep learning yang tidak digunakan pada project ini.
- Melakukan similarity atau segmentasi pada data text
