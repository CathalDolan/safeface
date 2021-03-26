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
    - Add on line 1: web: gunicorn safe-face.wsgi:application
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
    - 5.7.2 - Set Debug to True only if in Development environment:
        - DEBUG = 'DEVELOPMENT' in os.environ
    - 5.7.3 - Save, Add, Commit and Push to Github

# 6 Connect to AWS - Bucket
- 6.1 - Login to www.aws.amazon.com
    - 6.1.1 - If required, create and account from teh button in the top right
- 6.2 - Log into the AWS Management Console
- 6.3 - Locate and navigate to "S3" page
    - 6.3.1 - Click "Create Bucket"
    - 6.3.2 - Name the bucket, safe-face
    - 6.3.3 - Choose region closest to you
    - 6.3.4 - Uncheck "Block all Public Access" and acknowledge that the bucket will be public
    - 6.3.5 - Click "Create Bucket"
    - 6.3.6 - You'll be brought to the dash
- 6.4 - Set Bucket Settings - Properties
    - 6.4.1 - From the dash click on the bucket name to open into
    - 6.4.2 - Click the "Properties Tab and scroll to "Static website hosting" and click "Edit"
    - 6.4.3 - Click > "enable", the "Host a static website"
    - 6.4.4 - Add "index.html" and "error.html"
    - 6.4.5 - Click "Save Changes"
- 6.5 - Set Bucket Settings - Permissions
    - 6.5.1 - Select "Permissions" tab
    - 6.5.2 - Scroll to "Cross-origin resource sharing (CORS)" section and click "Edit"
    - 6.5.3 - Paste in the config as below or copy from https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/cors.html
        ```
        [
            {
                "AllowedHeaders": [
                    "Authorization"
                ],
                "AllowedMethods": [
                    "HEAD",
                    "GET",
                    "PUT",
                    "POST",
                    "DELETE"
                ],
                "AllowedOrigins": [
                    "*"
                ],
                "ExposeHeaders": [
                    "ETag",
                    "x-amz-meta-custom-header"]
            }
        ]
        ```
    - 6.5.4 - Click "Save Change"
    - 6.5.5 - Go to "Bucket Policy" section and click "Edit"
    - 6.5.6 - Click "Policy Generator" button. This opens a new tab
    - 6.5.7 - Complete generator:
        - Type = S3 Bucket Policy
        - Effect = Allow
        - Principal = *
        - AWS Service = Amazon S3 
        - Actions = GetObject
    - 6.5.8 - Go back to original window and copy the "Bucket ARN" code
    - 6.5.9 - Return to the policy genberator page and paste it into the ARN field
    - 6.5.10 - CLick, "Add Statement", then "Generate Policy" then copy the Json code that displays
    - 6.5.11 - Paste it into the Policy editor section on the original page
    - 6.5.12 - Add a /* onto the end of the resource key
    - 6.5.13 - Click "Save Changes" button
    - 6.5.14 - Scroll to "Access control list (ACL)" section and click "Edit"
    - 6.5.15 - In the "Everyone (public access)" section check the "List" option in teh "Objects" column
    - 6.5.16 - Confirm permission and click "Save Changes"
# 7 Connect to AWS - Groups, Policies & Users
    - 7.1 - Click the "Services" Dropdown (top left)
    - 7.2 - Find the "Security, Identity & Compliane" section and click "IAM" "IAM"
    - 7.3 - Create a Group
        - 7.3.1 - Select "Groups" from the left side menu
        - 7.3.2 - Click "Create New Group"
        - 7.3.3 - Name the group and click "Next Step"
        - 7.3.4 - Skip "Policy" by clicking "Next Step" again
        - 7.3.5 - On "Review" click "Create Group" button
    - 7.2 - Create a Policy
        - 7.2.1 - Click "Policies" from the left side menu and then the "Create Policy" button
        - 7.2.2 - Select the "Json" tab and click "Import managed policy" link. Opens a modal.
        - 7.2.3 - Search for "S3" and choose "AmazonS3FullAccess" document and click "Import" button
        - 7.2.4 - Click "Services" tab again, find "S3" and right click to open it in a new window
        - 7.2.5 - Got to the "Properties" tab and copy ARN number used before
        - 7.2.6 - Paste it into the policy twice in "Resource", replacing the * putting in a list and adding \* to the second one
        ```
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": "s3:*",
                    "Resource": [
                        "arn:aws:s3:::safe-face",
                        "arn:aws:s3:::safe-face/*"
                    ]
                }
            ]
        }
        ```
        - 7.2.7 - Click "Next Tags" button, then "Next Review" button
        - 7.2.8 - Add a name and description and click "Create Policy" button
            - safe-face-policy
            - Access to S3 bucket for Safe Face static file
        - 7.2.9 - Click Groups again from left side menu and click the group name to open it
        - 7.2.10 - Under "Permissions" tab click "Attach Policy", opens a new viewed
        - 7.2.11 - Search for the policy name just created
        - 7.2.12 - Select it and click "Attach Policy"
    - 7.3 - Create a User
        - 7.3.1 - Click "Users" from the left side menu
        - 7.3.2 - Click "Add User" button
        - 7.3.3 - Give the User a name
            - safe-face-staticfiles-user
        - 7.3.4 - Check "Programmatic access" and click "Next: Permissions"
        - 7.3.5 - On the next page check the group we created and click "Next: Tags" button
        - 7.3.6 - Click "Next" button on next paghe, and "Create User" on the one following that
        - 7.3.7 - A "Success" notification will display
        - 7.3.8 - From the notification, click "Download .csv"
        - 7.3.9 - SAVE THIS FILE - DON'T LOSE IT!
# 8 Connect to Django
    - 8.1 - Install packages:
        - pip3 install boto3
        - pip3 install django-storages
    - 8.2 - Freeze them:
        - pip3 freeze > requirements.txt
    - 8.3 - Add to installed apps in project settings.py
        - add 'storages', to INSTALLED_APPS
    - 8.4 - In settings.py, below MEDIA_ROOT add:
    ```
    if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'safe-face'
    AWS_S3_REGION_NAME = 'eu-west-1' (set to region selected in AWS bucket)
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    ```
    - 8.5 - Navigate to Heroku to add AWS variables
        - 8.5.1 - Open "Settings" tab and navigate to "Config Vars"
        - 8.5.2 - Click "Reveal Config Vars"
        - 8.5.3 - Create Key - Value pairs using the keys in teh .csv file downloaded previously
            - AWS_ACCESS_KEY_ID = "Access key ID"
            - AWS_SECRET_ACCESS_KEY = "Secret access key"
        - 8.5.4 - Add the key "USE_AWS" and value "True" pair
        - 8.5.5 - Click "Add" after each one
        - 8.5.6 - Remove the "DISABLE_COLLECTSTATIC" pairs by clicking the X and confirming
    - 8.6 - Return to settings.py
        - 8.6.1 - In AWS bucket configuration, add to existing list (at the end )
            - AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    - 8.7 - Create a new file at project level: custom_storage.py
        - 8.7.1 - Import packages at the top of the page:
            - from django.conf import settings 
            - from storages.backends.s3boto3 import S3Boto3Storage
        - 8.7.2 - Create custom classes:
            ```
            class StaticStorage(S3Boto3Storage):
                location = settings.STATICFILES_LOCATION

            class MediaStorage(S3Boto3Storage):
                location = settings.MEDIAFILES_LOCATION
            ``
        - 8.7.3 - Return to settings.py and create static and media files:
            ```
            # Static and media files
            STATICFILES_STORAGE = 'custom_storages.StaticStorage'
            STATICFILES_LOCATION = 'static'
            DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
            MEDIAFILES_LOCATION = 'media'
            ```
        - 8.7.4 - Still in settings.py, add overrides
            ```
            # Override static and media URLs in production
            STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
            MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
            ```
# 9 Long Term Static File Caching
    9.1 - In settings.py scroll to if 'USE_AWS in...' section and at the top insert
        ```
        # Cache control
        AWS_S3_OBJECT_PARAMETERS = {
            'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
            'CacheControl': 'max-age=94608000',
        }
        ```
    9.2 - Add, Commit, Push
# 10 Set up "Media" in S3
    - 10.1 - Go to AWS dashboard 
    - 10.2 - Click "Objects" tab followed by "Create Folder" button
    - 10.3 - Give it a name "media" and click "Create Folder" button
    - 10.4 - Click on the new folder name and hit the "Upload" button
    - 10.5 - Drag and drop images and/or other media into the folder
    - 10.6 - Click on "Additional Upload Options"
    - 10.7 - Scroll to "Access Control List" and check the "Read" option for "Everyone (public access)"
    - 10.8 - Accept the conditions and click "Upload"
# 11 Add Stripe Keys to Heroku and Create new Endpoint
    - 11.1 - Log into Stripe and click Developers then API Keys
    - 11.2 - Copy the keys and navigate to Heroku and click the "Settings" tab
    - 11.3 - Scroll to "Config Vars" section and click "Reveal Config Vars"
        - 11.3.1 - Add the key value pairs:
            - STRIPE_PUBLIC_KEY = paste in copied key value
            - STRIPE_SECRET_KEY = paste in copied key value
    - 11.4 - Return to Stripe and click "Webhooks" from left side menu
        - 11.4.1 - Click the "+ Add endpoint" button in top right
        - 11.4.2 - Add the endpoint url:
            - https://safe-face.herokuapp.com/checkout/wh
        - 11.4.3 - Click "Receive all event" link
        - 11.4.4 - Click "Add Endpoint" button
        - 11.4.5 - On displayed page, scroll to "Signing secret" and reveal it
        - 11.4.6 - Copy the secret and return to Keroku > Settings > Config Vars
        - 11.4.7 - Add the new secret as a key value pair
            - STRIPE_WH_SECRET - copied key value