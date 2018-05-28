
"""
GET key​ : Return the List value identified by key
SET key value​ : Instantiate or overwrite a List identified by key with value value
DELETE key​ : Delete the List identified by key
APPEND key value​ : Append a String value to the end of the List identified by key
POP key​ : Remove the last element in the List identified by key, and return that elt

TODO
assert value type is list
"""

class ListMap():

    def __init__(self):

        self._mapz = {}

    def set_kv(self, k, v):
        """Adds the pair (k, v) """
        # assert type(v) == list
        self._mapz[k] = v

    def contains(self, k):
        """Returns true if the map contains the given key"""
        return k in self._mapz

    def get(self, k):
        """Returns the value associated with the key"""
        if self.contains(k):
            return self._mapz[k]
        else:
            raise KeyError("Key not found")

    def delete_key(self, k):
        self._mapz.pop(k, None)


    def append_value(self, k, v):
        """Append a value to the end of the List identified by key"""
        lst = self.get(k)
        lst.append(v)

        self.set_kv(k, v)


    def pop_key(self, k):
        """Remove the last List element identified by key, 
        and return that element """
        lst = self.get(k)
        val = lst.pop()
        return val
        
