
from flask import Flask, request
from provider import provider
from settings import Config

app = Flask(__name__)
app.config.from_object(Config)


#Create new Provider
@app.route('/providers', methods=['GET'])
def GetProviders():
    if request.method == 'GET':
        p =  provider()
        return(p.getProviders())

#Create new Provider
@app.route('/createNewProvider', methods=['POST'])
def CreateNewProvider():
    if request.method == 'POST':
        p =  provider("",request.args.get('lat'), request.args.get('lon'),request.args.get('name'))
        return(p.createNewProvider())

#Get a new provider or change configuration from a privider
@app.route('/provider', methods=['GET','POST'])
def GetChangeProvider():
    if request.method == 'POST': #Change Provider
        p =  provider(request.args.get('_id'),request.args.get('lat'), request.args.get('lon'),request.args.get('name'))
        return(p.postProvider())
    else: # Get Provider
        p =  provider()
        return p.getProvider(request.args.get('_id')) 

#Delete Provider
@app.route('/deleteProvider', methods=['DELETE'])
def DeleteProvider():
    if request.method == 'DELETE':
        p =  provider()
        return(p.DeleteProvider(request.args.get('_id')))




if __name__ == '__main__':
    app.run()