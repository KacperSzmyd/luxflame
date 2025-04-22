# 🔥 Lux Flame — Handcrafted Lighters Shop

An elegant, minimalist e-commerce web app built with Flask for showcasing and selling premium handcrafted lighters.  
No user registration required — just browse, add to cart, and order.

![Build](https://img.shields.io/github/actions/workflow/status/KacperSzmyd/luxflame/tests.yml?branch=main)
![Python](https://img.shields.io/badge/python-3.12-blue)
![Flask](https://img.shields.io/badge/flask-2.x-lightgrey)

---

## 🌟 Features

- 🛒 View a catalog of products
- 🧺 Add items to cart, update quantity, remove items
- 📦 Complete order form with delivery and contact info
- ✅ Form validation with error messages
- 🎨 Dark, stylish and responsive UI with custom hover effects
- 🧪 Full test suite using `pytest` + GitHub Actions for CI

---

## 💡 Tech Stack


| Layer       | Technology      |
|-------------|------------------|
| Backend     | Flask            |
| Database    | SQLite + SQLAlchemy |
| Frontend    | HTML5 + CSS (custom dark theme) |
| Templating  | Jinja2           |
| Storage     | Flask `session`  |
| Testing     | Pytest


---


## ⚙️ How to Run

1. Clone the repository:
   git clone https://github.com/your-username/elegancki-sklep.git
   cd elegancki-sklep

2. Set up a virtual environment:
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows

3. Install dependencies:
    pip install -r requirements.txt

4. Initialize the database
    flask --app run db init
    flask --app run db migrate -m "Initial migration"
    flask --app run db upgrade

5. Run the app:
    flask --app run run

✨ To-Do

 Responsive layout


---

License
MIT – use it freely