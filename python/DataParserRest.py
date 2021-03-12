from flask import json
from Key_Values import parseKeyValueFile
import flask
from flask import Flask , jsonify, render_template
from flask.globals import request
from flask_restful import Resource, Api 
from flask_cors import CORS


app = Flask(__name__)
api = Api(app)
CORS(app)
cors = CORS(app, resources={
    r"/*": {
        "origins": "http://localhost:8080/"
    }
})



class HeaderDictAPI(Resource):
    def __init__(self, hdict):
        self.__headerDict = hdict

    def get(self):
        return{'header' : self.__headerDict}


class FooterDictAPI(Resource):
    def __init__(self, fdict):
        self.__footerDict = fdict
    def get(self):
        return{'footer': self.__footerDict}

class DataListAPI(Resource):
    def __init__(self, dlist):
        self.dataList = dlist
    def get(self):
        channelList =  []
        for item in self.dataList:
            channelList.append(item.title())
        return jsonify({"channels": channelList})

class DataChannelAPI(Resource):
    def __init__(self, dlist):
        self.dataList = dlist
    def get(self):
        # extract index from request
        index = 0
        data = []
        for items in self.dataList:
            data.append(items.title())
        # check index for range

        #return datachannel
        return jsonify({"channel": data[index]})



    
    
def main():

    # create the variables
    headerDict = {}
    footerDict = {}
    dataList = []
    headerDict, footerDict, dataList = parseKeyValueFile('text_2DateiÖffnen.csv')

    api.add_resource(HeaderDictAPI, '/api/v1/csv/header', resource_class_kwargs={'hdict':headerDict})
    api.add_resource(FooterDictAPI, '/api/v1/csv/footer', resource_class_kwargs={'fdict':footerDict})
    api.add_resource(DataListAPI, '/api/v1/csv/data', resource_class_kwargs={'dlist':dataList})
    api.add_resource(DataChannelAPI, '/api/v1/csv/channel', resource_class_kwargs={'dlist' :dataList})


    @app.route('/api/v1/csv/channel', methods=['POST', 'GET'])
  
    def webInput():
        item = ""
        if request.method == 'POST':
            item = request.form['dataForm']
        else:
            item = request.args.get('dataForm')
        print(item)    
   
    app.run(port=1339, debug=True)


     

if __name__ == '__main__': 
    main()
    