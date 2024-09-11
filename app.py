from flask import Flask, render_template, url_for, request, redirect, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from datetime import datetime

import logging
from logging.handlers import RotatingFileHandler
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

 
app = Flask(__name__)

# Initialize Basic Authentication
auth = HTTPBasicAuth()

# JWT Configuration
app.config['JWT_SECRET_KEY'] = 'uV8@29Jk8n#V^m7Zb@M9#5tQ&l!p4^mZj$S7rF6vV1WY?%E0^XAbL$k'  # Required for JWT Authentication
jwt = JWTManager(app)

# Define a dictionary for usernames and passwords (simple for now)
users = {
    "admin": "password123",
}

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY']="b9f5b8a83d7441ac5e927d13" # Required for flash messages
db = SQLAlchemy(app)

# Set up logging
if not app.debug: # Only activate logging in non-debug mode
    file_handler = RotatingFileHandler('error.log', maxBytes=10240, backupCount=10)
    file_handler.setLevel(logging.ERROR)
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)

# Database model for tasks
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id
 
# Verify the username and password
@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username 

# Route for displaying and adding tasks
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        
        # Validate that task content is not empty
        if not task_content.strip():
            flash('Task content cannot be empty!', 'error')
            return redirect('/')
        
        # Validate that task content length is not greater than 200 characters
        if len(task_content) > 200:
            flash('Task content is too long. Maximum 200 characters allowed!', 'error')
            return redirect('/')
        
        new_task = Todo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            flash('Task added successfully!', 'success')
            return redirect('/')
        except:
            flash('There was an issue adding your task', 'error')
            return redirect('/')

    # When it's a GET request, render the template
    else:
        # Get the current page number from the query string (default is 1)
        page = request.args.get('page', 1, type=int)

        # Fetch tasks for the current page with pagination
        tasks = Todo.query.order_by(Todo.date_created).paginate(page=page, per_page=5)

        return render_template('index.html', tasks=tasks)

# Route for deleting tasks
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        flash('Task deleted successfully!', 'success')  # Flash success message
        return redirect('/')
    except:
        flash('There was an issue deleting that task.', 'error')  # Flash error message
        return redirect('/')


# Route for updating tasks
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task_content = request.form['content']

        # Validate that task content is not empty
        if not task_content.strip():
            flash('Task content cannot be empty!', 'error')
            return redirect(f'/update/{id}')
        
        # Validate that task content length is not greater than 200 characters
        if len(task_content) > 200:
            flash('Task content is too long. Maximum 200 characters allowed!', 'error')
            return redirect(f'/update/{id}')
        
        try:
            task.content = task_content
            db.session.commit()
            flash('Task updated successfully!', 'success')
            return redirect('/')
        except:
            flash('There was an issue updating your task.', 'error')
            return redirect(f'/update/{id}')

    # When it's a GET request, render the template
    else:
        return render_template('update.html', task=task)

# API Route: Get all tasks (JWT Protected)
@app.route('/api/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    tasks = Todo.query.all()
    task_list = [{"id": task.id, "content": task.content, "date_created": task.date_created} for task in tasks]
    return jsonify(task_list)

# API Route: Get a single task by ID (JWT Protected)
@app.route('/api/tasks/<int:id>', methods=['GET'])
@jwt_required()
def get_task(id):
    task = Todo.query.get_or_404(id)
    return jsonify({"id": task.id, "content": task.content, "date_created": task.date_created})

# API Route: Create a new task (JWT Protected)
@app.route('/api/tasks', methods=['POST'])
@jwt_required()
def create_task():
    task_data = request.get_json()
    if not task_data or not task_data.get('content'):
        return jsonify({"error": "Task content is required"}), 400
    
    if len(task_data.get('content')) > 200:
        return jsonify({"error": "Task content exceeds 200 characters"}), 400
    
    new_task = Todo(content=task_data['content'])
    
    try:
        db.session.add(new_task)
        db.session.commit()
        return jsonify({"message": "Task created", "task": {"id": new_task.id, "content": new_task.content}}), 201
    except:
        return jsonify({"error": "An error occurred while creating the task"}), 500

# API Route: Update a task by ID (JWT Protected)
@app.route('/api/tasks/<int:id>', methods=['PUT'])
@jwt_required()
def update_task(id):
    task = Todo.query.get_or_404(id)
    task_data = request.get_json()

    if not task_data or not task_data.get('content'):
        return jsonify({"error": "Task content is required"}), 400
    
    if len(task_data.get('content')) > 200:
        return jsonify({"error": "Task content exceeds 200 characters"}), 400
    
    try:
        task.content = task_data['content']
        db.session.commit()
        return jsonify({"message": "Task updated", "task": {"id": task.id, "content": task.content}}), 200
    except:
        return jsonify({"error": "An error occurred while updating the task"}), 500

# API Route: Delete a task by ID (JWT Protected)
@app.route('/api/tasks/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_task(id):
    task = Todo.query.get_or_404(id)

    try:
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "Task deleted"}), 200
    except:
        return jsonify({"error": "An error occurred while deleting the task"}), 500

# Login route to authenticate and get a JWT
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    # Check if the provided username and password are valid
    if username not in users or users[username] != password:
        return jsonify({"msg": "Bad username or password"}), 401

    # Create a new token with the user identity (username)
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

# Custom 404 error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Custom 500 error page
@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()