import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time

st.title("📤 Upload Data CSV / Excel")

@st.cache_data
def load_file(uploaded_file):
    if uploaded_file.name.endswith(".csv"):
        return pd.read_csv(uploaded_file)
    else:
        return pd.read_excel(uploaded_file, engine="openpyxl")

uploaded_file = st.file_uploader("Pilih file (CSV atau Excel)", type=["csv", "xlsx", "xls"])

if uploaded_file:
    try:
        df = load_file(uploaded_file)
        st.session_state["data"] = df
        st.success("File berhasil diupload! 🎉")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Gagal membaca file: {e}")
else:
    st.info("Silakan upload file dengan format .csv atau .xlsx / .xls")


st.title("📊 Histplot: Distribusi Data Volume")

if "data" in st.session_state:
    df = st.session_state["data"]
    if "Volume" in df.columns:
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.histplot(df["Volume"], kde=True, bins=20, ax=ax)
        ax.set_title("Distribusi dari Vol.")
        ax.set_xlabel("Vol.")
        ax.set_ylabel("Persentase")
        st.pyplot(fig)
    else:
        st.warning("Kolom 'Volume' tidak ditemukan dalam data.")
else:
    st.info("Silakan upload file terlebih dahulu.")


st.title("📈 Animasi Harga per Hari")

if "data" in st.session_state:
    df = st.session_state["data"]
    if "Tanggal" in df.columns and "Harga" in df.columns:
        df['Tanggal'] = pd.to_datetime(df['Tanggal'], errors='coerce')
        df = df.dropna(subset=['Tanggal'])
        df = df.sort_values("Tanggal")

        speed = st.slider("Kecepatan animasi (detik)", 0.1, 2.0, 0.5)

        x, y = [], []
        fig, ax = plt.subplots()
        plot = st.empty()

        for i in range(0, len(df), 5):
            x.append(df['Tanggal'].iloc[i])
            y.append(df['Harga'].iloc[i])
            ax.clear()
            ax.plot(x, y, marker='o')
            ax.set_xlabel("Tanggal")
            ax.set_ylabel("Harga")
            ax.set_title("Harga vs Tanggal")
            ax.tick_params(axis='x', rotation=45)
            plot.pyplot(fig)
            time.sleep(speed)
    else:
        st.warning("Kolom 'Tanggal' dan/atau 'Harga' tidak ditemukan dalam data.")
else:
    st.warning("Silakan upload data terlebih dahulu.")


st.markdown(
    "<div style='text-align: center; color: gray; font-size: 50px; margin-top: 50px;'>© 2025 by Hilman Hendiyanto</div>",
    unsafe_allow_html=True
)
