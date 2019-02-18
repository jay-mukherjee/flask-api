from flask import Flask, request
import json

app = Flask(__name__)

sample_dict = {
    'heading': 'Sample header text',
    'content':'Sample page content' 
}

# the below methods are vanilla flask endpoints that return json
@app.route('/api/vanilla/endpoint1')
def endpoint1():
    jsonout = json.dumps(sample_dict)
    return jsonout

@app.route('/api/vanilla/endpoint2', methods=['POST'])
def endpoint2():
    if request.is_json:
        jsondata = request.get_json()
        # sample_dict
        sample_dict={}
        sample_dict['heading']=jsondata['header']
        sample_dict['content']=jsondata['content']
    
    return json.dumps(sample_dict)