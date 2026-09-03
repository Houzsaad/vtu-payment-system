# Salisu Mahadi Data — VTU Web Application

A Django-based Virtual Top-Up (VTU) web application built for a real client. The platform allows users to purchase mobile airtime and data through a wallet-based system integrated with the VTPass API.

The project was built to handle the complete purchase flow, including wallet management, transaction processing, PIN confirmation, service delivery, transaction tracking, and refunds for failed transactions.

> **Note:** This project was one of my first real-world commercial applications and gave me practical experience building and testing a financial transaction-based system.

---

## 🚀 Live Demo

**Live Application:** https://salisumahadidata.onrender.com

**GitHub Repository:**  
https://github.com/Houzsaad/vtu-payment-system

---

## 📸 Screenshots

### Registration

<p align="center">
  <img src="https://github.com/Houzsaad/vtu-payment-system/blob/52266e4d9e9f6de1bbf35111619c70a01ae0418e/WhatsApp%20Image%202026-05-01%20at%2015.46.01.jpeg" width="500"/>
</p>

### Login

<p align="center">
  <img src="https://github.com/Houzsaad/vtu-payment-system/blob/e685eed34545b3b65d1508275d789806d04ee39b/WhatsApp%20Image%202026-05-01%20at%2015.45.34.jpeg" width="500"/>
</p>

### Dashboard

<p align="center">
  <img src="https://github.com/Houzsaad/vtu-payment-system/blob/3b13e8974935796f6a5274f192ac75a4d332de47/WhatsApp%20Image%202026-05-01%20at%2015.43.18.jpeg" width="500"/>
</p>

---

## ✨ Features

### Authentication & Security
- User registration and login
- Unique email-based authentication
- Secure password hashing
- 4-digit transaction PIN with hashing
- Authentication-protected wallet and transaction operations

### Wallet & Transactions
- Wallet balance management
- Wallet debit during purchases
- Transaction records with status tracking
- Automatic wallet refund when a transaction fails
- Transaction history

### VTU Services
- Airtime purchase
- Data bundle purchase
- Support for major Nigerian networks:
  - MTN
  - Airtel
  - Glo
  - 9mobile
- VTPass sandbox and live API integration
- Three-step purchase flow with PIN confirmation

### User Interface
- Responsive Bootstrap 5 interface
- Dashboard
- Profile page
- Customer support through WhatsApp

---

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| Backend | Python, Django 5.2 |
| Database | SQLite (development), PostgreSQL (production) |
| API Integration | VTPass API |
| Frontend | Django Templates, Bootstrap 5, Bootstrap Icons |
| Deployment | Render |
| Version Control | Git, GitHub |

---

## 🔄 How the Purchase Flow Works

The application follows this general flow:

```text
User
  ↓
Select Service
  ↓
Select Network
  ↓
Select Data Plan / Enter Airtime Amount
  ↓
Enter Phone Number
  ↓
Review Transaction
  ↓
Enter Transaction PIN
  ↓
Validate Request
  ↓
Debit Wallet
  ↓
Send Request to VTPass
  ↓
Receive Response
  ↓
Update Transaction Status
  ↓
Refund Wallet if Transaction Fails
```

 ## Installation


```bash
1. Clone the repository
git clone https://github.com/Houzsaad/data_webapp.git
cd data_webapp

2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

3. Install dependencies
pip install -r requirements.txt

4. Create .env file in root directory
SECRET_KEY=your_django_secret_key
DEBUG=True
VTPASS_API_KEY=your_vtpass_api_key
VTPASS_PUBLIC_KEY=your_vtpass_public_key
VTPASS_SECRET_KEY=your_vtpass_secret_key
VTPASS_BASE_URL=https://sandbox.vtpass.com/api

5. Run migrations
python manage.py makemigrations
python manage.py migrate

6. Create superuser
python manage.py createsuperuser

7. Run development server
python manage.py runserver

8. Admin Setup
After running the server go to http://127.0.0.1:8000/admin and add:
Service Categories
Data (slug: data)
Airtime (slug: airtime)
Service Providers
MTN, Airtel, Glo, 9mobile for both Data and Airtime

9. Service Plans
Add the available data plans with the cossesponding VTPass variation code

10. Environment Variables
Variable
Description
SECRET_KEY
Django secret key
DEBUG
True for development, False for production
VTPASS_API_KEY
VTPass API key
VTPASS_PUBLIC_KEY
VTPass public key
VTPASS_SECRET_KEY
VTPass secret key
VTPASS_BASE_URL
VTPass base URL (sandbox or live)
```

📚 What I Learned

This was one of my first real-world commercial projects and helped me move beyond tutorial-based development.

Building the application taught me how to work with:

- Real client requirements
- Wallet and transaction logic
- Third-party API integrations
- Authentication and security
- Database design
- Transaction status handling
- Failed transaction handling
- Refund logic
- Debugging
- Testing
- Deployment

ne of the biggest lessons was that making a feature work is only part of building a real application. Transaction-based systems require careful consideration of security, database consistency, API failures, wallet balances, and different possible outcomes.


👨‍💻 Author

Huzaifa Sa'ad (Houzsaad)

Backend Developer — Python & Django

GitHub: https://github.com/Houzsaad
LinkedIn: https://www.linkedin.com/in/huzaifa-sa-ad
X:  https://www.x.com/Houzsaad

📄 License

This project was developed for educational and commercial purposes.
