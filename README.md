# ShardoX Email & Webhook Tool

Sebuah script Python interaktif yang memungkinkan Anda untuk:
- Mengirim email menggunakan Gmail dengan autentikasi dua faktor (2FA)
- Melihat log pengiriman email
- Spammer pesan ke Webhook Discord

## ✨ Fitur Unggulan

- ✅ Autentikasi 2FA menggunakan Google Authenticator
- 📧 Pengiriman email melalui Gmail (SMTP)
- 📜 Log histori pengiriman email (CSV)
- 🚀 Spammer Webhook Discord (maks 100 pesan)
- 🎨 Tampilan terminal dengan warna dinamis

---

## 📲 Cara Install & Menjalankan di Termux

### 1. **Install Termux & Update**
```bash
pkg update && pkg upgrade
pkg install python
git clone https://github.com/NamaKamu/tools-termux-shardox.git
cd tools-termux-shardox
pip install pyotp qrcode colorama requests
python shardox.py```

🛠️ Konfigurasi Gmail
Untuk mengirim email, Anda memerlukan:

- Email Gmail aktif
- App Password (bukan password biasa)

Langkah membuat App Password:

- Aktifkan 2-Step Verification di akun Gmail Anda.
- Buka https://myaccount.google.com/apppasswords
- Buat password untuk "Mail" > "Other (Custom name)".
- Salin App Password dan tempel ke bagian app_password di script ini.

# 🔐 Autentikasi Dua Faktor
Sebelum mengirim email, Anda akan diminta memverifikasi kode OTP menggunakan aplikasi seperti Google Authenticator.

# 💬 Credit
Script ini dibuat oleh NelloW

# ⚠️ Disclaimer
- Gunakan script ini dengan bijak.
- Penulis tidak bertanggung jawab atas penyalahgunaan.
