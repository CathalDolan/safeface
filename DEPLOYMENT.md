Go to www.heroku.com
If you don't already have an account, click "Sign Up for Free" and create one.
Once logged in, click "New" in top right hand corner
    - Select "Create New App" from dropdown
Give the app a name and choose region closest to you ande click "Create app"
YOu'll be brought to a new page. Click "Resources" along the top.
    - Under "Add-ons" type "post" and select "Heroku Postgres" from options
    - Select the free (or any) plan and click "Submit Order Form"
Return to GitPod (or whatever IDE you're working on)
    - Install dj database
        - pip3 install dj_database_url
    - Install psycopg2
        - pip3 install psycopg2-binary
    - Free the requirements
        - pip3 freeze > requirements.txt
Set Up the Shop's database
    - Go to project settings.py
        - import dj_database_url
    - Scroll to "DATABASES"
        - Comment out existing sql lite database code
        - Create a new one initially with:
            DATABASES = {
                'default': dj_database_url.parse()
            }
    - Return to Heroku and click the "Settings" tab
        - Scroll to "Config Vars" and click the "Reveal Config Vars" button
        - Copy the DATABASE_URL postgres code from the field on the right
    - Back in Project settings in the IDE
        - Put a pair of single quotes between the brackets after "parse()"
        - Paste the code copied from Heroku between the quotes
    - SAVE
    - Run migrations from teh cli:
        - python3 manage.py migrate
    - Load the categories from the cli (if in fixtures):
        - python3 manage.py loaddata categories
    - Load the categories from the cli (if in fixtures):
        - python3 manage.py loaddata categories

