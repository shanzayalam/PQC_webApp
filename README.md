# Post-Quantum Cryptography Web Application

This Flask-based web app demonstrates the use of **Post-Quantum Cryptography (PQC)** using the Kyber512 algorithm (a NIST finalist). Users can:

- Generate public/private keys
- Encrypt a message using a public key
- Decrypt the ciphertext using the private key

## Tech Stack

- **Backend**: Flask (Python 3.x)
- **PQC Library**: pqcrypto
- **Frontend**: HTML, CSS, Bootstrap
- **Security**: Flask-Talisman for secure headers

---

## Features

- Kyber512 integration for key encapsulation
- Clean and interactive UI
- Secure headers via Talisman
- Safe display of keys and results (base64)

---

## ⚙️ Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/pqc-web-app.git
cd pqc-web-app
