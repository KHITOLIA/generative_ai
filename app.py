from flask import Flask
from db import Database

app = Flask(__name__)

obj = Database()
