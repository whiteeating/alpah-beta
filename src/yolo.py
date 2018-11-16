from flask import Flask, request,Response
import json
import jsonpath
import time
import os
import logging
import logger
from PIL import Image
import numpy as np
from werkzeug.utils import secure_filename
import uuid
from dnt import *

app = Flask(__name__)
UPLOAD_FOLDER = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'gif', 'GIF'])

#mylogger.info("ctpn inti")
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def hello_world():
    return '<h3>'+'hello world'+'</h3>'

@app.route('/yolo', methods=['POST'])
def ctpn():
    FileList = request.json['FileList']
    js = json.dumps(request.json, sort_keys=True, indent=4, separators=(',', ':'))
    try:
        res=performDetect(FileList)
        print(type(res))
        '''
	wordlist = jsonpath.jsonpath(result,'$..text')
	word=''
    	for i in wordlist:
        	word=word+i
    	return word
        '''
        return res;
	#return json.dumps({'res':result,'timeTake':round(timeTake,4)},ensure_ascii=False)
    except Exception as e:
        print('error : \n' + str(e))
        print('request output : \n' + js)
        return "wrong"
@app.route('/up_photo', methods=['POST'], strict_slashes=False)
def api_upload():
    print("ok")
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    f = request.files['photo']
    if f and allowed_file(f.filename):
        fname = secure_filename(f.filename)
        ext = fname.rsplit('.', 1)[1]
        new_filename = str(uuid.uuid1()) + '.' + ext
        img_path=os.path.join(file_dir, new_filename)
        f.save(img_path)
        print(img_path)
        #orc_info = {'TraceId': '20180808010101-0000001','FileList': img_path, 'Image': ''}
        #words=api_test.test1(orc_info)
        return img_path
    else:
        return jsonify({"error": 1001, "msg": "wrong connect"})
if __name__ == '__main__':
    app.run(port=4, debug=True,use_reloader=False,host='172.16.24.38')
