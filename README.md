# amcef_posts
instalation:
  - download or clone repository
   
    $ git clone https://github.com/wienerjaro/amcef_posts.git
  - jump into amcef_posts dir
   
    $ cd amcef_posts
  - create venv
  
    $ python3 -m venv amcef_venv
  - activate venv
  
    $ source amcef_venv/bin/activate
  - install requirements 
  
    $ pip install -r requirements.txt 
  - jump into posts_service
  
    $ cd posts_service
  - run prepared migrations
  
    $ python manage.py migrate (if fails delete migrations and run $python manage.py makemigrations) and migrate again
  - start server
  
    $ python manage.py runserver
    
usage:
  - try with postman or swagger (http://localhost:8000/swagger/)
  - for use backend module create superuser
  
    $ python manage.py createsuperuser
  - log into http://localhost:8000/admin/
  
  Note: Swagger may have some issues, its new for me.
