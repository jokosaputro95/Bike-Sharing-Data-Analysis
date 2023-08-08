# Final Submission of Learning Data Analysis Class With Pyhon
Submission ini mendapatkan :star::star::star::star::star: dari reviewer

# Table of Content
- [Kriteria & Penilaian Submission](#kriteria--penilaian-submission)
- [Final Project Struture](#final-project-struture)
- [Dataset](#dataset-used)
- [Introduction](#introduction)
- [Business Problem](#business-problem)
- [Data Overview](#data-overview)
- [Methodology](#methodology)
- [Directory Structure](#directory-structure)
- [Setup Environment](#setup-environment)
- [Run Streamlit App](#run-streamlit-app)

# Kriteria & Penilaian Submission
## Kriteria
- [x] Menggunakan Salah Satu dari Dataset yang Telah disediakan
- [x] Melakukan Seluruh Proses Analisis Data dengan minimal 2 buah pertanyaan bisnis dan 2 buah visualisasi data
- [x] Proses Analisis Dibuat dalam Notebook yang Rapi
- [x] Membuat Dashboard Sederhana Menggunakan Streamlit

# Final Project Struture
```
.
├── README.md
├── Submission_Proyek_Akhir_Analisis_Data.ipynb
├── bike-sharing
├── requirements.txt
└── venv
```

## Penilaian
1. Memberikan dokumentasi menggunakan text cell pada notebook (.ipynb) untuk menjelaskan setiap tahapan analisis data. 
2. Membuat visualisasi data yang baik dan efektif dengan menerapkan prinsip desain dan integritas.
3. Deploy dashboard ke dalam streamlit cloud.
4. Menerapkan teknik analisis lanjutan seperti RFM analysis, geoanalysis, clustering, dll. (Tanpa menggunakan algoritma machine learning) 

# Dataset Used:
Data set yang digunakan pada Penyelesaian Submission Akhir ini adalah: [bike-sharing-dataset](https://drive.google.com/file/d/1RaBmV6Q6FYWU4HWZs80Suqd7KQC34diQ/view)

# Introduction
Penggunaan sepeda sebagai moda transportasi telah mendapatkan daya tarik dalam beberapa tahun terakhir karena masalah lingkungan dan kesehatan. Kota-kota di seluruh dunia telah berhasil meluncurkan program berbagi sepeda untuk mendorong penggunaan sepeda. Di bawah program tersebut, pengendara dapat menyewa sepeda menggunakan kios manual atau otomatis yang tersebar di seluruh kota untuk jangka waktu tertentu. Dalam kebanyakan kasus, pengendara dapat mengambil sepeda dari satu lokasi dan mengembalikannya ke tempat lain yang ditentukan.

# Business Problem
Tujuan dari Kasus ini adalah untuk melihat keterkaitan dan tren jumlah penyewaan sepeda berdasarkan jam, harian, musim dan kondisi cuaca.

# Data Overview
Kumpulan data ini berisi hitungan jumlah penyewaan sepeda baik secara jam, harian, musiman dan kondisi cuaca mulai dari tahun 2011 sampai dengan 2012.

**Deskripsi singkat tentang data:** </br>
1. instant: Record index
2. dteday: Date
3. season: Season (1:spring, 2:summer, 3:fall, 4:winter)
4. yr: Year (0: 2011, 1:2012)
5. mnth: Month (1 to 12)
6. hr : hour (0 to 23)
7. holiday: weather day is holiday or not (extracted from Holiday Schedule)
8. weekday: Day of the week
9. workingday: If day is neither weekend nor holiday it's 1, otherwise is 0.
10. weathersit: (extracted from Freemeteo)
Clear, Few clouds, Partly cloudy, Partly cloudy
Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
11. temp: Normalized temperature in Celsius.
12. atemp: Normalized feeling temperature in Celsius.
13. hum: Normalized humidity. The values are divided to 100 (max)
14. windspeed: Normalized wind speed. The values are divided to 67 (max)
15. casual: count of casual users
16. registered: count of registered users
17. cnt: count of total rental bikes 17. including both casual and registered

# Methodology
- Menentukan Pertanyaan Bisnis (Business Problem)
- Menyaipkan semua library yang dibutuhkan
- Data Wrangling
    - Gathering Data
    - Assessing Data
    - Cleaning Data
- Exploratory Data Analysis (EDA)
- Visualization & Explanatory Analysis
- Conclusion

# Directory Structure
```
./Bike-Sharing-Data-Analysis
├── README.md
├── Submission_Proyek_Akhir_Analisis_Data.ipynb
├── bike-sharing
│   ├── file
│   │   └── df_day_hour.csv
│   └── main.py
├── requirements.txt
└── venv
```

# Setup Environment
```
# change to directory Bike-Sharing-Data-Analysis
cd Bike-Sharing-Data-Analysis

# activate virtual environment
source venv/bin/activate

# install library
pip install -r requirements.txt
```

# Run Streamlit App
```
# change to directory bike-sharing
cd bike-sharing

# run streamlit
streamlit run main.py
```