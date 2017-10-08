"""
This data structure keeps track of the count of each element inserted. It also
returns min and max in O(1) time as well. Uses a doubly linked list to keep track
of distinct counts to achieve efficiency. 

Provides these operations in O(1):

    - whether a key exists
    - count of a key
    - any (or all) elements with the minimum/maximum count

"""


"""
Node for doubly linked list
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = self.prev = None

class CounterMinMax(object):

    def __init__(self):
        self._nodes = {}
        self._keys = {}
        self._vals = collections.defaultdict(set)
        self._head = Node(None)
        self._tail = Node(None)
        self._head.next = self._tail
        self._tail.prev = self._head
    
    """
    Inserts a new key <Key> with value 1. Or increments an existing key by 1.

    :param key: str
    :returns: void
    """
    def inc(self, key):
        self._keys[key] = self._keys.get(key, 0) + 1
        val, orig = self._keys[key], self._keys[key] - 1
        current_node = orig and self._nodes[orig] or self._head
        if val not in self._nodes:
            self.insert_after(current_node, val)
        self._vals[val].add(key)
        if orig:
            self._vals[orig].remove(key)
            self.update_original(orig)

    """
    Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.

    :param key: str
    :returns: void
    """
    def dec(self, key):
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
            
    """
    Returns one of the keys with maximal value.

    :returns: str
    """
    def getMaxKey(self):
        
        if self.isEmpty(): return ''
        return next(iter(self._vals[self._tail.prev.val]))

    """
    Returns one of the keys with Minimal value.

    :returns: str
    """
    def getMinKey(self):
        if self.isEmpty(): return ''
        return next(iter(self._vals[self._head.next.val]))
    
    """
    Check if count for a certain value is 0, then deletes the node 
    associated with the value.

    :returns: void
    """
    def update_original(self, val):
        if not self._vals[val]:
            self.delete_node(self._nodes[val])
            del self._vals[val]
    
    """
    Creates a node then inserts it after the node that's passed in

    :param node: node to insert after
    :param val: value to create node with  
    :returns: void
    """
    def insert_after(self, node, val):
        self._nodes[val] = Node(val) 
        nxt = self._nodes[val]
        nxt.next, nxt.prev = node.next, node
        node.next.prev = node.next = nxt 
    
    """
    Delete a specified node. removes from node hashmap as well

    :param node: node to delete
    :returns: void
    """
    def delete_node(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        node.next = node.prev = None # remove pointers
        del self._nodes[node.val]
    
    """
    Returns whether the data structure is empty or not.

    :returns: bool
    """
    def isEmpty(self):
        return self._head.next == self._tail