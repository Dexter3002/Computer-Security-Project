# 🕵️‍♂️ Session Hijacking (Cookie Theft) —  Simulation Demo (TMI 4133 Project)

This is a **Flask-based web application** designed to simulate how session hijacking through cookie theft can occur. The project demonstrates vulnerabilities in cookie handling and highlights best practices for securing session cookies.

> ⚠️ **Disclaimer:** This project is intended for **Simulation Demo (TMI 4133 Project) purposes only**. Do **not** deploy in production or use maliciously.

---

## 🔍 Overview

**Session hijacking** is a web attack where an attacker captures a user's session cookie to impersonate them. This Flask app simulates such a vulnerability by:

- **Capturing session cookies** (due to insecure settings)
- Allowing login and signup with password hashing
- Displaying personalized dashboard content after login
- Highlighting cookie-based attack vectors

---

## 🛡️ Mitigation Techniques Demonstrated

| Technique              | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| **HttpOnly Cookies**   | Prevents client-side scripts from accessing the session cookie.             |
| **Secure Flag**        | Ensures cookies are sent only over HTTPS.                                   |
| **SameSite Policy**    | Restricts cross-site cookie sharing (e.g., `SameSite=Strict` or `Lax`).     |
| **Session Expiry**     | Automatically clears session after logout or time-out.                      |

> ⚠️ In this demo, these features are **intentionally misconfigured** to show how attacks can occur when not implemented.

---

## 🧪 Functionality Testing

| Feature                | Test Result         |
|------------------------|---------------------|
| Login/Signup           | ✅ Working           |
| Session Persistence    | ✅ Working           |
| Cookie Configuration   | ❌ Intentionally Vulnerable |
| Flash Messages         | ✅ Working           |
| Logout & Redirection   | ✅ Working           |

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.x
- Flask
- pyotp
- pip install -r requirements.txt

> 💡 **Note:** To run the full simulation and test both the vulnerable and secure implementations, you need to run the following files:
>
> 1. `cookie theft site/main.py` – This is the **vulnerable Flask application** with insecure cookie settings (simulates session hijacking risk).
> 2. `attacker_server/attacker_server.py` – This is the **attacker’s server** that receives stolen session cookies.
> 3. `protected site (mitigation)/main.py` – This is the **secured (mitigated) version** of the web application with proper cookie security flags (HttpOnly, Secure, SameSite).
>
> Use `main.py` to test how the attack is **excecuted** or **prevented** when proper session cookie configurations are applied.

