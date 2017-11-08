"""
Red Black Tree implementation in Python

Rules:
	1. Root is always "Black"
	2. Red nodes cannot be adjacent (no direct parents that are red)
	3. # of "Black" nodes in paths to nodes with < 2 children are the same
		- We're essentially counting null nodes as leaves

Insertion algorithm:
	if not tree:
		insert BLACK node
	else:
		insert RED node # red-red conflict
		parent = inserted.parent
		if parent is RED:
			if parent.sibling == RED:

				color parent BLACK
				color parent.sibling BLACK

				# we don't need to recolor if parent.parent is root. This is 
				# because root node is shared between all paths thus leaving
				# the parent as black will just increment count of black nodes
				# in each path by 1 universally

				if parent's parent is not root:
					color parent.parent RED
					recheck validity of parent.parent

			elif not parent.sibling: 
				
				if parent = parent.parent.left:
					if inserted == parent.right:
						rotate left
					rotate right
					
				else:
					if inserted == parent.left:
						rotate right
					rotate left

				# update colors	
				color parent BLACK
				color parent.parent RED

			else: # parent.sibling == BLACK
				# NOTE: when a new RED node is inserted, it's parent's sibling
				# 	will either be RED or None (why is this?)
				# Thus, this case only happens when we're adjusting the tree
				# after a recoloring 

				# 4 cases
				# parent | parent.parent | rotation
				# left | left | right
				# right | left | left -> right
				# right | right | left
				# left | right | right -> left

				color parent BLACK
				color parent.parent RED

Deletion algorithm:
	
"""

import collections

class TreeNode:
	def __init__(self, v, c):
		self.val = v
		self.color = c
		self.count = 0
		self.sub = 0
		self.left = self.right = None

class RedBlackTree:
 
	# could use enums instead.
	RED = 0
	BLACK = 1

	def __init__(self, init_list=[]):
		self.root = None
		if init_list: # if initial list is passed in, generate a tree from it
			for v in init_list:
				print('val:{0}'.format(v))
				node = TreeNode(v, self.RED)
				self.insert(node)
				self.levelorder()
				print('-----------------')
		self.count = len(init_list)

	def insert(self, node):
		if not self.root:
			node.color = self.BLACK
			self.root = node
		else:
			path = []
			itr = self.root
			while itr:
				if itr.val == node.val:
					update(path)
					itr.val += 1
					return # node found. update count and exit
				path.append(itr)
				itr = itr.left if node.val < itr.val else itr.right
			# inserted by this point
			parent = path[-1]
			if parent.val > node.val: # insert
				parent.left = node
			else:
				parent.right = node
			self.try_fix(node, path)

	def update(self, nodes):
		for node in nodes:
			node.val += 1
			node.sub += 1

	def try_fix(self, node, path):
		parent = path.pop()
		if node.color == self.RED and parent.color == self.RED: # red-red conflict
			print('fix', node.val)
			# parent can't be root thus len(path) > 0
			grand = path.pop()
			sibling = grand.right if grand.val > parent.val else grand.left

			if sibling and sibling.color == self.RED:

				parent.color = sibling.color = self.BLACK
				if path: # grand is not root
					grand.color = self.RED
					self.try_fix(grand, path)

			else: # sibling is BLACK or None
				print('black or n')
				if grand.val > parent.val: # parent is left child
					if parent.val < node.val: # node is right child
						self.rotateLeft(grand, parent, node)
						parent = node
					self.rotateRight(path and path[-1] or None, grand, parent)
					grand.color, parent.color = parent.color, grand.color 

				else:
					if parent.val > node.val: # node is left child
						self.rotateRight(grand, parent, node)
						parent = node
					self.rotateLeft(path and path[-1] or None, grand, parent)
					grand.color, parent.color = parent.color, grand.color 


	def rotateRight(self, parent, pivot, child):
		# rotation
		print(pivot.val, child.val)
		if parent:
			if parent.val > pivot.val:
				parent.left = child
			else:
				parent.right = child
		else:
			self.root = child

		print('rRight')
		# subtree count adjust
		pivot.left, child.right = child.right, pivot
		temp = pivot.count
		pivot.count += -child.count + (child.right and child.right.count or 0)
		child.count = temp
		if child.left and pivot.left: # adjust left child count
			child.left.count -= pivot.left.count

	def rotateLeft(self, parent, pivot, child):
		print('rLeft')
		# rotation
		if parent:
			if parent.val > pivot.val:
				parent.left = child
			else:
				parent.right = child
		else:
			self.root = child
		pivot.right, child.left = child.left, pivot

		# subtree count adjust
		temp = pivot.count
		pivot.count += -child.count + (child.left and child.left.count or 0)
		child.count = temp
		if child.right and pivot.right:
			child.right.count -= pivot.right.count

	def delete(self, node):
		pass

	def get_node(self, val):
		node = self.root
		while node:
			if node.val == val:
				return node
			node = node.left if node.val > val else node.right
		print('Node with value {0} does not exist.'.format(val))
		return None

	def less_than_count(self, val):
		pass

	def greater_than_count(self, val):
		pass

	def inorder_print(self, node):
		if node:
			self.inorder_print(node.left)
			print(node.val)
			self.inorder_print(node.right)

	def inorder(self):
		self.inorder_print(self.root)

	def levelorder(self):
		queue = collections.deque([self.root])
		result = []
		while queue:
			temp = []
			for _ in range(len(queue)):
				n = queue.popleft()
				col = None
				if n and n.color == self.RED:
					col = 'r'
				else:
					col = 'b'
				temp.append(n and str(n.val) + col or '#')
				if n:
					queue.append(n.left)
					queue.append(n.right)
			result.append(temp)
		for r in result:
			print(r)

if __name__ == '__main__':
	
	rbTree = RedBlackTree([10,20,-10,15,17,40,50,60])
	rbTree.levelorder()