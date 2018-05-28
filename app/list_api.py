import json
from flask import jsonify, Blueprint, request

from app.mini_red.list_ops import ListMap

lmap = ListMap()
list_api = Blueprint('list', __name__,  url_prefix='/list')


# TODO sort out response, should be list
@list_api.route('/get/<key>')
def get(key):
    return json.dumps(lmap.get(str(key)))


@list_api.route('/set_kv', methods=['POST'])
def set_kv():
    k = request.json['key']
    v = request.json['value']
    
    lmap.set_kv(k, v)
    return 'key: {}, value {} added'.format(k, v)


@list_api.route('/delete_key/<key>', methods=['DELETE'])
def delete(key):
    lmap.delete_key(key)
    return '{} deleted'.format(key)


@list_api.route('/append_v', methods=['POST'])
def append_v():
    k = request.json['key']
    v = request.json['value']

    lmap.append_value(k, v)
    return 'value {} appended'.format(v)


@list_api.route('/pop_key/<key>', methods=['PUT'])
def pop_key(key):
    lmap.pop_key(key)
    return 'popped'


@list_api.route('/get_all')
def get_all():
    response = vars(lmap)

    return jsonify(response)










