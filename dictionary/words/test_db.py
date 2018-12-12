#! /Users/jodth07/Env/dreamers/bin/python
import psycopg2
from Application import db
# from .Application.dictionary.models import Dictionary
# from .Application.user.models import User
from Application.user.models import User
from Application.dictionary.models import Dictionary
from datetime import datetime

# 'postgresql://jodth07:Jd25390725@localhost/dasa'

hostname = 'localhost'
username = 'jodth07'
password = 'Jd25390725'
database = 'dasa'

myConn = psycopg2.connect(database=database, user=username, password=password, host=hostname)
cur = myConn.cursor()

cur.execute("SELECT other_names FROM dictionary WHERE ID=100003")

for item in cur.fetchall():
    print(item)
# def connect(conn)

# word = Dictionary.query.filter_by(id=100003)

# print(word.other_names)