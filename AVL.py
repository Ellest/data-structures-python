from BTreeVisualizer import BTreeVisualizer

class TreeNode:
    """
    Binary Tree Node obj. Contains an additional variable 'height' to keep
    track of maximum depth at the node
    """
    def __init__(self, val):
        self.val = val
        self._left = self._right = None # private backing fields
        self.height = 1

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node
        self.update_height()

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node
        #temp = self.height
        self.update_height()
        #print('updating root height from {} to {}...'.format(temp, self.height))

    def update_height(self):
        left_h = self.left and self.left.height or 0
        right_h = self.right and self.right.height or 0
        self.height = max(left_h, right_h) + 1

    def height_diff(self):
        left_h = self.left and self.left.height or 0
        right_h = self.right and self.right.height or 0
        return abs(left_h - right_h)

class AVLTree:
    """
    4 Cases

    left - left
    ------------
    rotation: right

    left - right
    ------------
    rotation: left -> right

    right - right
    ------------
    rotation: left

    right - left
    ------------
    rotation: right -> left
    """
    def __init__(self):
        self.root = None
        self.visualizer = BTreeVisualizer()

    def searchHelper(self, val, node):
        if not node:
            return False
        if val == node.val:
            return True
        if val < node.val:
            return self.searchHelper(val, node.left)
        return self.searchHelper(val, node.right)

    def search(self, val):
        return searchHelper(val, self.root)

    def insertHelper(self, node, insertNode):
        if not node:
            return insertNode
        # no need to insert (val found)
        # this can be extended to keep count of duplicates
        if node.val != insertNode.val: 
            if insertNode.val < node.val:
                node.left = self.insertHelper(node.left, insertNode)
                heightDiff = node.height_diff()
                if heightDiff > 1:
                    if insertNode.val > node.left.val: # left - right case
                        node.left = self.rotateLeft(node.left)
                    node = self.rotateRight(node)
            else:
                node.right = self.insertHelper(node.right, insertNode)
                heightDiff = node.height_diff()
                if heightDiff > 1:
                    if insertNode.val < node.right.val: # right - left case
                        node.right = self.rotateRight(node.right)
                    node = self.rotateLeft(node)
        return node

    def insert(self, val):
        self.root = self.insertHelper(self.root, TreeNode(val))
        #self.visualizer.visualize(self.root)
        #print('----------------------')

    def rotateRight(self, node):
        pivot = node.left
        node.left, pivot.right = pivot.right, node
        return pivot

    def rotateLeft(self, node):
        pivot = node.right
        node.right, pivot.left = pivot.left, node
        return pivot

    # for debugging
    """
    def level_order(self):
        from collections import deque
        queue = deque([self.root])
        levels = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level.append(node.val)                
            levels.append(level)
        for l in levels:
            print(l)
    """

if __name__ == '__main__':
    myAVL = AVLTree()
    myAVL.insert(1)
    myAVL.insert(2)
    myAVL.insert(3)
    myAVL.insert(6)
    myAVL.insert(15)
    myAVL.insert(-2)
    myAVL.insert(-5)
    myAVL.insert(-8)
    