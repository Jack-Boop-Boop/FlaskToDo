#Todo App
A simple Todo List web application built using Flask and SQLite.

Features
Add new todo items.
View incomplete and completed tasks.
Mark tasks as complete.
Project Structure
graphql
Copy
Edit
📂 project-directory

│-- __init__.py       # Initializes the Flask app and database
│-- models.py         # Defines the database model for Todo items
│-- routes.py         # Handles the app routes and logic
│-- templates/
│   ├── index.html    # Frontend template for displaying tasks
│-- static/
│   ├── main.css      # Styles for the application
│-- todo.db           # SQLite database file (created on runtime)

Installation
Clone the repository

sh
Copy
Edit
git clone https://github.com/your-repo/todo-app.git
cd todo-app
Create and activate a virtual environment (optional but recommended)

sh
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

sh
Copy
Edit
pip install flask flask_sqlalchemy
Run the application

sh
Copy
Edit
python -m flask run
Open in browser
Visit http://127.0.0.1:5000/ to use the app.

Usage
Enter a task in the input box and click "Add Item" to save it.
Incomplete tasks are listed under "Incomplete Items."
Click "Mark As Complete" to move a task to the "Completed Items" list.
Technologies Used
Flask (for backend)
SQLite (for data storage)
HTML, CSS (for frontend)
License
This project is licensed under the MIT License.
