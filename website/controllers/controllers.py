from model.connections import make_connection
from datetime import datetime

cursor = make_connection()


def find_messages():
    return cursor.find().sort("data", -1)


def insert_message(autor, message, email):

    inserir = {
        'author': autor,
        'message': message,
        'email': email,
        'data': datetime.now()
    }

    cursor.insert_one(inserir)
