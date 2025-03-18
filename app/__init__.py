from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Correct database file path
file_path = os.path.join(os.getcwd(), "todo.db")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{file_path}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create the database tables before the first request


from app import routes
