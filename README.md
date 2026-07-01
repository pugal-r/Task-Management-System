# ✅ TODO App

A full-stack **Task Management Web Application** built with Django, featuring secure user 
authentication, complete CRUD operations, and a decoupled REST API architecture.

## 🚀 Features

- 🔐 User Authentication — Register, Login, Logout
- 👤 Profile Management — View, Update profile & Reset password
- 📝 Task Management — Add, Edit, Delete tasks
- ✅ Complete Tasks — Mark individual or all tasks as complete
- 🗑️ Trash System — Soft delete with restore functionality
- 🔗 REST API — Fully decoupled backend API using Django REST Framework
- 👥 User-Specific Data — Each user sees only their own tasks

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Django (Templates, HTML, CSS) |
| Backend | Django REST Framework |
| Database | SQLite |
| Auth | Django Built-in Authentication |
| Styling | Custom CSS3 with Outfit Font |

## 📁 Project Structure

TodoApp/
│
├── BackendApp/          # REST API Server (port 8000)
│   ├── todo_api/
│   │   ├── models.py       # TaskModel
│   │   ├── serializer.py   # TaskSerializer
│   │   ├── views.py        # API Views
│   │   └── urls.py         # API Routes
│   └── manage.py
│
└── FrontendApp/         # Frontend Server (port 1020)
├── base/
│   ├── views.py        # Task Views
│   └── urls.py         # Task Routes
├── authen/
│   ├── views.py        # Auth Views
│   └── urls.py         # Auth Routes
├── templates/          # HTML Templates
└── manage.py



## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/todo-app.git
cd todo-app
```

### 2. Install dependencies
```bash
pip install django djangorestframework requests
```

### 3. Run Backend Server
```bash
cd BackendApp
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 8000
```

### 4. Run Frontend Server
```bash
cd FrontendApp
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 1020
```

### 5. Open in browser

## 📸 Pages

| Page | Description |
|------|-------------|
| Login | Secure user login |
| Register | New user registration |
| Home | View & manage pending tasks |
| Add Task | Create a new task |
| Completed | View completed tasks |
| Trash | Restore or permanently delete tasks |
| Profile | View & update user profile |
| About | App information |

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/tasks/?user_id=` | Get all tasks for a user |
| POST | `/api/tasks/` | Create a new task |
| GET | `/api/task/<id>` | Get single task |
| PUT | `/api/task/<id>` | Update a task |
| DELETE | `/api/task/<id>` | Soft delete a task |
| PUT | `/api/completeall/?user_id=` | Complete all tasks |
| PUT | `/api/restore-all/?user_id=` | Restore all trash |
| DELETE | `/api/delete-forever/<id>` | Permanently delete |
| DELETE | `/api/delete-all-trash/?user_id=` | Empty trash |

## 👨‍💻 Author

Built with ❤️ using Django & Django REST Framework
