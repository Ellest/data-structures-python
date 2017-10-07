from collections import defaultdict

"""

Disjoint sets

Utilizes Path Compression when merging to maintain optimal performance.
Path Compression is critical for disjoint sets to maintain performance 
levels. Without compression, the data structure will just become an N-ary
tree and operations will depend on the height of the tree.

"""


class DisjointSet:

	def __init__(self, data_array = []):
		self._parents = {}
		self._ranks = {}
		# if given array is not empty, create set for each element
		for data in data_array:
			make_set(data)
	"""
	Creates a "set" for given data

	:param data: 

	"""
	def make_set(self, data):
		if not self.contains(data):
			self._parents[data] = data
			self._ranks[data] = 0

	"""
	Returns the parent of the given node. 
	* Recursively performs path compression during the process.

	:param node: given node to find parent of
	:returns: return highest parent of given node
	"""
	def get_parent(self, data):
		if self._parents[data] == data:
			return data
		# recursive call to parent's parent
		self._parents[data] = self.get_parent(self._parents[data]) 
		return self._parents[data]

	"""
	Unions two sets

	:returns: union status
	"""
	def union(self, data1, data2):
	# check containment
		if self.contains(data1) and self.contains(data2): 
			parent1, parent2 = self.get_parent(data1), self.get_parent(data2)
			if parent1 != parent2:  
				if self._ranks[parent1] >= self._ranks[parent2]:
					# increment rank if two parents have the same rank
					if self._ranks[parent1] == self._ranks[parent2]:
						self._ranks[parent1] += 1
					self._parents[parent2] = parent1
				else:
					self._ranks[parent2] += 1
					self._parents[parent1] = parent2
				return True
		return False

	"""
	Visualize the data structure. Does not perform path compression
	as this is just a visualization tool

	:returns: list of sets
	"""
	def get_sets(self):
		sets = defaultdict(list)
		processed = set()
		for data in self._parents:
			if data not in processed:
				chain = []
				if self._parents[data] == data:
					processed.add(data)
					chain = [data]
				while data not in processed and self._parents[data] != data:
					processed.add(data)
					chain.append(data)
					data = self._parents[data]
				sets[data].extend(chain)	
		print sets.values()

	"""
	Checks if a certain data is currently in the data structure

	:returns: boolean indicating containment
	"""
	def contains(self, data):
		return data in self._parents


"""

# Example Use
mySet = DisjointSet()
mySet.make_set('A')
mySet.make_set('B')
mySet.make_set('C')
mySet.get_sets()
mySet.union('A','B')
mySet.get_sets()
mySet.union('B', 'C')
mySet.get_sets()

"""