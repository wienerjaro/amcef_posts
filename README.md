# amcef_posts
instalation:
  - download or clone repository
  - create venv
  - activate venv
  - run pip install -r requirements.txt 
  - python manage.py migrate (if fails delete migrations and run python manage.py makemigrations) and migrate again
  - python manage.py runserver

  - try with postman or swagger (http://localhost:8000/swagger/)
  - for use backend module create superuser, run python manage.py createsuperuser
  - log into http://localhost:8000/admin/
  
  Note: Swagger may have some issues, its new for me.
