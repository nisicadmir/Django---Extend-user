# Django app with Django 1.10

This is an example app of extending Django User with AbstractUser. AbstractUser is extended with two types of User account. User type can be Candidate or Agent. Also the app provides different registrations for two types of accounts, extending Allauth application. After user finishes registration, he cannot view index page until he 'finishes' the registration proccess. User must type first and last name and after that the user can login. This is a simple example, you can provide different types of users and different post registration column procces.

## Installing backend (works with python2.7)
```
git clone https://admirn@bitbucket.org/admirn/django-extend-user.git
```
```
cd django-extend-user
```
```
virtualenv env
```
```
source ./env/bin/activate
```
```
pip install -r requirements.txt
```
```
cd backend
```
```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py runserver
```
Needs SMTP configuration for sending emails
