# Salisu Mahadi Data — VTU Web Application

A Django-based Virtual Top-Up (VTU) web application that allows users to purchase mobile data and airtime for all major Nigerian networks (MTN, Airtel, Glo, 9mobile) using a wallet system integrated with the VTPass API.

---

## Features

- User registration and login with unique email authentication
- Secure Password and 4-digit transaction PIN (hashed)
- Wallet system with balance tracking
- Buy data bundles for MTN and Airtel
- Buy airtime for MTN and Airtel
- Two-step purchase flow with PIN confirmation
- Transaction history with status tracking
- Automatic wallet refund on failed transactions
- VTPass sandbox and live API integration
- Responsive Bootstrap 5 UI
- Profile page with customer care (WhatsApp)

---

## Tech Stack

- **Backend** — Python, Django 5.2
- **Database** — SQLite (development), PostgreSQL (production)
- **Payment API** — VTPass
- **Frontend** — Django Templates, Bootstrap 5, Bootstrap Icons
- **Deployment** — Render (yet)

---

## Project Structure
data_webapp/
├── accounts/          # User authentication, registration, login
├── wallet/            # Wallet model, transactions
├── services/          # VTU services, VTPass integration
├── templates/         # HTML templates
├── static/            # CSS, images
├── manage.py
└── requirements.txt
---

## Installation

**1. Clone the repository**
```bash
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
Admin Setup
After running the server go to http://127.0.0.1:8000/admin and add:
Service Categories
Data (slug: data)
Airtime (slug: airtime)
Service Providers
MTN, Airtel, Glo, 9mobile for both Data and Airtime
Service Plans
Add data plans with correct VTPass variation codes
Environment Variables
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
Purchase Flow
1. User selects service (Data or Airtime)
2. User selects network (MTN, Airtel, etc.)
3. User selects plan and enters phone number
4. User reviews transaction summary
5. User enters 4-digit transaction PIN
6. Wallet is debited
7. VTPass API delivers service to phone number
8. Transaction is logged with status
9. Wallet is refunded if transaction fails
API Integration
This app uses the VTPass API for service delivery.
Sandbox URL: https://sandbox.vtpass.com/api
Live URL: https://vtpass.com/api
Author
Huzaifa Sa'ad (Houzsaad)
GitHub: @Houzsaad
License
This project is for educational and commercial use.
