from flask import json
from flask.templating import render_template
from Key_Values import parseKeyValueFile
import flask
from flask import Flask , jsonify
from flask.globals import request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS, cross_origin


app = Flask(__name__)
api = Api(app)
CORS(app)




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
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('item')   
        args = self.parser.parse_args()
        value = args.get('item')
        self.get(value)

    def get(self, value):
        # extract index from request

        index = 0
        for items in self.dataList:
            if value == items.title():
                index += 1
                return jsonify({"Channel"[index]: items.data()})
            index += 1
        # check index for range

        #return datachannel
        



    
    
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
    
    app.run(port=1339, debug=True)



if __name__ == '__main__': 
    main()



#@app.route('/api/v1/csv/channel/', methods=['GET'])
#def channel():
    #item = ""
    #item = request.args.get('id')
    #return item
    #print(item)
