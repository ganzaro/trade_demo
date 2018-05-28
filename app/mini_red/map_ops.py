
"""
○ GET key​ : Return the Map value identified by key
○ SET key value​ : Instantiate or overwrite a Map identified by key with value value
○ DELETE key​ : Delete the Map identified by key
○ MAPGET key mapkey​ : Return the String identified by mapkey from within the
Map identified by key.
○ MAPSET key mapkey mapvalue​ : Add the mapping mapkey -> mapvalue to the
Map identified by key.
○ MAPDELETE key mapkey​ : Delete the value identified by mapkey from the Map

TODO
assert value type is map
"""

class MapMap():

    def __init__(self):

        self._mapz = {}


    def set_kv(self, k, v):
        """Adds the pair (k, v) to the table"""
        self._mapz[k] = v

    def contains(self, k):
        """Returns true if the map contains the given key"""
        return k in self._mapz

    def get(self, k):
        """Returns the value associated with the key"""
        return self._mapz[k]

    def delete_key(self, k):
        self._mapz.pop(k, None)

    def map_get(self, k, map_key):
        val_map = self.get(k)
        return val_map[map_key]

    def map_set(self, k, map_key, map_val):
        pass

    def map_del(self, k, map_key):
        pass

# s = MapMap()
# s.set_kv("c1", {"k1": "v1"})
# s.set_kv("c2", {"k2": "v2", "k22": "v22"})
# print(s.get('c2'))

# print(s.map_get("c2", "k22"))
