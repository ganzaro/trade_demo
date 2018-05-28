from flask import jsonify, Blueprint, request

str_api = Blueprint('string', __name__)
from app.mini_red.str_ops import StringMap

smap = StringMap()

@str_api.route('/get/<key>')
def get(key):
    print("keyz2- " + key)
    return smap.get(str(key))


@str_api.route('/set_kv', methods=['POST'])
def set_kv():
    k = request.json['key']
    v = request.json['value']
    
    smap.set_kv(k, v)

    return 'key: {}, value {} added'.format(k, v)

@str_api.route('/delete_key/<key>', methods=['DELETE'])
def delete(key):
    smap.delete_key(key)
    return '{} deleted'.format(key)

@str_api.route('/get_all')
def get_all():
    response = vars(smap)

    return jsonify(response)










