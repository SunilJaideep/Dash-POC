import sqlalchemy

url = 'postgresql+psycopg2://postgres:admin@127.0.0.1:5432/dash_assignment'
engine = sqlalchemy.create_engine(url)