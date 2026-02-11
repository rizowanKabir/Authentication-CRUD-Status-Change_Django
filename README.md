# Task Management System (Django)

A Task Management Web Application built with Django that allows users to register, login, and manage tasks with role-based access. Admin users can see all tasks, while regular users can see only their own tasks. Tasks can be added, edited, deleted, and their status updated (NotStarted, InProgress, Completed). The project uses a custom user model (UserInfoModel) and a TaskModel for task management. The UI is modern and responsive with internal CSS, hero image, badges, and dashboard cards. The project structure includes a Django app with templates, static files, models.py, views.py, urls.py, and optional forms.py. To set up, clone the repository, create a virtual environment, install dependencies (pip install -r requirements.txt), apply migrations (python manage.py makemigrations and python manage.py migrate), create a superuser (python manage.py createsuperuser), and run the development server (python manage.py runserver) at http://127.0.0.1:8000/. 

Features include user authentication (register, login, logout), role-based access control (Admin/User), add/edit/delete tasks, update task status, admin viewing all tasks, modern responsive UI with hero section, badges, dashboard cards, and internal CSS styling.

Project structure:

task_management/
├── task_app/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── dashboard.html
│   │   ├── task_list.html
│   │   ├── add_task.html
│   │   └── edit_task.html
│   ├── static/
│   │   └── images/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py (optional)
├── task_management/
│   ├── settings.py
│   └── urls.py
└── manage.py

Models:

UserInfoModel: full_name (CharField), user_type (CharField: User/Admin), username (default Django field)

TaskModel: task_name (CharField), task_description (TextField), task_status (CharField: NotStarted/InProgress/Completed), deadline (DateField), created_by (ForeignKey to UserInfoModel)

Views & URLs: home_page /, register_page /register/, login_page /login/, dashboard /dashboard/, task_list /tasks/, add_task /tasks/add/, edit_task /tasks/edit/<task_id>/, delete_task /tasks/delete/<task_id>/, change_status /tasks/status/<task_id>/

Installation & Setup: clone the repo, create virtual environment, activate it, install dependencies using pip install -r requirements.txt, apply migrations using python manage.py makemigrations and python manage.py migrate, create superuser using python manage.py createsuperuser, run server using python manage.py runserver, visit http://127.0.0.1:8000/.

Future Enhancements: task priorities and categories, email notifications for deadlines, real-time status updates with AJAX, dark/light mode toggle, API endpoints for mobile integration.

License: MIT License
