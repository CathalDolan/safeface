![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Run the Project:
    python3 manage.py runserver

# Initial Set-up and Creating a Django Project

1. Install Django using PIP (Pip Installs Packages). In console window type 
    - pip3 install django
2. Create Project. In console window type:
    - django-admin startproject safe_face . (Full stop to put into current directory)
3. Create a .gitignore file:
    - touch .gitignore
    - If not already included, add:
        - *.sqlite3
        - *.pyc 
        - __pycache__
4. Run initial migration:
    - python3 manage.py migrate
5. Create a SuperUser to access admin:
    - python3 manage.py createsuperuser
    - Add username: CDolan
    - Add email address: cdolan@gizagig.com 
    - Add password (Min 8 characters): Navan1976
    - Confirm password
6. In settings.py ensuire os is imported
    import os


# 2. Set-up and Install User Authentication
## 2.1 Set-Up
1. Install Djano Allauth package:
    - pip3 install django-allauth
2. We get settings from [(https://django-allauth.readthedocs.io/en/latest/installation.html)]
    - Check if "'django.template.context_processors.request'" is included in settings.py "TEMPLATES". If not, add it.
    - Copy "AUTHENTICATION_BACKENDS"
        - Paste immediately beneath TEMPLATES in settings.py
        - Remove the 3 dots top and bottom
    - Install Apps 
        - Copy from "INSTALLED_APPS":
            'django.contrib.sites',
            'allauth',
            'allauth.account',
            'allauth.socialaccount',
        - Paste into "INSTALLED_APPS" in settings.py
    - Beneath "AUTHENTICATION_BACKENDS" in settings.py add:
        SITE_ID = 1
    - Go to urls.py
        - In "urlpatterns" add a path to "allauth":
            path('accounts/', include('allauth.urls')),
        - Add "include" to django.urls imports
            from django.urls import path, include
3. Update the database with new app by migrating: 
    - ensure all changes have been saved
    - python3 manage.py migrate
4. Create template folders for allauth:
    mkdir templates
    mkdir templates/allauth

## 2.2 Update default domain name in admin (Required for SM connection)                      Images
    - Expose site: python3 manage.py runserver
    - Go to admin section by adding "/admin" to url
    - Login
        - CDolan
        - Navan1976
    - In "Django Administration" navigate to "SITES" and click on "Sites"
    - Click on "example.com"
        - Update "Domain name" to safeface.example.com
        - Update "Display name" to project name. Can use capitals and spaces
        - Click "Save"

## 2.3 Email Set-Up
    - Go to settings.py
        - Beneath SITE_ID add: EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
        - Beneath that add: (All can be found in <https://django-allauth.readthedocs.io/en/latest/configuration.html>)
            ACCOUNT_AUTHENTICATION_METHOD = 'username_email' (Tells allauth we want to use usernames or emails for Authentication)
            ACCOUNT_EMAIL_REQUIRED = True (EMail is required to register)
            ACCOUNT_EMAIL_VERIFICATION = 'mandatory' (Email must be authenticated to register)
            ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True (User must add email twice when registering)
            ACCOUNT_USERNAME_MIN_LENGTH = 4 (Username must be a minim of 4 characters)
            LOGIN_URL = 'accounts/login/' (Login url)
            LOGIN_REDIRECT = '/' (Where user goes after logging in)
    - Freeze the requirements:
        pip3 freeze > requirements.txt

## 2.4 Copy allauth templates
    This allows us to customise the pages created by default by allauth. In the cli:
        cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./CI_WebShop_Django/templates/allauth
    - Removed any unrequired templates such as openid or tests
    - If not present, add a base.html file to the allauth folder
    - Add "allauth" to the project templates. The root templates are also created at this point (this can also be done later, see 4.3.5). 
        - Go to project settings.py
        - Within "DIRS" in "TEMPLATES" add two paths:
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth') 


# Version Control

Gitpod is used as the IDE for writing code. From there it is pushed to a remote repository on Github.
It is a public repo available on [(https://github.com/CathalDolan/safeface)].

Development employs the use of two principal branches; "master" and "dev". Work is carried out on the
dev branch and once complete it is merged with the master branch. NO WORK SHOULD BE CARRIED OUT ON 
THE MASTER BRANCH. As and when required, additional temporary branches were created from the dev
branch.

## New Branch Creation

1. Creation of dev branch and direct navigation to it:
    git checkout -b dev

## Written to Repo Process

1. Confirm you are on the correct branch:
    git checkout dev
2. Save changes: Click file "Save All"
3. Add changes: git add .
4. Commit changes: git commit -m "Comment: reason for commit"
5. Push changes to the repository:
    git push origin master
6. Change to master branch:
    git checkout master
7. Merge in the dev branch:
    git merge dev

## Other useful Git commands used:
- "git checkout branch_name": Switch to a different branch
- "git branch -d branch_name: Delete a branch if no conflicts (-D in place of -d if there are conflicts)
- "git status": Check that staus of additions and commits
- "git log --online": 
- "git branch -a": Show all active branches
