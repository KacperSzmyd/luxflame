# LuxFlame – Flask Web Store for Handcrafted Lighters

A minimal, stylish online store built with Flask for selling premium handcrafted lighters.  
No user registration, just smooth browsing, cart management, and order placement.  

---

## 🔥 Features

- 🖼️ Product catalog with images and detailed descriptions
- 🛒 Session-based shopping cart (no login required)
- 📬 Order form (name, email, shipping address)
- 💾 Database-driven structure using SQLAlchemy
- 📱 Fully responsive dark layout – desktop & mobile
- 🧪 Basic test suite (optional)

---

## 💡 Tech Stack


| Layer       | Technology      |
|-------------|------------------|
| Backend     | Flask            |
| Database    | SQLite + SQLAlchemy |
| Frontend    | HTML5 + CSS (custom dark theme) |
| Templating  | Jinja2           |
| Storage     | Flask `session`  |

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
 Project setup & folder structure

 Product list view

 Product detail page

 Cart add/remove functionality

 Order form & confirmation

 Responsive layout

 Basic tests (optional)

---

License
MIT – use it freely