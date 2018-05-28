from flask import jsonify, Blueprint, request

str_api = Blueprint('string', __name__)
from app.mini_red.str_ops import StringMap

smap = StringMap()

@str_api.route('/<int:key>/get')
def get(key):
    return smap.get(key)
    # return 'Hello World'


@str_api.route('/set_kv', methods=['POST'])
def set_kv():
    k = request.json['key']
    v = request.json['value']
    
    smap.set_kv(k, v)

    return str(smap)












