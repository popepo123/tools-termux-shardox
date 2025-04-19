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
python shardox.py
