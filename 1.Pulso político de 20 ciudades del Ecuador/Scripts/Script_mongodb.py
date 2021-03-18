#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pymongo
import pprint
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


# In[2]:


###API ########################
ckey = "tIaMOe2pYntmwLT3JLU89ETW7"
csecret = "qzIWvghjvQx9THMMxGQ3TdG2amAhPqLUu8ra3G9BTwH3J8N776"
atoken = "1110505230498705408-2iPeM8DRO3R5yec1OH51WIEI6j7j3Z"
asecret = "mkHAf4xlJmY4uOfYkzw0MwKP8zeIzU0ZYLz2TfKUwCCp6"
#####################################


# In[3]:


class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = mycol.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())


# In[4]:


'MONGODB'
myclient = pymongo.MongoClient("mongodb://localhost:27017")  
try:
    mydb=myclient["ciudades"]
    mycol=mydb["ambato"]
except:
    mydb=myclient["ciudades"]
    mycol=mydb["ambato"]


# In[ ]:


twitterStream.filter(track=['Ecuador','Ambato','Pulso Politico','Elecciones 2021','Lasso','Arauz'])


# In[ ]:




