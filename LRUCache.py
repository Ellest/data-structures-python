"""

Uses a Doubly Linked list as the core of the implementation.

"""
class DLNode:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = DLNode(None, None)
        self.tail = DLNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self._map = {}
        
    def add(self, node):
        last = self.tail.prev
        last.next = self.tail.prev = node
        node.prev = last
        node.next = self.tail
    
    def delete(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        node.next = None
            
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # get node if exists, then update usage on it
        if key not in self._map: return -1
        node = self._map[key]
        self.delete(node)
        self.add(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0: return
        if key in self._map:
            self._map[key].val = value
            self.get(key)
        else:
            if len(self._map) == self.capacity:
                del self._map[self.head.next.key]
                self.delete(self.head.next)
            node = DLNode(key, value)
            self._map[key] = node
            self.add(node)