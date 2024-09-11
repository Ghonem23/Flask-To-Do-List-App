## Flask-To-Do-List-App

![Flask-To-Do-List-App Logo](Flask-To-Do-List-App\static\images\logo.png)  
**A versatile to-do list application** built using **Flask**, **SQLAlchemy**, and **Electron**, offering both web and desktop functionality with JWT authentication and REST API support.

## Table of Contents
- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Screenshots](#screenshots)
- [Installation](#installation)
  - [Web App Setup](#web-app-setup)
  - [Desktop App Setup](#desktop-app-setup)
- [Usage](#usage)
  - [Task Management](#task-management)
  - [API Endpoints](#api-endpoints)
  - [JWT Authentication](#jwt-authentication)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

Flask-To-Do-List-App is a comprehensive to-do list application that allows users to add, update, delete, and manage tasks efficiently. The application provides both a **web-based interface** and a **desktop version** using Electron.

The app features secure user authentication with **JWT (JSON Web Tokens)** and provides a fully functional **REST API** to manage tasks via external applications. Additionally, it offers pagination, form validation, and clear flash message feedback for user actions.

---

## Key Features

- **Add, Update, and Delete Tasks**: Create tasks with ease, update task details, and remove tasks.
- **Responsive Flash Messages**: Informative flash messages for every action (task creation, update, delete, etc.).
- **Dark Mode Toggle**: Users can switch between light and dark themes.
- **Pagination**: Display tasks with pagination to improve performance and user experience.
- **REST API**: Fully functional API endpoints to manage tasks.
- **JWT Authentication**: Secure API with JSON Web Token (JWT) for authenticated access.
- **Cross-platform Desktop App**: Run the application as a standalone desktop app using **Electron**.

---

## Screenshots

![Flask-To-Do-List-App Screenshot](Flask-To-Do-List-App\static\images\1.jpg)
![Flask-To-Do-List-App Screenshot](Flask-To-Do-List-App\static\images\2.jpg)
![Flask-To-Do-List-App Screenshot](Flask-To-Do-List-App\static\images\3.jpg)

---

## Installation

### Web App Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Ghonem23/Flask-To-Do-List-App
   cd Flask-To-Do-List-App

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the dependencies
```bash
pip install -r requirements.txt
```
4. Create the SQLite database
```bash
flask db init
flask db migrate
flask db upgrade
```

5. Start the Flask development server:
```bash
python app.py
```

6. Open the web app in your browser at http://127.0.0.1:5000.

# Desktop App Setup
1. Install Node.js from https://nodejs.org/en
2. Navigate to the Electron app directory:
```bash
cd flask-electron-app
```
3. Install the Electron dependencies:
```bash
npm install
```
4. Start the Electron app:
```bash
npm start
```
5. The Electron desktop application will launch and automatically start the Flask server.

## Usage

### Task Management

- Add new tasks using the input box and "Add Task" button.
- View tasks in a paginated table with delete and update options.
- Flash messages inform users of success or failure of each action.
- Toggle between light and dark mode using the switch in the navbar.

### API Endpoints

Task Master provides a full set of REST API endpoints:

- **GET /api/tasks**: Retrieve all tasks.
- **GET /api/tasks/<id>**: Retrieve a specific task by ID.
- **POST /api/tasks**: Create a new task (JSON body with `content` is required).
- **PUT /api/tasks/<id>**: Update a task by ID.
- **DELETE /api/tasks/<id>**: Delete a task by ID.

### JWT Authentication

API endpoints are secured with JWT authentication. To access them, you will need a valid token.

- **Login**: Use your credentials to get a JWT token.
- **Token**: Include the token in the `Authorization` header for each API request:

---

## Technologies Used

- **Frontend**: HTML5, CSS3 (Poppins & Roboto fonts), Vanilla JavaScript
- **Backend**: Flask, SQLAlchemy, SQLite
- **Authentication**: JWT (JSON Web Tokens)
- **Desktop App**: Electron
- **API**: RESTful API with Flask
- **Deployment**: Flask and Electron packaging for desktop application

---

## Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements!

1. Fork the repository.
2. Create a new branch for your feature:
 ```bash
 git checkout -b feature-branch
 ```
3. Commit your changes
  ```bash
  git commit -m "Add feature"
  ```
4. Push to the branch:
  ```bash
  git push origin feature-branch
  ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

MIT License

Copyright (c) [2024] [Ahmed Hussein]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
