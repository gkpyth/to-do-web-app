from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from models import db, Task
from datetime import datetime

current_year = datetime.now().year

main = Blueprint("main", __name__)

# @main.route('/')
# def index():
#     """Serve the main application page"""
#     return render_template("index.html", current_year=current_year)

@main.route('/', methods=['GET'])
def get_all_tasks():
    """Retrieve all tasks from the database"""
    tasks = Task.query.all()

    return render_template("index.html", tasks=tasks)

@main.route('/add_task', methods=['POST'])
def add_task():
    """Add a new task to the database"""
    task_text = request.form.get('task')

    new_task = Task(task=task_text)
    db.session.add(new_task)
    db.session.commit()

    return redirect(url_for('main.get_all_tasks'))
