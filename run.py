from app import create_app
import os

app = create_app()
app.static_folder = os.path.join(os.path.dirname(__file__), "app/static")


if __name__ == "__main__":
    app.run(debug=True)
