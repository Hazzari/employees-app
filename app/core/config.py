from environs import Env

env = Env()
env.read_env()
PROJECT_NAME = env.str('PROJECT_NAME', "FastAPI example application")
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', 'localhost')
API_V1_STR = "/api"
MONGO_HOST = env.str('MONGO_HOST', 'localhost')
MONGO_PORT = env.str('MONGO_PORT', '27017')

MONGO_DB_URL = f'mongodb://{MONGO_HOST}:{MONGO_PORT}/'
