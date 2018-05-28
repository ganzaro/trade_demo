# from flask import jsonify, Blueprint, request

# map_api = Blueprint('map', __name__,  url_prefix='/map')
# from app.mini_red.map_ops import MapMap

# mmap = MapMap()

# @str_api.route('/get/<key>')
# def get(key):
#     print("keyz2- " + key)
#     return smap.get(str(key))


# @str_api.route('/set_kv', methods=['POST'])
# def set_kv():
#     k = request.json['key']
#     v = request.json['value']
    
#     smap.set_kv(k, v)
#     response = vars(smap)

#     return jsonify(response)

# @str_api.route('/delete_key/<key>', methods=['DELETE'])
# def delete(key):
#     smap.delete_key(key)
#     return '{} deleted'.format(key)

# # @str_api.route('/get_keys')
# # def get_all_keys():
# #     pass










