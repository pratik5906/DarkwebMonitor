# DarkWebMonitor

A modern Django web application that helps users monitor their email and phone credentials for breaches on the dark web.  
The app features real-time breach detection, detailed breach reports, a responsive dashboard, and automatic dark mode support.

---

## Features

- **User Authentication:** Secure signup, login, and logout.
- **Credential Monitoring:** Add and manage email/phone credentials to monitor.
- **Breach Detection:** Integration with public breach APIs (e.g., LeakCheck) to check for compromised data.
- **Breach Details:** View what specific data was leaked for each breached credential.
- **Modern Dashboard:** Responsive UI built with Bootstrap 5, Animate.css, and system-based dark mode.
- **Photo Breach Guidance:** Quick access to free photo breach monitoring via Pixsy.
- **Security Best Practices:** CSRF protection, secure POST-only logout, and `.gitignore` for sensitive files.

---

## Screenshots
![Dashboard Screenshot
![Screenshot 2025-05-10 at 11 03 37 AM](https://github.com/user-attachments/assets/1815b2ee-11d3-4ec8-aed0-766e5e676609)

![Login Screenshot](screenshots/login.png)
<img width="1470" alt="Screenshot 2025-05-10 at 11 08 26 AM" src="https://github.com/user-attachments/assets/5ade3afe-bc56-4314-b4e8-95d11b45b87e" />

---

## Getting Started

### 1. Clone the repository


### 2. Set up a virtual environment
python -m venv venv source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Set up environment variables

Create a `.env` file (see `.env.example` if provided) and add your secret key and API keys.

### 5. Run migrations
python manage.py migrate

### 6. Run the development server
python manage.py runserver

---

## Usage

- **Sign up** and log in.
- **Add credentials** (email/phone) to monitor.
- **View breach status** and click “Show Details” to see what data was leaked.
- **Check credentials** manually or use the dashboard for ongoing monitoring.
- **Explore photo breach monitoring** via the Pixsy integration card.

---

## Technologies Used

- Django 5
- Bootstrap 5
- Animate.css
- Python 3
- LeakCheck API (or similar)
- [Pixsy](https://www.pixsy.com/) (for photo breach guidance)

---

## Security & Best Practices

- Sensitive files (e.g., `.env`, `db.sqlite3`) are excluded via `.gitignore`.
- All forms protected with CSRF tokens.
- Logout is POST-only (Django 5+ standard).
- No credentials or API keys are committed to the repo.

---

## License

This project is licensed under the MIT License.

---

## Author

[Pratik5906](https://github.com/pratik5906)

---

## Acknowledgements

- [LeakCheck API](https://leakcheck.io/)
- [Pixsy](https://www.pixsy.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Animate.css](https://animate.style/)

---
