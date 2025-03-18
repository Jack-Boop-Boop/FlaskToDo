# Todo App 📝

A simple Todo List web application built using Flask and SQLite. Manage your tasks efficiently with this lightweight and easy-to-use app!

## Features 🚀
- ✅ **Add new todo items**.
- 🗂️ **View incomplete and completed tasks**.
- ✔️ **Mark tasks as complete**.

## Project Structure 📂
```
📂 project-directory
│-- __init__.py       # Initializes the Flask app and database
│-- models.py         # Defines the database model for Todo items
│-- routes.py         # Handles the app routes and logic
│-- templates/
│   ├── index.html    # Frontend template for displaying tasks
│-- static/
│   ├── main.css      # Styles for the application
│-- todo.db           # SQLite database file (created on runtime)
```

## Installation 🔧

### 1. Clone the repository
```bash
git clone https://github.com/your-repo/todo-app.git
cd todo-app
```

### 2. Create and activate a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install flask flask_sqlalchemy
```

### 4. Run the application
```bash
python -m flask run
```

### 5. Open in browser
Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to use the app.

## Usage 🖥️

- Enter a task in the input box and click "Add Item" to save it.
- Incomplete tasks are listed under **"Incomplete Items"**.
- Click **"Mark As Complete"** to move a task to the **"Completed Items"** list.

## Technologies Used 💻
- **Flask** (for backend)
- **SQLite** (for data storage)
- **HTML, CSS** (for frontend)

## License 📄
This project is licensed under the [MIT License](LICENSE).
```

### Improvements:
- Added a bit more description for each section to make it clearer.
- Included some emojis for extra visual appeal and easier reading.
