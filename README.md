![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

After restart from Github
pip3 install -r requirements.txt
pip3 freeze --local > requirements.txt  - after installing a new pip3?

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


# 1 Introduction
Back to Contents

Safe Face is my fourth milestone project for the Code Institute "Full Stack Software Development Diploma". It's
principal purpose is to demonstrate my abilities and knowledge of working with and combining HTML, CSS, Javascript 
and Python languages, while working with the Django framework, a database and Stripe payments integration.

## 1.1 What is Safe Face
Safe Face is a b2b website that allows businesses to purchase protective face masks in a straight forward manner.

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
Back to Contents

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

Products Page - Add button for regular visitors who can update qty in cart.


Home Page Carousel - With Indicators: https://getbootstrap.com/docs/4.0/components/carousel/
Back to Top button - https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_scroll_to_top
Remove Number Input Default Arrows: https://www.w3schools.com/howto/howto_css_hide_arrow_number.asp
Image Gallery on Product_Info - https://gosnippets.com/snippets/bootstrap-4-ecommerce-preview-product-with-images
MArketing Banner Ticker Tape - https://bbbootstrap.com/snippets/bootstrap-scrolling-breaking-news-ticker-53214404
Preventing Users Manually putting in non-multiple numbers - http://jsfiddle.net/nottrobin/vN3xK/
Back Buttons - https://www.w3schools.com/JSREF/met_his_back.asp

# Interesting Bugs
- Cart "Update" Wouldn't work due to specificity
-- var form=$(this).prev('.updated-form');  became    var form = $(this).siblings("form"); solved by tutor support.

QUantity_input_script needed am else atatement to inc and dec from cart and product info pages. Also had to use https://www.w3schools.com/tags/att_data-.asp and item.product.id 


# Integrating Stripe

Core logic/payment flow for this comes from here:
    - https://stripe.com/docs/payments/accept-a-payment
CSS from here: 
    - https://stripe.com/docs/stripe-js

1. - Stripe.com
    - Create an account
2. - https://stripe.com/docs/payments/accept-a-payment
    - Custom Payment Flow
    - Number 3: Collect Card Details - Set up Stripe elements
    - Copy the script and paste into {% block corejs %} in base.html
3. Go to Chedckout.html
    - Add postload js block and include block.super
        {% block postloadjs %}
            {{ block.super }}
        {% endblock %}
    - Add client secret and public key Json scripts
        {{ stripe_public_key|json_script:"id_stripe_public_key" }}
        {{ client_secret|json_script:"id_client_secret" }}
        <script src="{% static 'checkout/js/stripe_elements.js' %}"></script>
    - Add the public key
        - Copy the publishable key from the dashboard (image)
        - Add it to Checkout Views Context (image)
    - Create new folder, js, in static on same level as css folder
        - Create file, stripe_elements.js
4. Add vars to stripe_elements.js (slice the ends to remove quotation marks)
    - var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
    - var clientSecret = $('#id_client_secret').text().slice(1, -1);
5. Add additional vars to stripe_elements.js
    - Public key var
        var stripe = Stripe(stripePublicKey);
    - Use it to create an instance of Stripe elements
        var elements = stripe.elements();
    - Use that to create a card element
        var card = elements.create('card', {style: style});
    - Mount the card to the card-element id
        card.mount('#card-element');
    - Image
6. Add JS inline styling
    - Copy basic styles from Stripe: https://stripe.com/docs/payments/integration-builder (image)
    - Insert into stripe_element.js above card var and card.mount
        - Make changes as required
        - Add style to the card.var (image12)
7. Add Stripe default CSS to Checkout.css
    /* Stripe Components */
    .StripeElement,
    .stripe-style-input {
    box-sizing: border-box;
    height: 40px;
    padding: 10px 12px;
    border: 1px solid transparent;
    border-radius: 0px;
    background-color: white;
    box-shadow: 0 1px 3px 0 #e6ebf1;
    -webkit-transition: box-shadow 150ms ease;
    transition: box-shadow 150ms ease;
    }

    .StripeElement--focus,
    .stripe-style-input:focus,
    .stripe-style-input:active {
    box-shadow: 0 1px 3px 0 #cfd7df;
    }

    .StripeElement--invalid {
        border-color: orange;
    }

    .StripeElement--webkit-autofill {
    background-color: #fefde5 !important;
    }

    .stripe-style-input::placeholder {
        color: #aab7c4;
    }
8. Take advantage of Stripe Style input class
    - Add stripe style input to all relevant fields in forms.py (image)
    - Add the class to the checkout css (image 12)
9. Add the JS to the checkout html within block postloadjs
    - <script src="{% static 'checkout/js/stripe_elements.js' %}"></script>
10. Include the input in Checkout.html
    - <input type="hidden" value="{{ client_secret }}" name="client_secret"> (image 11)
11. Add a listener for card errors in Stripe_elements.js (image 13)
    card.addEventListener('change', function (event) {
        var errorDiv = document.getElementById('card-errors');
        if (event.error) {
            var html = `
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>${event.error.message}</span>
            `;
            $(errorDiv).html(html);
        } else {
            errorDiv.textContent = '';
        }
    });
12. Provide total cost and amount to be charged to Stripe via Checkout Views
    - Import cart_contents from the cart contexts 
        from cart.contexts import cart_contents
    - Inject the data into the checkout function and calculate total (image 14)
        current_cart = cart_contents(request)
        total = current_cart['gross_total']
        stripe_total = round(total * 100)
13. Install Stripe
    - pip3 install stripe
    - Import into views beneath cart_contents
        import stripe
    - Also import settings just below messages
        from django.conf import settings
14. Add stripe reqs to settings.py inclu currency and key access
    - STRIPE_CURRENCY = 'eur'
    - STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
    - STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
15. Export the keys using the cli
    - On Stripe dash copy the "publishable key"
    - In cli: export STRIPE_PUBLIC_KEY=copied code
    - On Stripe dash copy the "secret key"
    - In cli: export STRIPE_SECRET_KEY=copied code
    - Images 15 & 16
    - Each time the workspace is restarted this must be repeated.
    - export STRIPE_WH_SECRET=copied code
16 . Create Payment Intent in Checkout Views
    - Add the keys at the top of teh function:
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY
    - Set the secret key on stripe
        stripe.api_key = stripe_secret_key
    - Create the payment Intent
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
    - Image 17
17 . Update Context and add key warning
    - In Context:
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    - Warning to alert us if we forget to set public key
        if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')
        template = 'checkout/checkout.html'
    - Image 18
18 . Add event listener to...
    - From https://stripe.com/docs/payments/accept-a-payment?ui=elements go to section 4 and copy the client.js (image 19)
    - Paste into stripe_elements.js
    - Prevent multiple submissions. Add code to the Stripe code:
        card.updated({ 'disabled': true});
        $('#submit-button').attr('disabled', true);
    - Inject the error message into the card error div:
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${result.error.message}</span>
        `;
        $(errorDiv).html(html);
    - Insert form submission method:
        form.onsubmit();
    - Add error var:
        var errorDiv = document.getElementById('card-errors');
    - If there's an error Re-enable the card element and submit button:
        card.updated({ 'disabled': false});
        $('#submit-button').attr('disabled', false);
    - If no error submit the form:
        if (result.paymentIntent.status === 'succeeded') {
            form.submit();
        }
    - Image 20
