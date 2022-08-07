import streamlit as st
import requests

st.title("Aplikasi Pengecekan Potensial Klien")
age = st.number_input("Usia")
job = st.selectbox("Pekerjaan", ['technician', 'self-employed', 'management', 'services', 'admin.',
       'blue-collar', 'retired', 'unemployed', 'student', 'entrepreneur',
       'housemaid'])
marital = st.selectbox("Status Pernikahan", ['married', 'divorced', 'single'])
education = st.selectbox("Pendidikan", ['illiterate', 'basic.4y', 'basic.6y', 'basic.9y', 'high.school', 'university.degree', 'professional.course'])
housing = st.selectbox("Apakah klien memiliki Housing Loan?", ['yes', 'no'])
loan = st.selectbox("Apakah klien memiliki Pinjaman Pribadi?", ['yes', 'no'])
contact = st.selectbox("Communication Type? (Bagaimana Klien dihubungi)", ['cellular', 'telephone'])
day_of_week = st.selectbox("Waktu Campaign (Hari)", ['thu', 'mon', 'tue', 'wed', 'fri'])
month = st.selectbox("Waktu Campaign (Bulan)", ['mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
duration = st.number_input("Durasi Kontak Terakhir dengan Klien")
campaign = st.number_input("Berapa kali klien dihubungi? (last campaign)")
previous = st.number_input("Berapa kali klien telah dihubungi sebelumnya? (sebelum last campaign)")
poutcome = st.selectbox("Apakah klien berhasil dihubungi?", ['failure', 'nonexistent', 'success'])
cons_price_idx = st.number_input("Indeks Harga Konsumen saat campaign?")

# inference
data = {'age': age,
        'job': job,
        'marital': marital,
        'education': education,
        'housing': housing,
        'loan': loan,
        'contact': contact,
        'month': month,
        'day_of_week': day_of_week,
        'duration': duration,
        'campaign':campaign,
        'previous': previous,
        'poutcome': poutcome,
        'cons.price.idx': cons_price_idx}

URL = "https://backend-p1ml2-marwan.herokuapp.com/subscribe_prediction" 

# komunikasi
r = requests.post(URL, json=data)
res = r.json()
if r.status_code == 200:
    st.title(res['result']['label_name'])
elif r.status_code == 400:
    st.title("PAGE ERROR")
    st.write(res['message'])