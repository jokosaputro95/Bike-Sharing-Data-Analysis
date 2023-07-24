import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Read datasets
df_day_hour = pd.read_csv("file/df_day_hour.csv")

name = "Joko Saputro"
email = "jokosaputro616@gmail.com"
id_dicoding = "joko_saputro"



def main():
    st.title("Bike Sharing Data Analysis with Python - Final Submission :sparkles:")

    # Sidebar
    with st.sidebar:
        st.header("My Profile")
        st.write("Nama Lengkap: " + name)
        st.write("Email: " + email)
        st.write("ID Dicoding: " + id_dicoding)

        st.header("Table of Content")
        st.markdown("- [Pertanyaan 1: Bagaimana keterkaitan antara kondisi cuaca dengan jumlah penyewaan sepeda harian dan per jam?](#pertanyaan-1-bagaimana-keterkaitan-antara-kondisi-cuaca-dengan-jumlah-penyewaan-sepeda-harian-dan-per-jam)", unsafe_allow_html=True)
        st.markdown("- [Pertanyaan 2: Bagaimana tren penyewaan sepeda berdasarkan musim (season) dan tahun (year)?](#pertanyaan-2-bagaimana-tren-penyewaan-sepeda-berdasarkan-musim-season-dan-tahun-year)", unsafe_allow_html=True)

    # Pertanyaan 1:
    st.header("Pertanyaan 1: Bagaimana keterkaitan antara kondisi cuaca dengan jumlah penyewaan sepeda harian dan per jam?")
    
    # Conclusion 1:
    fig = plt.figure(figsize=(10, 6))
    sns.barplot(data=df_day_hour, x='weather_y', y='count_y')
    plt.title('Jumlah Penyewaan Sepeda berdasarkan Kondisi Cuaca')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Jumlah Penyewaan')

    # Menampilkan plot
    st.pyplot(fig)

    fig = plt.figure(figsize=(10, 6))
    sns.lineplot(data=df_day_hour, x='weekday_y', y='count_y', hue='weather_y')
    plt.title('Jumlah Penyewaan Sepeda per Hari dalam Seminggu berdasarkan Kondisi Cuaca')
    plt.xlabel('Hari dalam Seminggu')
    plt.ylabel('Jumlah Penyewaan')
    st.pyplot(fig)

    # Bar plot for weatherwise weekday distribution of counts
    fig, ax = plt.subplots(figsize=(15, 8))
    sns.barplot(data=df_day_hour, x='weekday_y', y="count_y", hue="weather_y")
    ax.set_title("Weatherwise weekday distribution of counts")
    ax.set_xlabel('Hari dalam Seminggu')
    ax.set_ylabel('Jumlah Penyewa')
    plt.legend(title='Cuaca', loc='upper right')
    st.pyplot(fig)

    # Bar plot for weatherwise hour distribution of counts
    fig, ax1 = plt.subplots(figsize=(15, 8))
    sns.barplot(data=df_day_hour, x='hour', y="count_y", hue="weather_y")
    ax1.set_title("Weatherwise hour distribution of counts")
    ax1.set_xlabel('Jam')
    ax1.set_ylabel('Jumlah Penyewa')
    plt.legend(title='Cuaca', loc='upper right')
    st.pyplot(fig)

    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

    # Analisis distribusi data harian berdasarkan kondisi cuaca
    sns.countplot(data=df_day_hour, x='weekday_x', hue="weather_y", ax=ax1)
    ax1.set_title('Distribusi Data Harian Berdasarkan Kondisi Cuaca')
    ax1.set_xlabel('Hari', fontsize=12)
    ax1.set_ylabel('Jumlah Data', fontsize=12)
    ax1.legend(title='Hari', loc='upper right')

    # Analisis distribusi data perjam berdasarkan kondisi cuaca
    sns.countplot(data=df_day_hour, x='hour', hue="weather_y", ax=ax2)
    ax2.set_title('Distribusi Data Perjam Berdasarkan Kondisi Cuaca')
    ax2.set_xlabel('Jam', fontsize=12)
    ax2.set_ylabel('Jumlah Data', fontsize=12)
    ax2.legend(title='Cuaca', loc='upper right')

    # Menampilkan plot
    fig.tight_layout()
    st.pyplot(fig)

    # Pertanyaan 2:
    st.header("Pertanyaan 2: Bagaimana tren penyewaan sepeda berdasarkan musim (season) dan tahun (year)?")

    # Conclusion 2:
    fig = plt.figure(figsize=(15, 8))
    sns.barplot(x='season_x', y='count_x', hue='year_x', data=df_day_hour)
    plt.title('Tren Jumlah Penyewaan Sepeda per Musim Berdasarkan Tahun')
    plt.xlabel('Musim')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    plt.legend(title='Tahun', loc='upper right')
    st.pyplot(fig)

    # Membuat kanvas dengan 3 kolom (1 bar plot dan 2 line plot)
    fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(18, 6))

    # Bar plot untuk analisis jumlah penyewaan sepeda per jam berdasarkan tahun (yr)
    sns.barplot(x='hour', y='count_x', hue='year_y', data=df_day_hour, ax=ax1)
    ax1.set_title('Tren Jumlah Penyewaan Sepeda per Jam Berdasarkan Tahun')
    ax1.set_xlabel('Jam')
    ax1.set_ylabel('Jumlah Penyewaan Sepeda')
    ax1.legend(title='Tahun', loc='upper right')

    # Bar plot untuk analisis jumlah penyewaan sepeda per hari berdasarkan tahun (yr)
    sns.barplot(x='weekday_x', y='count_x', hue='year_x', data=df_day_hour, ax=ax2)
    ax2.set_title('Tren Jumlah Penyewaan Sepeda per Hari Berdasarkan Tahun')
    ax2.set_xlabel('Hari')
    ax2.set_ylabel('Jumlah Penyewaan Sepeda')
    ax2.legend(title='Tahun', loc='upper right')

    # Bar plot untuk analisis jumlah penyewaan sepeda per musim berdasarkan tahun (yr)
    sns.barplot(x='season_x', y='count_x', hue='year_x', data=df_day_hour, ax=ax3)
    ax3.set_title('Tren Jumlah Penyewaan Sepeda per Musim Berdasarkan Tahun')
    ax3.set_xlabel('Musim')
    ax3.set_ylabel('Jumlah Penyewaan Sepeda')
    ax3.legend(title='Tahun', loc='upper right')

    # Menampilkan plot
    fig.tight_layout()
    st.pyplot(fig)

    st.subheader("Conclusion")
    st.write("Pertanyaan 1: Bagaimana keterkaitan antara kondisi cuaca dengan jumlah penyewaan sepeda harian dan per jam?")
    st.write("Penjelasan: Berdasarkan data yang berhasil divisualisasikan keterkaitan kondisi cuaca terhadap jumlah penyewaan sepeda atau bike sharing sangatlah erat, hal ini dibuktikan pada cuaca clear (cerah) trafic penyewaan sepeda oleh pengguna baik yang statusnya registered mauapun casual sangatlah tinggi.")

    st.write("Pertanyaan 2: Bagaimana tren penyewaan sepeda berdasarkan musim (season) dan tahun (year)?")
    st.write("Penjelasan: Berdasarkan data yang berhasil divisualisasikan terlihat bahwa tren penyewaan sepeda berdasarkan musim (season) dan tahun (year) selalu mengalami peningkatan di segala musim berdasarkan setiap tahunnya.")
if __name__ == '__main__':
    main()