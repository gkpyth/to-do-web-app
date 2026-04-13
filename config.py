import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    # Secret key for session security - checks environment variable first, falls back to dev key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'

    # Database location - SQLite file stored in the instance folder
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance', 'to-do.db')

    # Disable modification tracking - saves memory, not needed
    SQLALCHEMY_TRACK_MODIFICATIONS = False