Description:
A simple server set up using Django framework along with rest_framework module to understand REST api's tools.
It can be used to understand tools such as GET,PUT,POST and other tools by creating your own models.




How to use:

* Clone the repository
* Create a virtual environment, activate it and run pip install -r requirements.txt
* cd into demo_rest
* Create super user using python manage.py createsuperuser, provide credentials as prompted
* If you have modified the model:
    + Run python manage.py makemigrations
    + Run python manage.py migrate
* Run python manage.py runserver 
* Click on the link sa prompted in the CLI, or copy and paste the localhost link in your browser along with port.


