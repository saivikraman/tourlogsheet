## Prerequisites

Before running the project, make sure you have the following installed:

- Python
- Django

->Start project
django-admin startproject niclog(your project name)

->create app
cd niclog
python manage.py startapp tourlog(your app name)
->create templates	
          |_ _ app(any name)
		|_ _ _your html files

->views.py

- **Login**: Users can log in with their username and password. Additionally, they need to provide an Employee ID (EMP_ID). If the provided EMP_ID exists in the database, the user is redirected to view employee details. If not, they are redirected to a registration page.

- **Logout**: Users can log out of their accounts.

- **Signup**: New users can sign up for an account using a form. After successful registration, they are redirected to the login page.

- **Update**: Employees can update their information.

- **View Employee Details**: After login, employees can view their details.

- **Employee Registration**: Allows employees to register their information, including personal and travel details.

->create superuser to access admin panel
python manage.py createsuperuser
python manage.py makemigrations
python manage.py migrate

Run the development server:
Access the admin panel at http://localhost:8000/admin/ and log in with the superuser credentials to manage users and employee data.

-> Access the Employee Management System at http://localhost:8000/ to register, log in, and perform other actions.

## Usage

1. Navigate to http://localhost:8000/ to access the application.

2. Sign up for a new account or log in with an existing one.

3. Update your profile or register as an employee.

4. Log out when done.

## Project Structure

- `app/`: Contains Django app code.
- `templates/`: Contains HTML templates for rendering views.
- `models.py`: Defines the database models for the application.
- `forms.py`: Contains custom forms used in the application.
- `urls.py`: Defines URL patterns for the application.
- `views.py`: Contains the view functions for handling requests.
- `admin.py`: Configures the admin panel for managing user and employee data.

