import json

class provider:
    id = ""
    lat = ""
    lon = ""
    name = ""
    
    def __init__(self, id="", lat="",lon="",name=""):
        self.id = id
        self.lat = lat
        self.lon = lon
        self.name = name


    def get(self,id):
        data = {}
        data['id'] = self.id
        data['lat'] = self.lat
        data['lon'] = self.lon
        data['lat'] = self.lat
        data['name'] = self.name

        return "should return with id" +id
 
    def post(self):
        data = {}
        data['id'] = self.id
        data['lat'] = self.lat
        data['lon'] = self.lon
        data['lat'] = self.lat
        data['name'] = self.name

        return json.dumps(data)