from flask import Flask, request, render_template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__, template_folder="templates")

EMAIL = "akuntugas3916@gmail.com"
PASSWORD = "rybw zfpr cfmp fzkh"  # App Password Gmail

@app.route("/", methods=["GET"])
def index():
    # halaman utama form kontak
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send_message():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    if not all([name, email, message]):
        return render_template("index.html", error="Form tidak lengkap!")

    # buat email
    msg = MIMEMultipart()
    msg["From"] = EMAIL
    msg["To"] = EMAIL
    msg["Subject"] = "Pesan Baru dari Form Kontak"

    body = f"""
    Nama: {name}
    Email: {email}
    Pesan:
    {message}
    """
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.send_message(msg)

        # render index.html dengan pesan sukses
        return render_template("index.html", success="Terima kasih, pesan Anda berhasil dikirim!")
    except Exception as e:
        # render index.html dengan pesan error
        return render_template("index.html", error=f"Gagal mengirim pesan: {e}")

if __name__ == "__main__":
    app.run(debug=True)
