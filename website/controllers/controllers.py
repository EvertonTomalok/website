from model.connections import make_connection
from bson.objectid import ObjectId
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


def delete_message_by_id(_id):
    cursor.delete_one({'_id': ObjectId(_id)})
