from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
SERVICE_URL = 'https://gorest.co.in/public/v1/users'
CONNECTION_ROW = 'postgressql://'

Model = declarative_base(name='Model')

engine = create_engine()