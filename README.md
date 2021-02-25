## Introduction
TFTUS CMS
## Running the application
1. Install  ```python3.7``` in windows/ubuntu/mac
2. Install virtualenv ```sudo pip3 install virtualenv```
3. create virtual env using python3 ```virtualenv -p python3 envname```
4. activate virtual env ```source {envname with path}/bin/activate```
5. Clone repo ```git clone https://github.com/ranvijay-sachan/tftus.git```
6. Navigate into the directory ```cd tftus```
7. Install the dependencies ```pip install -r requirements.txt```
8. migrate database ```python manage.py migrate```
9. create superuser ```python manage.py createsuperuser```
10. Start the backend server ```python manage.py runserver```
11. Visit the application on the browser - [http:127.0.0.1:8000](http:127.0.0.1:8000)
12. open admin panel in new tab and login with superuser password and Add master data if required - [http:127.0.0.1:8000/admin](http:127.0.0.1:8000/admin)
13. Check Swagger API doc for more details - [http://127.0.0.1:8000/swagger](http://127.0.0.1:8000/swagger)