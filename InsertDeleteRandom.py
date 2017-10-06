"""
Data Structure supports the following operations:

Insert - O(1)
Delete - O(1)
GetRandom - O(1)

Note: This version does not allow duplicates

"""
class InsertDeleteRandom:
	
	def __init__(self):
		
		self. _arr = []
		self. _map = {}

	"""
	Tries to insert val into the list.

	:param val: value to be inserted
	:returns: true if insert success, false if already exists
	"""
	def insert(self, val):
		if val in self._map: return False
		self._map[val] = len(self._arr)
		self._arr.append(val)
		return True

	"""
	Tries to delete val from list.

	:param val: value to be deleted
	:returns: true if delete success, false if DNE
	"""
	def delete(self, val):
		if val not in self._map: return False
		p = self._map[val] # position of val
		if p != len(self._arr) - 1:
			self._arr[p], self._arr[-1] = self._arr[-1], self._arr[p] 
			self._map[self._arr[p]] = p
		self._arr.pop()
		del self._map[val]
		return True

	"""
	Returns a random element from list

	:returns: random element within list
	"""
	def get_random(self):
		return not self.is_empty() and random.choice(self._arr)

	def is_empty(self):
		return len(self._arr) > 0
