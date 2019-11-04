# shopping-cart
Django project with MYSQL migrations on Project with defined categories

Run following command for using virtual environment created:
  cart_env\scripts\activate

Run following command for using virtual environment created:
  python manage.py migrate
  python manage.py runserver
  
Create super-user to login into system by :
  python manage.py createsuperuser
  -> This will ask username and password to set. Also check "y" at the end to avoid password validations
  
Now run server again and login with created user, you will see one more app i.e. Product under which 2 more entities are there.
