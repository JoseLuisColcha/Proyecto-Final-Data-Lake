import couchdb
import pymongo

couch_server=couchdb.Server()
couch_server.resource.credentials=('Jose Luis Colcha','1723547624')
couch_db = couch_server['provincias']

mongo_client = pymongo.MongoClient("mongodb+srv://esfot:esfot@cluster0.cyxcn.mongodb.net/freefire?retryWrites=true&w=majority")
mongo_client_db = mongo_client.get_database('provincia_pulso_politico')

for row in couch_db.view('_all_docs', include_docs=True):
    print(row['doc'])
    if mongo_client_db.provincia_pulso_politico.count_documents({"_id":row['doc']['_id']})==0:
        mongo_client_db.provincia_pulso_politico.insert(row['doc'])

        