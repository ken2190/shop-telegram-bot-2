import psycopg2

from data.config import DB_URI

connect = psycopg2.connect(DB_URI)
cursor = connect.cursor()