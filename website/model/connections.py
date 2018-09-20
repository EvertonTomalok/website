from pymongo import MongoClient


def make_connection():
    """
    Create a connection with BigData.
    :return: cursor "empresas" and "contatos"
    """
    client = MongoClient()
    db = client.web

    mensagens = db.mensagens

    return mensagens
