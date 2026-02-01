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
        return render_template("error.html", message="Form tidak lengkap!")

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

        # tampilkan halaman sukses
        return render_template("home.html")
    except Exception as e:
        # tampilkan halaman error
        return render_template("error.html", message=f"Gagal mengirim pesan: {e}")

if __name__ == "__main__":
    app.run(debug=True)