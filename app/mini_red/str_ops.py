"""

○ GET key​ : Return the String value identified by key
○ SET key value​ : Instantiate or overwrite a String identified by key with value value
○ DELETE key​ : Delete the String identified by key

"""

class StringMap():

    def __init__(self):

        self._mapz = {}

    # TODO set, update
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


# s = StringMap()
# s.add_entry("KBD", "v1")
# s.add_entry("c1", "v2")
# s.add_entry("c2", "v3")
# print(s.get_key('c2'))

# for k in s._mapz:
#     print(k)

# s.delete_key("c2")
# print(s.get_key('c2'))





