# DiabetesAPI
API for diabetes management system using Python-Django.

##Django applications on Heroku
1. Set up a virtual environment
    pip install virtualenv
    virtualenv venv
    venv\Scripts\activate
    source venv/bin/activate

2. Declare app dependencies
    pip freeze > requirements.txt

3. Build your app and run it locally
    pip install -r requirements.txt

4. Running the application locally
    heroku local web

5. Deploy your application to Heroku
    $ git add .
    $ git commit -m "Added a Procfile."
    $ heroku login
    $ heroku create
    $ git push heroku master
