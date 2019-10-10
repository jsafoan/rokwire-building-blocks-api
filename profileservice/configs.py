import os

from dotenv import load_dotenv

# Load .env file
load_dotenv()

# this has to be have the file path to the folder for saving image files and other necessary files from rest service
PROFILE_REST_STORAGE = os.getenv('REST_STORAGE', '/usr/src/app/rest')
MONGO_PROFILE_URL = os.getenv('MONGO_PROFILE_URL', 'localhost:27017')
MONGO_PII_URL = os.getenv('MONGO_PII_URL', 'localhost:27017')
FLASK_APP = os.getenv('FLASK_APP', 'profile_rest_service')
FLASK_ENV = os.getenv('FLASK_ENV', 'production')
PROFILE_ENDPOINT = os.getenv('PROFILE_ENDPOINT', '/profiles')

PROFILE_DB_NAME = 'profiledb'
PII_DB_NAME = 'piidb'
PROFILE_DB_PROFILE_COLL_NAME = 'NonPiiDataset'
PII_DB_PII_COLL_NAME = 'PiiDataset'
FIELD_OBJECTID = '_id'
FIELD_PROFILE_UUID = 'uuid'
FIELD_PID = 'pid'

GZIP_LEVEL = int(os.getenv('GZIP_LEVEL', '6'))
GZIP_MIN_SIZE = int(os.getenv('GZIP_MIN_SIZE', '102400'))