from flask import jsonify, Blueprint, request

list_api = Blueprint('list', __name__,  url_prefix='/list')

from app.mini_red.list_ops import ListMap

lmap = ListMap()

@list_api.route('/get/<key>')
def get(key):
    return lmap.get(str(key))


@list_api.route('/set_kv', methods=['POST'])
def set_kv():
    k = request.json['key']
    v = request.json['value']
    
    lmap.set_kv(k, v)
    response = vars(lmap)

    return jsonify(response)

@list_api.route('/delete_key/<key>', methods=['DELETE'])
def delete(key):
    lmap.delete_key(key)
    return '{} deleted'.format(key)


@list_api.route('/append_kv', methods=['POST'])
def append_kv():
    k = request.json['key']
    v = request.json['value']

    lmap.append_value(k, v)
    response = vars(lmap)

    return jsonify(response)

# @str_api.route('/get_keys')
# def get_all_keys():
#     pass










