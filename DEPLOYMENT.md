Deployment is done in two stages, the first to Heroku, the second to AWS (AMazon Web Services)

# 1. Go to www.heroku.com
If you don't already have an account, click "Sign Up for Free" and create one.

- 1.1 Once logged in, click "New" in top right hand corner
    1.1.1 - Select "Create New App" from dropdown
- 1.2. Give the app a name and choose region closest to you ande click "Create app"
- 1.3. You'll be brought to a new page. Click "Resources" along the top.
    - 1.3.1 - Under "Add-ons" type "post" and select "Heroku Postgres" from options
    - 1.3.2 - Select the free (or any) plan and click "Submit Order Form"
- 1.4. Return to GitPod (or whatever IDE you're working on)
    - 1.4.1 - Install dj database
        - pip3 install dj_database_url
    - 1.4.2 - Install psycopg2
        - pip3 install psycopg2-binary
    - 1.4.3 - Free the requirements
        - pip3 freeze > requirements.txt
# 2. Set Up the Shop's database
- 2.1 - Go to project settings.py
    - import dj_database_url
- 2.2 - Scroll to "DATABASES"
- 2.3 - Comment out existing sql lite database code
- 2.4 - Create a new one initially with:
        DATABASES = {
            'default': dj_database_url.parse()
        }
- 2.5 - Return to Heroku and click the "Settings" tab
    - 2.5.1 - Scroll to "Config Vars" and click the "Reveal Config Vars" button
    - 2.5.2 - Copy the DATABASE_URL postgres code from the field on the right
- 2.6 - Back in Project settings in the IDE
    - 2.6.1 - Put a pair of single quotes between the brackets after "parse()"
    - 2.6.2 - Paste the code copied from Heroku between the quotes
- 2.7 - SAVE
- 2.8 - Run migrations from the cli:
    - python3 manage.py migrate
- 2.9 - Load the categories from the cli (if in fixtures):
    - python3 manage.py loaddata categories
- 2.10 - Load the categories from the cli (if in fixtures):
    - python3 manage.py loaddata categories
- 2.11 - Return to Project Settings
    - 2.11.1 - Add an if statement to allow the front end to work locally or when viewed through Heroku deployment
        ```
        if 'DATABASE_URL' in os.environ:
            DATABASES = {
                'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
            }
        else:
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                }
            }
        ```
- 2.12 - Install Gunicorn via cli
    - pip3 install gunicorn
    - pip3 freeze > requirements.txt
- 2.13 - Create a Procfile
    - Create a new project level file "Procfile"
    - Add on line 1: web: gunicorn boutique_ado.wsgi:application
- 2.14 - Login to Heroku via the cli
    - heroku login -i
    - Add email
    - Add password
- 2.15 - Prevent Heroku from collecting static files
    - heroku config:set DISABLE_COLLECTSTATIC=1 --app safe-face
- 2.16 - Add Heroku and local host to Settings.py ALLOWED_HOSTS
    - ALLOWED_HOSTS = ['safe-face.herokuapp.com', 'localhost']

# 3. Initial Deploy to Heroku
    - git add .
    - git commit -m "reason for commit"
    - git push origin [branch_name]
    - git push heroku master
    - If an error displays regarding heroku not being a recognised repo add below then try above again.
        heroku git:remote -a [project name on heroku]

# 4. Automatic Deploy
Set up so that whenever we push to Github, the code automatically deploys to Heroku
- 4.1 - Go to Heroku and click the "Deploy" tab 
    - 4.1.1 - Go to "Deployment Method" section
        - Click "GitHub" 
        - Ensure you are on teh correct repo
        - Add the project name as saved in Github and click "Search"
        - Select the correct repo
        - Click "Connect"
    - 4.1.2 - Scroll to "Automatic Deploys"
        - Click "Enable Automatic Deploys"

# 5 Set Secret Key
- 5.1 - Generate a secret Key
    - https://miniwebtool.com/django-secret-key-generator/
    - Copy the Key
- 5.2 - Go to Heroku and click teh settings tab
- 5.3 - Scroll to "Config Vars" and click "Reveal Config Vars"
- 5.4 - Add "SECRET_KEY" as the key
- 5.5 - Paste in teh copied secret key as the value
- 5.6 - Click "Add"
- 5.7 - Go to projedct settings.py
    - 5.7.1 - Go to secret key and replace existing key with:
        - SECRET_KEY = os.environ.get('SECRET_KEY', '')
