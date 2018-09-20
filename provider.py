import json
import os
from pymongo import MongoClient
from bson.objectid import ObjectId

class provider:
    _id = ""
    lat = int()
    lon = int()
    name = ""

    mydb = ""
    
    def __init__(self, _id="", lat="",lon="",name=""):
        self._id = _id
        self.lat = lat
        self.lon = lon
        self.name = name

    def stringfy(self):
        data = {}
        data['_id'] = self._id
        data['lat'] = self.lat
        data['lon'] = self.lon
        data['name'] = self.name
        return (data)
    
    def connectDB(self):
        myclient = MongoClient(os.environ['DATABASE_URL'])
        self.mydb = myclient[os.environ['DATABASE']]

    def getProviders(self):
        self.connectDB()
        providers = self.mydb.providers.find()
        data = []
        for p in providers:
            p['_id'] = str(p['_id'])
            data.append(p)

        return json.dumps({'success':True,'data':data}), 200, {'ContentType':'application/json'} 

    def getProvider(self,_id):
        self.connectDB()
        p = self.mydb.providers.find_one({"_id":  ObjectId(_id)})
        self._id = str(p['_id'])
        self.lat = p['lat']
        self.lon = p['lon']
        self.name = p['name']
        return json.dumps({'success':True,'data':self.stringfy()}), 200, {'ContentType':'application/json'} 
 
    def postProvider(self):
        self.connectDB()
        data = {}
        data['lat'] = self.lat
        data['lon'] = self.lon
        data['name'] = self.name
        self.mydb.providers.update_one({'_id':ObjectId(self._id)},{'$set': data})
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

    def createNewProvider(self):
        self.connectDB()
        data = {}
        data['lat'] = self.lat
        data['lon'] = self.lon
        data['name'] = self.name
        post_id = self.mydb.providers.insert_one(data).inserted_id
        return json.dumps({'success':True,'id':str(post_id)}), 200, {'ContentType':'application/json'} 

    def DeleteProvider(self,_id):
        self.connectDB()
        self.mydb.providers.delete_one({"_id":  ObjectId(_id)})
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
    
