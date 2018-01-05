import random
import sys
import argparse

class TreeNode:
    """
    Binary Tree Node obj. Contains an additional variable 'height' to keep
    track of maximum depth at the node
    """
    def __init__(self, val):
        self.val = val
        self._left = self._right = None # private backing fields
        self.left_h = self.right_h = 0
        self.height = 1

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node
        self.left_h = node and node.height or 0
        self.height = max(self.left_h, self.right_h) + 1
        #self.update_height()

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node
        #temp = self.height
        self.right_h = node and node.height or 0
        self.height = max(self.left_h, self.right_h) + 1
        #self.update_height()
        #print('updating root height from {} to {}...'.format(temp, self.height))

    def height_diff(self):
        #left_h = self.left and self.left.height or 0
        #right_h = self.right and self.right.height or 0
        return abs(self.left_h - self.right_h)

class AVLTree:

    """
    BST with AVL balancing. Uses a bit of an assumption that the tree is balanced
    before each insert. This means we can identify the type of rotation sequence
    by check the insert position and subtree structure. 
    """
    def __init__(self, debug=False, visualizer=None):
        self.root = None
        self.visualizer = visualizer
        self.debug = debug

    @classmethod
    def initWithRandom(cls, size=10, **kwargs):
        treeObj = cls(**kwargs)
        for _ in range(size):
            treeObj.insert(random.randint(1, 100)) 

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
            if insertNode.val < node.val: # means insert happened left
                node.left = self.insertHelper(node.left, insertNode)
                if node.height_diff() > 1:
                    # if insertNode was greater than right we must have a left-right
                    # case because if we assume tree was balanced before insert, the
                    # point at we see a height difference must be at least 2 nodes 
                    # (levels) away from the insert level
                    if insertNode.val > node.left.val: 
                        node.left = self.rotateLeft(node.left)
                    node = self.rotateRight(node)
            else:
                node.right = self.insertHelper(node.right, insertNode)
                if node.height_diff() > 1:
                    # same logic as above, but opposite side 
                    if insertNode.val < node.right.val: # right - left case
                        node.right = self.rotateRight(node.right)
                    node = self.rotateLeft(node)
        return node

    def insert(self, val):
        self.root = self.insertHelper(self.root, TreeNode(val))
        if self.debug:
            self.visualizer.visualize(self.root)
            print('----------------------')

    def rotateRight(self, node):
        pivot = node.left
        node.left, pivot.right = pivot.right, node
        return pivot

    def rotateLeft(self, node):
        pivot = node.right
        node.right, pivot.left = pivot.left, node
        return pivot

    def deleteHelper(self, root, key):
        if not root:
            return      
        if key == root.val:
            if not root.right:
                return root.left
            itr = root.right
            while itr.left:
                itr = itr.left
            root.val, itr.val = itr.val, root.val # swap value with next greatest
            root.right = self.deleteNode(root.right, key) # recursively delete
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root

    def deleteVal(self, key):
        if type(key) == int:
            self.root = self.deleteHelper(self.root, key)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='AVL Tree Data Structure')
    parser.add_argument('-d', '--debug', help='Debug Flag', action='store_true', required=False)
    parser.add_argument('-r', '--random', help='Random Flag', action='store_true', required=False)
    parser.add_argument('-s', '--size', help='Random Count', required=True)
    args = vars(parser.parse_args())
    if args['debug']:
        viz = None
        try:
            from BTreeVisualizer import BTreeVisualizer
            viz = BTreeVisualizer()
        except ImportError as e:
            print('BTreeVisualizer Not Found. Make sure to include it in the same dir!!')
        else:
            if args['random']:
                avl = AVLTree.initWithRandom(size=int(args['size']), debug=True, visualizer=viz)
    else:
        if args['random']:
            avl = AVLTree.initWithRandom(debug=False)
    
