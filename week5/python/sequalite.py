import requests
import json
import sqlite3
from faker import Faker
from time import time

def get_jokes(n):
    for i in range(n):
        print(i + 1)
        url = 'https://api.chucknorris.io/jokes/random'
        data = requests.get(url)
        data = data.json()
        joke = data['value']
        joke = joke.replace("'", "")
        connection = sqlite3.connect('jokes.db')  #Make a connection to the database
        cursor = connection.cursor() #Think of the cursor as the place that executes queries
        create_table = f"CREATE TABLE IF NOT EXISTS jokes (joke text NOT NULL);"
        cursor.execute(create_table)
        query = f"INSERT INTO jokes (joke) VALUES ('{joke}');"
        cursor.execute(query)  #Cursor runs the query
        connection.commit()  #Finalize the result. "Write" it to the DB
        # results = cursor.fetchall() #Fetch theh results back from the cursor into python variable
        connection.close()  #Close the connection

def read_jokes():
    connection = sqlite3.connect('jokes.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM jokes;")
    connection.commit()
    results = cursor.fetchall()
    connection.close

    for result in results:
        print(result)

# read_jokes()

def gen_fake_data(n):
    start = time()
    f = Faker()
    connection = sqlite3.connect('jokes.db')  #Make a connection to the database
    cursor = connection.cursor() #Think of the cursor as the place that executes queries
    for i in range(n):
        print(i + 1)
        name = f.name()
        query = f"INSERT INTO jokes (joke) VALUES ('{name}');"
        cursor.execute(query)  #Cursor runs the query
    connection.commit()  #Finalize the result. "Write" it to the DB
    connection.close()
    end = time()
    print(f"The function ran in {round(end-start,2)}s")

gen_fake_data(5)
read_jokes()