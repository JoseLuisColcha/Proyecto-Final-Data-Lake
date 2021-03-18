#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
from argparse import ArgumentParser
import requests
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
import couchdb


# In[2]:


try:
    client = MongoClient('localhost')
    print (client.list_database_names())
    clientatl = MongoClient('mongodb+srv://preyectofinal:1234@cluster0.3zh62.mongodb.net/ciudades?retryWrites=true&w=majority')
    print (clientatl.list_database_names())
except requests.ConnectionError as e:
    raise e


# In[3]:


#insert_many()
db = client['ciudades']
col = db['loja']
dbatl = clientatl['ciudades']
colatl = dbatl['loja']

for doc in col.find({}):
 print(doc)
 

for doc in col.find({}):
 colatl.insert_one(doc)
 print(doc)

for doc in colatl.find({}):
 print(doc)


# In[ ]:




