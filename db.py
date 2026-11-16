import mysql.connector as sql

class Database:
    def __init__(self):
        self.conn = sql.connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'root',
            password = 'Tushar@2000',
            database = "tb"
        )
        self.cursor = self.conn.cursor()
        print("Database connection established.")

        # step 1: create a database
        self.cursor.execute('''
        CREATE DATABASE IF NOT EXISTS tb''')

        # step 2: create any table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                            (user_id INT PRIMARY KEY,
                            name VARCHAR(255) NOT NULL,
                            email VARCHAR(255) NOT NULL UNIQUE,
                            pass  VARCHAR(255) NOT NULL)''')
        self.cursor.execute('''create table if not exists training_basket
                            (item_id INT PRIMARY KEY,
                            item_name VARCHAR(255) NOT NULL,
                            quantity INT NOT NULL)''')
obj = Database()
