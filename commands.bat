@echo off
REM This batch file will execute a series of commands

REM Install dependencies
pip install django
pip install python-dotenv
pip install -r requirements.txt
pip install social-auth-app-django
pip install Pillow
pip install django-crispy-forms

REM Activate the virtual environment
call .\env\Scripts\activate

REM Show Django installation
pip show django

REM Reinstall Django
pip uninstall -y django
pip install django

REM Run migrations and start the server
python manage.py migrate
python manage.py runserver
