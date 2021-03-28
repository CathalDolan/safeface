(#Contents)
(#some-markdown-heading) so your link should look like so:




# 1 Introduction
Back to Contents

Safe Face is my fourth milestone project for the Code Institute "Full Stack Software Development Diploma". It's
principal purpose is to demonstrate my abilities and knowledge of working with and combining HTML, CSS, Javascript 
and Python languages, while working with the Django framework, a database and Stripe payments integration. The basic
layout, functionality and structure is based on Code Institute's ["Ado Boutique"](https://github.com/ckz8780/boutique_ado_v1)
Full Stack Frameworks With Django project.

## 1.1 What is Safe Face
Safe Face is a b2b (Business to Business) website that allows businesses to purchase protective face masks in a
straight forward manner.

## 1.2 Why will Users use it?
The site is constructed in such a way that navigating it feels natural and intuitive to the user. The categories
are laid out clearly with multiple routes to see the products contained within them. The products themselves are 
presented so as to allow users to make an informed decision about whether to purchase. Once that decision has 
been made, it is a straight forward process to select a quantity and then checkout using Stripe payments.


# 2 UI & Design
Back to Contents

Owing to the nature of the products being sold on the site, the design needs to create an instant sense of
trust with the user. This is done via a combination of colours, typography, imagery and by providing lots of space
without compromising on providing essential product information. 

## 2.1 Colour Pallete
The main blue colour used is the Pantone Colour of the Year 2020; "PANTONE 19-4052 Classic Blue".    https://www.pantone.com/eu/en/articles/color-of-the-year/color-of-the-year-2020
As the website is medical based, a colour that creates the perception of cleanliness is essential.
Blue does exactly this, with the shade chosen also instilling calmness, confidence and a sense
of connection. The secondary colours associated with the blue, reinforce this perception, with the
green in particular complimenting the the sterility of the blue, while the other colours enhance
the sense of calmness.

## 2.2 Fonts
Two fonts were chosen for this project, both taken from Google Fonts https://fonts.google.com/. 
- Open Sans was selected for content
- Oswald used for headings

Both were picked because of their regular use in medical websites. With 29% of all hospitals sites 
using Open Sans and 3% using Oswald, employing them here creates a sense of familiarity that builds 
trust with the user.
(https://www.ilovewp.com/resources/medical/wordpress-for-hospitals/most-used-google-fonts-on-hospital-websites/)

## 2.3 Imagery
So as to avoid clutter and thus maintain and sense of "cleanness", very limited imagery is
employed. This gives the site an opportunity to breath, so that the strong colours and fonts
come through. However, this means that where non-product imagery is used, it needs to very 
strongly reinforce the message of trust. For this reason, strong, trustworthy images of people
in masks are used. The images were sourced from:
- d 
- g 


# 3 Site Content
[Back to Contents](#Content)

## 3.1 Index
Blah Blah
- Wireframes
    -- Desktop
    -- Tablet
    -- Mobile

## 3.2 Category Pages

## 3.3 Product Pages

## 3.4 Shopping Cart  

## 3.5 Checkout 

## 3.6 Confirmation

## 3.7 Registration

## 3.8 Login

## 3.9 Profile

## 3.10 Log Out


# 4 Deployment

## 4.1 Github

## 4.2 Heroku


# 5 Testing

## 5.1 Testing link
The suite of test cases is contained in a separate file:

## 5.2 Known Bugs
1. Blah

## 5.3 Linting
Each piece of code was put through a "checker" to review the quality of the code.

### 5.3.1 HTML
- Website: https://validator.w3.org/nu/#textarea
- Result: All code passed, primarily with the exception of lines containing Jinja2 code. An repeated ID error was also ignored because the line of code is added dynamically and only one of the lines of code will be included.

### 5.3.2 CSS
- Website: https://jigsaw.w3.org/css-validator/validator
- Result: No errors or issues found

### 5.3.3 JavaScript
- Website: https://jslint.com/
- Result: Instances of "Double Quotes" ignored as a decision was made to use single quotes

### 5.3.4 Python
- Website: http://pep8online.com/
- Results: No errors or issues found


# 6 Technolgies & Third Party Plugins Employed
Back to Contents

## 6.2 Django:
The Django framework forms the backbone of the functional code and is used in conjunction with Python

## 6.3 Python:
As much as possible, functionality was created using Python.

## 6.4 Javascript:
Where functions could not be created in Python, Javascript was used. On occasion this also called for the use of JQuery. The latter is accessed bia CDN.

## 6.5 CSS:
The majority of styling of the HTML code is done with CSS, though certain Flask and Materialize code has it's own inbuilt styling.

## 6.6 HTML:
Basic site layout and structure is achieved with HTML. However, in conjunction with Flask, Jinja2 was extensively used: https://jinja.palletsprojects.com/en/2.11.x/.

## Fontawesome:
## JQuery:


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
    - Add username: CDolan1
    - Add email address: cdolan1@gizagig.com 
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

After restart from Github
pip3 install -r requirements.txt
pip3 freeze --local > requirements.txt  - after installing a new pip3?

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


Products Page - Add button for regular visitors who can update qty in cart.


Home Page Carousel - With Indicators: https://getbootstrap.com/docs/4.0/components/carousel/
Back to Top button - https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_scroll_to_top
Remove Number Input Default Arrows: https://www.w3schools.com/howto/howto_css_hide_arrow_number.asp
Image Gallery on Product_Info - https://gosnippets.com/snippets/bootstrap-4-ecommerce-preview-product-with-images
MArketing Banner Ticker Tape - https://bbbootstrap.com/snippets/bootstrap-scrolling-breaking-news-ticker-53214404
Preventing Users Manually putting in non-multiple numbers - http://jsfiddle.net/nottrobin/vN3xK/
Back Buttons - https://www.w3schools.com/JSREF/met_his_back.asp
Favicon - https://www.youtube.com/watch?v=kEf1xSwX5D8

# Interesting Bugs
- Cart "Update" Wouldn't work due to specificity
-- var form=$(this).prev('.updated-form');  became    var form = $(this).siblings("form"); solved by tutor support.

QUantity_input_script needed am else atatement to inc and dec from cart and product info pages. Also had to use https://www.w3schools.com/tags/att_data-.asp and item.product.id 


Issue with the Qty inpout field in Cart, I can add non-multiples. Known bug


http://jigsaw.w3.org/css-validator/validator