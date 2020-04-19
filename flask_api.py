from flask import Flask, jsonify, request
from lib import* #library file
from line_removal import*  #morphological operation file
from tessarct import*  #tessaract processing file

app = Flask(__name__)

@app.route('/mean',methods =['POST'])
def meaning():
    request_data = request.get_json()
    if "file_path" in request_data.keys(): #checks file path in key....
        arg = open(request_data['file_path'],request_data['name'])  #passing path & name of img.
        tes = tesract(request_data['name']) # passing parameter to tessract file
        param = arg.path()  #line_removal.py
        pytes = tes.pro()  #tessarct.py 
        syno = tes.syn()  #tessarct.py
        return jsonify("Successfully done!!!",pytes,syno)
    else:
        return jsonify("FilePath Not Given")

app.run(debug=True)
