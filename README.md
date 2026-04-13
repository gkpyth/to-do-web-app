# To-Do Web App

A server-rendered to-do list web application built with Python, Flask, and SQLAlchemy. Users can add tasks, mark them complete, edit them inline, delete them, and filter by status.
\- part of bootcamp Projects Portfolio

## Features
- Add tasks via form submission
- Mark tasks complete/incomplete with checkbox toggle (strikethrough on completion)
- Inline editing — click any active task to edit it in place (Enter to save, Escape to cancel)
- Delete tasks with a single click
- Smart ordering — active tasks on top by creation order, completed tasks at the bottom sorted by most recently completed
- Filter by All, Active, or Completed via tab-based URL query parameters
- Client + server-side input validation (prevents empty/whitespace-only submissions)
- Contextual empty state messages per filter tab
- Custom gradient background with Bootstrap 5 UI components
- Auto-focus on input field after every action

## Requirements
- Python 3
- Flask
- Flask-SQLAlchemy
- python-dotenv

## Installation
```
pip install -r requirements.txt
```

## How to Run
```
python app.py
```
The app runs at `http://localhost:5000`.

## Routes

| Method | Route | Description |
|--------|-------|-------------|
| `GET` | `/` | Display tasks (optional `?filter=all\|active\|completed`) |
| `POST` | `/add_task` | Add a new task |
| `POST` | `/toggle_task/<id>` | Toggle task status between To Do and Done |
| `POST` | `/edit_task/<id>` | Update task text (inline editing) |
| `POST` | `/delete_task/<id>` | Delete a task |

## Project Structure
```
to-do-web-app/
├── app.py                 # Flask app entry point
├── config.py              # App configuration and environment variables
├── models.py              # Task database model
├── routes.py              # Route definitions
├── .env                   # Environment variables (SECRET_KEY)
├── requirements.txt
├── templates/
│   └── index.html         # Main page template (Jinja2)
└── static/
    └── css/
        └── style.css      # Custom styles and gradient background
```

## How It Works
Every interaction — adding, completing, editing, or deleting a task — submits a form to a Flask route, which updates the SQLite database and redirects back to the main page. Tab-based filtering is handled via URL query parameters (`/?filter=all`, `/?filter=active`, `/?filter=completed`), with the active tab state preserved through Jinja2 conditional rendering. Inline editing uses minimal inline JavaScript event handlers to swap task text with an input field on click — the actual save is still a standard form POST to Flask. Tasks are automatically sorted with active items on top (by creation order) and completed items at the bottom (by most recent completion time).

## Limitations
- Full page reload on every action (no client-side interactivity beyond inline editing)
- No drag-and-drop reordering (would require a JavaScript library and AJAX calls)
- No user authentication or multi-user support
- Completed tasks cannot be edited — must be unchecked first

## Author
Ghaleb Khadra