"""

Supports the following API in O(1) time

Inc(Key) 
    Inserts a new key with value 1. Or increments an existing key by 1. Key is 
    guaranteed to be a non-empty string.

Dec(Key) 
    If Key's value is 1, remove it from the data structure. Otherwise decrements 
    an existing key by 1. If the key does not exist, this function does nothing. 
    Key is guaranteed to be a non-empty string.

GetMaxKey()
    Returns one of the keys with maximal value. If no element exists, return 
    an empty string "".

GetMinKey() 
    Returns one of the keys with minimal value. If no element exists, return 
    an empty string "".

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = self.prev = None

class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._nodes = {}
        self._keys = {}
        self._vals = collections.defaultdict(set)
        self._head = Node(None)
        self._tail = Node(None)
        self._head.next = self._tail
        self._tail.prev = self._head
    
    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        self._keys[key] = self._keys.get(key, 0) + 1
        val, orig = self._keys[key], self._keys[key] - 1
        current_node = orig and self._nodes[orig] or self._head
        if val not in self._nodes:
            self.insert_after(current_node, val)
        self._vals[val].add(key)
        if orig:
            self._vals[orig].remove(key)
            self.update_original(orig)

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self._keys:
            orig = self._keys[key]
            self._keys[key] -= 1
            val = self._keys[key]
            if not val:
                del self._keys[key]
            self._vals[orig].remove(key)
            if val:
                if val not in self._nodes:
                    self.insert_after(self._nodes[orig].prev, val)
                self._vals[val].add(key)
            self.update_original(orig)
            

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.isEmpty(): return ''
        return next(iter(self._vals[self._tail.prev.val]))

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.isEmpty(): return ''
        return next(iter(self._vals[self._head.next.val]))
    
    def update_original(self, val):
        if not self._vals[val]:
            self.delete_node(self._nodes[val])
            del self._vals[val]
    
    def insert_after(self, node, val):
        self._nodes[val] = Node(val) 
        nxt = self._nodes[val]
        nxt.next, nxt.prev = node.next, node
        node.next.prev = node.next = nxt 
    
    def delete_node(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        node.next = node.prev = None # remove pointers
        del self._nodes[node.val]
    
    def isEmpty(self):
        return self._head.next == self._tail