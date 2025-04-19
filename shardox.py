import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import colorama
from colorama import Fore
import re
import time
from datetime import datetime
import os
import csv
import pyotp
import qrcode
import requests
import time
import sys

colorama.init()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_print(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def rainbow_bold_text(text):
    colors = [Fore.RED]
    rainbow = ""
    color_index = 0
    for char in text:
        rainbow += colors[color_index] + "\033[1m" + char
        color_index = (color_index + 1) % len(colors)
    return rainbow + "\033[0m"

def cyan_color(text):
    colors = [Fore.BLUE, Fore.WHITE, Fore.CYAN]
    rainbow = ""
    color_index = 0
    for char in text:
        rainbow += colors[color_index] + "\033[1m" + char
        color_index = (color_index + 1) % len(colors)
    return rainbow + "\033[0m"
    
def yellow_color(text):
    colors = [Fore.YELLOW]
    rainbow = ""
    color_index = 0
    for char in text:
        rainbow += colors[color_index] + "\033[1m" + char
        color_index = (color_index + 1) % len(colors)
    return rainbow + "\033[0m"

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def two_factor_authentication():
    print(rainbow_bold_text("\n--- Autentikasi Dua Faktor (2FA) ---"))

    secret = "JBSWY3DPEHPK3PXP"
    totp = pyotp.TOTP(secret)

    print(rainbow_bold_text("Pindai QR Code ini menggunakan aplikasi Google Authenticator:\n"))
    uri = totp.provisioning_uri(name="ShardoX Teams", issuer_name="SX")
    img = qrcode.make(uri)
    img.show()

    print(rainbow_bold_text("Masukkan kode OTP yang muncul di aplikasi Google Authenticator:"))
    otp = input(rainbow_bold_text("Kode OTP: "))
    if totp.verify(otp):
        print(Fore.GREEN + "\033[1mAutentikasi berhasil!\033[0m")
        return True
    else:
        print(Fore.RED + "\033[1mKode OTP salah! Coba lagi.\033[0m")
        return False

def show_about():
    type_print(rainbow_bold_text("\n--- ShardoX Teams ---"))
    type_print(yellow_color("Selamat datang di server kami!"))
    type_print(yellow_color("Server ini memberikan berbagai layanan dan fitur menarik."))
    type_print(yellow_color("\nPilih opsi untuk melanjutkan:"))
    print(rainbow_bold_text("1. Kirim pesan melalui Gmail"))
    print(rainbow_bold_text("2. Lihat log pengiriman email"))
    print(rainbow_bold_text("3. Spammer Webhook Discord URL"))  # Menambahkan opsi
    print(rainbow_bold_text("4. Keluar"))
    type_print(cyan_color("\nScript ini dibuat oleh: NelloW"))
    type_print(cyan_color("Join Komunitas ShardoX: https://discord.gg/PRNUmK7ZBG"))

def get_user_choice():
    choice = input(rainbow_bold_text("\nMasukkan pilihan Anda (1/2/3/4): "))
    return choice

sender_email = "javacity.id@gmail.com"
app_password = "acwi fapy nzen huyd"

def spam_discord_webhook():
    print(rainbow_bold_text("\n--- Spammer Webhook Discord ---"))

    webhook_url = input(rainbow_bold_text("Masukkan URL Webhook Discord: "))
    message = input(rainbow_bold_text("Masukkan pesan yang ingin dikirim: "))
    message_count = input(rainbow_bold_text("Masukkan jumlah pesan yang ingin dikirim (max 100): "))

    if not message_count.isdigit() or int(message_count) > 100 or int(message_count) <= 0:
        print(rainbow_bold_text("Jumlah pesan tidak valid, harus antara 1 hingga 100!"))
        return

    for i in range(int(message_count)):
        payload = {
            "content": message
        }
        try:
            response = requests.post(webhook_url, json=payload)
            if response.status_code == 204:
                print(Fore.GREEN + f"Pesan ke-{i+1} berhasil dikirim ke Webhook Discord!" + "\033[0m")
            else:
                print(Fore.RED + f"Gagal mengirim pesan ke-{i+1}. Status: {response.status_code}" + "\033[0m")
        except Exception as e:
            print(Fore.RED + f"Terjadi kesalahan saat mengirim pesan: {e}" + "\033[0m")
            break

    back_to_main_menu()

def send_email():
    if not two_factor_authentication():
        print(Fore.RED + "\033[1mAutentikasi gagal. Pengiriman email dibatalkan.\033[0m")
        return

    last_sent_time = 0
    current_time = time.time()
    if current_time - last_sent_time < 10:
        print(rainbow_bold_text("Tunggu beberapa detik sebelum mengirim email lagi."))
        return
    last_sent_time = current_time

    receiver_email = input(rainbow_bold_text("Masukkan email tujuan: "))
    if not is_valid_email(receiver_email):
        print(rainbow_bold_text("Email tidak valid! Silakan coba lagi."))
        return
    
    body = input(rainbow_bold_text("Masukkan pesan yang ingin dikirim: "))
    if len(body) > 500:
        print(rainbow_bold_text("Pesan terlalu panjang, maksimal 500 karakter!"))
        return
    if not receiver_email or not body:
        print(rainbow_bold_text("Email tujuan atau pesan tidak boleh kosong!"))
        return

    confirmation = input(rainbow_bold_text(f"Anda akan mengirim email ke {receiver_email}. Apakah Anda yakin? (y/n): "))
    if confirmation.lower() != 'y':
        print(rainbow_bold_text("Pengiriman dibatalkan."))
        return

    subject = input(rainbow_bold_text("Masukkan subjek email (kosongkan untuk subjek default): "))
    subject = subject if subject else "Pesan dari Termux"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, app_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()

        log_email_status("Terkirim", receiver_email)

        print(Fore.GREEN + "\033[1mEmail berhasil terkirim!\033[0m")
        back_to_main_menu()

    except Exception as e:

        log_email_status(f"Gagal - {e}", receiver_email)
        print(Fore.RED + f"\033[1mTerjadi kesalahan: {e}\033[0m")
        retry_send_email()

def log_email_status(status, email):
    with open('email_log.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), status, email])

def show_email_log():
    try:
        with open('email_log.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"{row[0]} - {row[1]} - {row[2]}")
        back_to_main_menu()
    except FileNotFoundError:
        print(rainbow_bold_text("Log email tidak ditemukan."))
        back_to_main_menu()

def back_to_main_menu():
    choice = input(rainbow_bold_text("\nKembali ke menu utama? (y/n): "))
    if choice.lower() == 'y':
        show_about()
        handle_menu_choice(get_user_choice())
    else:
        print(rainbow_bold_text("Terima kasih! Sampai jumpa!"))
        exit()

def retry_send_email():
    choice = input(rainbow_bold_text("\nApakah Anda ingin mencoba mengirim email lagi? (y/n): "))
    if choice.lower() == 'y':
        send_email()
    else:
        back_to_main_menu()

def handle_menu_choice(choice):
    if choice == '1':
        send_email()
    elif choice == '2':
        show_email_log()
    elif choice == '3':
        spam_discord_webhook()
    elif choice == '4':
        print(rainbow_bold_text("Terima kasih! Sampai jumpa!"))
        exit()
    else:
        print(rainbow_bold_text("Pilihan tidak valid!"))
        show_about()
        handle_menu_choice(get_user_choice())

clear_console() 
show_about()
choice = get_user_choice()

handle_menu_choice(choice)
