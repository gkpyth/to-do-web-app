from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from models import db, Task
from datetime import datetime


current_year = datetime.now().year

main = Blueprint("main", __name__)

# Retrieve all tasks from the database
@main.route('/', methods=['GET'])
def get_tasks():
    """Retrieve all tasks from the database"""
    filter_type = request.args.get('filter', 'all')

    if filter_type == 'active':
        tasks = Task.query.filter_by(status='To Do').all()
    elif filter_type == 'completed':
        tasks = Task.query.filter_by(status='Done').all()
    else:
        tasks = Task.query.order_by(Task.status.desc(), Task.completed_at.desc(), Task.id.asc()).all()

    return render_template("index.html", tasks=tasks, filter_type=filter_type, current_year=current_year)

# Upon submitting the form, the new task will be added to the database
@main.route('/add_task', methods=['POST'])
def add_task():
    """Add a new task to the database"""
    task_text = request.form.get('task', '').strip()

    if task_text:
        new_task = Task(task=task_text)
        db.session.add(new_task)
        db.session.commit()

    return redirect(url_for('main.get_tasks'))

# Upon clicking on the task, enable inline editing
@main.route('/edit_task/<int:task_id>', methods=['POST'])
def edit_task(task_id):
    """Enable inline editing of a task"""
    task = Task.query.get(task_id)
    new_text = request.form.get('task', '').strip()

    if new_text:
        task.task = new_text
        db.session.commit()

    return redirect(url_for('main.get_tasks'))

# Upon checking the checkbox, the task status will be updated to 'Done'
@main.route('/toggle_task/<int:task_id>', methods=['POST'])
def toggle_task(task_id):
    """Toggle the status of a task"""
    task = Task.query.get(task_id)
    if task.status == 'To Do':
        task.status = 'Done'
        task.completed_at = datetime.now()
    else:
        task.status = 'To Do'
        task.completed_at = None

    db.session.commit()

    return redirect(url_for('main.get_tasks'))

# Upon clicking the X button, the task will be removed from the database
@main.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    """Delete a task from the database"""
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()

    return redirect(url_for('main.get_tasks'))