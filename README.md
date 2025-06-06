# 🕵️‍♂️ Session Hijacking (Cookie Theft) — Phishing Simulation Demo

This is a **Flask-based web application** designed to simulate how session hijacking through cookie theft can occur. The project demonstrates vulnerabilities in cookie handling and highlights best practices for securing session cookies.

> ⚠️ **Disclaimer:** This project is intended for **educational purposes only**. Do **not** deploy in production or use maliciously.

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

### 📦 Installation

```bash
git clone https://github.com/your-username/session-hijacking-demo.git
cd session-hijacking-demo
pip install -r requirements.txt
