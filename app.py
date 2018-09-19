
from flask import Flask, request
from provider import provider

app = Flask(__name__)

#Create new Provider
@app.route('/createNewProvider', methods=['POST'])
def CreateNewProvider():
    if request.method == 'POST':
        p =  provider(request.args.get('id'),request.args.get('lat'), request.args.get('lon'),request.args.get('name'))
        return(p.id)

#Get a new provider or change configuration from a privider
@app.route('/provider', methods=['GET','POST'])
def GetChangeProvider():
    if request.method == 'POST': #Change Provider
        p =  provider(request.args.get('id'),request.args.get('lat'), request.args.get('lon'),request.args.get('name'))
        return(p.post())
    else: # Get Provider
        p =  provider()
        return p.get(request.args.get('id')) 



if __name__ == '__main__':
    app.run()