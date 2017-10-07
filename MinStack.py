"""

Stack that keeps track of the minmum value in the stack.
Uses O(n) extra space to keep minmum at each value

O(1) push, pop, peek, get_min 
"""

class MinStack:

	def __init__(self):
		self._stack = []
		self._min = None

	"""
	Pops and returns the element at the top of the stack.
	Adjusts min accordingly 

	:returns: top of stack
	"""
	def pop(self):
		if not self.isEmpty():
			returnVal, self._min = self._stack.pop()
			return returnVal

	"""
	Pushes given val to stack. 

	:returns: None
	"""
	def push(self, val):
		self._stack.append((val, self._min))
		if self._min is None or val < self._min:
			self._min = val

	"""
	Returns the element at the top of the stack

	:returns: top of stack
	"""
	def peek(self):
		if not self.isEmpty():
			return self._stack[-1][0]

	"""
	Returns the min value of the stack	

	:returns: stack min
	"""
	def get_min(self):
		if not self.isEmpty():
			return self._min

	"""
	Checks if the stack is emtpy

	:returns: boolean 
	"""
	def isEmpty(self):
		return len(self._stack) > 0

