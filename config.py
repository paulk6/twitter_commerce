import os

class Config():
    # environ.get will look at the environment variables and see if the SECRET_KEY is included. it will use that value if so.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
