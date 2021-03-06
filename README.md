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

## 2.4 Create folders and copy allauth templates
    - mkdir templates
    - mkdir templates/allauth
    - Copy allauth directory into new directories so we can customise the pages created by default by allauth. In the cli:
        cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates/allauth
    - Removed any unrequired templates such as openid or tests
    - If not present, add a base.html file to the allauth folder
        - Cut and paste code from allauth/account/base.html and paste into allauth/base.html
        - Extend allauth/base.html into account html
            {% extends "base.html" %}

            {% block content %}
                <div class="container header-container">
                    <div class="overlay"></div>
                    <div class="row">
                        <div class="col-12 col-md-6">
                            <div class="allauth-form-inner-content">
                                {% block inner_content %}
                                {% endblock %}
                            </div>
                        </div>
                    </div>
                </div>
            {% endblock %}
    - Add "allauth" to the project templates. The root templates are also created at this point (this can also be done later, see 4.3.5). 
        - Go to project settings.py
        - Within "DIRS" in "TEMPLATES" add two paths:
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth')


# 3 Set-up Project Base HTML

1. Create a "base.html" file in the project templates folder
2. Go to <https://getbootstrap.com/docs/4.6/getting-started/introduction/>
    **Note**: Bootstrap 4 is employed as opposed to Bootstrap 5, because
    some changes in the latter made the tutorial code unworkable.
3. Navigate to "Starter Template" and copy complete
4. Paste it into project base.html
5. Make sure both Popper.js and Bootstrap JS are included and in this order (or combined)
6. If jQuery script is absent, navigate to <https://code.jquery.com/>
7. From jQuery Core, select most up todate stable "slim" by clicking on it and copying the
8. Paste it above the popper.ja or combined script
9. Add backwards compatibility to browsers via metat tags. Add:
    <meta htt-equiv="X-UA-Compatible" content="ie=edge">
10. Cut script lines from the bottom and paste them beneath Bootstrap link and above "title" tags
11. Add {% load static %} to the very top of the page
12. Wrap the header elements in blocks for later reuse.
    - {% block core_meta %}
    - {% block core_css %}
    - {% block core_js %}
13. Beneath each header block insert additional blocks to allow for addition of extras on later pages
    - {% block extra_meta %}
    - {% block extra_css %}
    - {% block extra_js %}
14. Add blocks and extra blocks within the body (All positioned beneath "header" tags)
    - Title: Safe Face[title]{% block extra_title %}{% endblock %}</title>
    - Page Header: {% blockpage_header %}
    - Block Content: {% block content %}
    - Extra JS: {% block postloadjs %}
15. All blocks to include {% endblock %}


# 4 Setup an App (Home in this example)

## 4.1 Basic Creation
1. Create the basic app:
    python3 manage.py startapp home
2. Create a templates directory within the new app:
    mkdir -p home/templates/home
3. Add the app name to project settings.py
    - Open project settings.py
    - Go to "INSTALLED_APPS" section
    - Add the new app name to the bottom of the list
        - Encase in single strokes and put a comma at the end: e.g. 'home',

## 4.2 Create basic html page
1. Create index.html file within inner app folder home/templates/home
2. In new file, add extend and load blocks at the top of the page
    - {% extends "base.html" %}
    - {% load static %}
    - {% block content %}

## 4.3 Create a View to render html template 
1. Navigate to the App views.py
2. Define a view (In this example for home/index)
    def index(request):
        return render(request, 'home/index.html')
3. Create an App urls.py file at the same level as urls.py
    - Add the imports
        from django.contrib import admin
        from django.urls import path
    - Create an empty path to indicate that this is the route URL and it's going to render views.index with the name of home
        urlpatterns = [
            path('', views.index, name='home'),
        ]
    - Import "views" from the current directory:
        from . import views
4. Add a path in the Project urls.py
    - Go to project urls.py
    - in "urlpatterns" beneath existing paths add:
        path('', include('home.urls')),
        path('products/', include('products.urls')),

## 4.4 Connecting to database

If the app takes advantage of a database, additional actions are required.

1. In the App folder, create a new folder called "fixtures"
2. If there are existing Json fixture files, add them
3. We need to create some "models" for the fixtures to go into:
    - Go to App models.py
    - Create class(es)
4. Make migrations:
    - Do a dry run first
        python3 manage.py makemigrations --dry-run
    - If necessary, install "pillow"
        pip3 install pillow
    - To make actual migrations
        python3 manage.py makemigrations
    - Run migrate with plan first to be sure all is OK
        python3 manage.py migrate --plan
    - If yes, run migrate
        python3 manage.py migrate
    - **Note**: It's best to specify which App the migrations are being done from. Above migrates all
5. Register the model in App admin.py
    - Go to App admin.py file
    - Import the relevant mnodel
        from .models import [model_name]
    - Register it. This goes at the end of the page
        admin.site.register([model_name])
6. Load the fixtures data
    python3 manage.py loaddata [fixture_jsonFile_name]

## 4.5 Tidying the Database Admin

Rewatch Products Set-up, Products Admin, 2nd Video in tutorials


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
6. Go to Github                                                        Images and more instructions

## Other useful Git commands used:
- "git checkout branch_name": Switch to a different branch
- "git branch -d branch_name: Delete a branch if no conflicts (-D in place of -d if there are conflicts)
- "git status": Check that staus of additions and commits
- "git log --online": 
- "git branch -a": Show all active branches


# Interesting Bugs

## Bootstrap 5 incompatibility
Needed to change to 4.6.0 because some of the XYZ wouldn't work with latest changes

## allauth base.html
Where base.html must be mannually added to the allauth folder, the code needs to be transferred from 
allauth/accounts/base.html. Additionmal code then must be added to the latter. See 2.4 above.
