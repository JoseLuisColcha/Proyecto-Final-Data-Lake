from facebook_scraper import get_posts
import pymongo
import json
import time

myclient = pymongo.MongoClient("mongodb://localhost:27017") 

try:
    mydb=myclient['noticias_mundo']
    mycol=mydb['elmundo']
except:
    mydb=myclient['noticias_mundo']
    mycol=mydb['elmundo']
    
i=1
for post in get_posts('elmundo', pages=100000, extra_info=True):
    print(i)
    i=i+1
    time.sleep(5)
    
    id=post['post_id']
    doc={}
     
    doc['id']=id
    
    mydate=post['time']
    
    try:
        doc['texto']=post['text']
       

        doc['post_url']=post['post_url']
        mycol.save(doc)

    
        print("guardado exitosamente")

    except Exception as e:    
        print("no se pudo grabar:" + str(e))    

