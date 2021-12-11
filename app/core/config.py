from environs import Env

env = Env()
env.read_env()
PROJECT_NAME = env.str('PROJECT_NAME', "FastAPI example application")
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
API_V1_STR = "/api"
