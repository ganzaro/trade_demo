import json
from flask import jsonify, Blueprint, request

from app.mini_red.map_ops import MapMap

mmap = MapMap()
map_api = Blueprint('map', __name__,  url_prefix='/map')

@map_api.route('/get/<key>')
def get(key):
    return json.dumps(mmap.get(str(key)))


@map_api.route('/set_kv', methods=['POST'])
def set_kv():
    k = request.json['key']
    v = request.json['value']
    
    mmap.set_kv(k, v)
    return 'key: {}, value {} added'.format(k, v)


@map_api.route('/delete_key/<key>', methods=['DELETE'])
def delete(key):
    mmap.delete_key(key)
    return '{} deleted'.format(key)


@map_api.route('/get_all')
def get_all():
    response = vars(mmap)

    return jsonify(response)


@map_api.route('/map_get/<key>/<map_key>')
def map_get(key, map_key):
    val = mmap.map_get(key, map_key)
    return json.dumps(val)

