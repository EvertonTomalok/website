from pymongo import MongoClient


def make_connection():
    """
    Create a connection with BigData.
    :return: cursor "empresas" and "contatos"
    """
    client = MongoClient(
        "mongodb://r4mp3r4dm-henriqueM:n647GKg30M7QTzzI@bigdatadb-shard-00-00-ppgoo.mongodb.net:27017,bigdatadb-shard-00-01-ppgoo.mongodb.net:27017,bigdatadb-shard-00-02-ppgoo.mongodb.net:27017/test?ssl=true&replicaSet=BigDataDB-shard-0&authSource=admin")

    db = client.bigdata

    empresas = db.empresas
    contatos = db.contatos

    return empresas, contatos
