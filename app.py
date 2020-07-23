import os
from flask import Flask, request
from core import concat_2_str

app = Flask(__name__)

cors_options_res = ('', 204, {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600'
})
cors_header = {
    'Access-Control-Allow-Origin': '*'
}

@app.route('/healthz', methods=['GET'])
def healthz():
    return ('OK', 200)

def parse_entry_req(request):
    str1 = request.args.get('str1')
    str2 = request.args.get('str2')
    return str1, str2

@app.route('/entry', methods=['GET', 'POST', 'OPTIONS'])
def entry():
    if request.method == 'OPTIONS':
        return cors_options_res
    str1, str2 = parse_entry_req(request)
    res = concat_2_str(str1, str2)
    return (res, 200, cors_header)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('app_port', 5000)))
