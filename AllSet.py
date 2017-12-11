class AllSet:
    """
    Data structure supporting the following ops in O(1) time:

    get(key)
        - get val associated with key

    set(key, val)
        - set key to val

    setAll(val)
        - sets all elements contained to val
    """
    def __init__(self):
        self.updates = set()
        self.all = None
        self._map = {}

    @classmethod
    def initWithMap(cls, mp):
        c = cls()
        if not mp:
            return c
        for k in mp:
            c.set(k, mp[k])
        return c

    def get(self, key):
        if key not in self._map:
            return -1
        if key not in self.updates and self.all:
            self.updates.add(key)
            self._map[key] = self.all
        return self._map[key]

    def set(self, key, val):
        self.updates.add(key)
        self._map[key] = val

    def setAll(self, val):
        self.updates = set()
        self.all = val
    
if __name__ == '__main__':
    myMap = {1:2, 3:4, 5:10}
    a = AllSet.initWithMap(myMap)

    print(a.get(1)) # 2
    print(a.get(2)) # -1
    print(a.get(5)) # 10
    a.setAll(5)
    print(a.get(1)) # 5
    print(a.get(5)) # 5
    a.set(1, 3)
    print(a.get(1)) # 3 
    a.setAll(15)
    print(a.get(1)) # 15
    print(a.get(5)) # 15
    a.set(5, 3)
    print(a.get(5)) # 3
    a.set(5, 4)
    print(a.get(5)) # 4
