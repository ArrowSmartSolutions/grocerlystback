# my-grocery-project

## Overview
This project is a collaborative grocery list application built using Django and Django REST Framework. It allows users to create, manage, and share grocery lists with others, providing different levels of access permissions.

## Features
- **User Management**: Users can register, log in, and manage their profiles.
- **Grocery Lists**: Users can create grocery lists, add items, and check them off when purchased.
- **Collaborative Access**: Users can share their grocery lists with others, granting different permission levels (VIEW, EDIT).
- **API Support**: The application provides a RESTful API for interacting with grocery lists and items.

## Project Structure
```
my-grocery-project
├── manage.py
├── config
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── groceries
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── permissions.py
│   ├── urls.py
│   ├── tests.py
│   └── migrations
│       └── __init__.py
├── users
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── permissions.py
│   ├── urls.py
│   ├── signals.py
│   ├── tests.py
│   └── migrations
│       └── __init__.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd my-grocery-project
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
4. Set up the database and apply migrations:
   ```
   python manage.py migrate
   ```
5. Create a superuser to access the admin panel:
   ```
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage
- Access the admin panel at `http://127.0.0.1:8000/admin/`.
- Use the API endpoints under `/api/` to interact with grocery lists and user permissions.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.