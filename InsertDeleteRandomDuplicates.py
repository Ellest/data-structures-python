import random
from collections import defaultdict

"""
Data structure that supports the following operations in O(1) time:

- Insert
- Delete
- Get random element from list

"""

class InsertDeleteRandom:

	def __init__(self):
		self._list = []
		self._map = defaultdict(set)

	"""
	Insert a given value into the list

	:param val: value to insert
	:returns: whether the list already contained the element or not
	"""
	def insert(self, val):
		self._map[val].add(len(self._list))
		self._list.append(val)
		return len(self._map[val]) == 1

	"""
	Deletes the passed in value from the list.
	Shifts array elements to make delete constant and also to maintain the 
	data structure porperly.

	:param val: value to delete
	:returns: delete status
	"""
	def delete(self, val):
		if val not in self._map: 
			return False
		end = len(self._list) - 1
		if end in self._map[val]:
			self._map[val].remove(end)
		else:
			pos = self._map[val].pop() # grabs a random value from index list
			self._list[pos], self._list[-1] = self._list[-1], self._list[pos] # swap with end
			element = self._list[pos] # swapped element (originally at end)
			# update index list
			self._map[element].remove(end)
			self._map[element].add(pos)
		self._list.pop()
		if not self._map[val]: # delete from map if list does not contain anymore of it
			del self._map[val]
		return True

	"""
	Utilizes the random module to return a random element from the list.
	An alternative to random.choice would be using random.randint to generate
	a random value within the range of the length of the array and returning
	the element at that index.

	:returns: random element from list
	"""
	def get_random(self):
		return random.choice(self._arr)