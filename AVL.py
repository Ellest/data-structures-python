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

    def search(self, val):
        pass

    def insert(self, val):
        pass

    def rotateRight(self, node):
        pivot = node.left
        node.left, pivot.right = pivot.right, node
        return pivot

    def rotateLeft(self, node):
        pivot = node.right
        node.right, pivot.left = pivot.left, node
        return pivot

if __name__ == '__main__':
    pass