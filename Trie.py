class Trie:

	def __init__(self, wordList=[]):
		self.trie = {}
		self.add_list(wordList)

	def add_list(self, wordList):
		for w in wordList:
			self.add_word(w)

	def add_word(self, word):
		if word:
			node = self.trie
			for char in word:
				node = node.setdefault(char, {})
			node['#'] = {} # make end node

	def word_search(self, word):
		if word: 
			node = self.trie
			for char in word:
				if char not in node: 
					return False
				node = node[char]
			return '#' in node # check if there's an end
		return False

	def delete_word(self, word):
		if word:
			stack = [self.trie]
			node = self.trie
			for char in word:
				if char not in node: # word DNE since mismatch
					return
				node = node[char]
				stack.append(node)
			if '#' in node: #word exists since terminal node
				stack.pop() # remove last since last == node
				del node['#']
				# use stack to traverse back to delete child nodes if empty
				for i in range(len(word)-1, -1, -1):
					node = stack.pop()
					if not node[word[i]]:
						del node[word[i]]


	def recursive_find(self, node, sequence, tails):
		if '#' in node:
			tails.append(''.join(sequence))
		for child in node:
			sequence.append(child)
			self.recursive_find(node[child], sequence, tails)
			sequence.pop()

	def prefix_search(self, prefix):
		node = self.trie
		for char in prefix:
			if char not in node:
				return []
			node = node[char]
		tails = []
		self.recursive_find(node, [], tails)
		return [prefix + tail for tail in tails]


"""

# example uses

myTrie = Trie()
myTrie.add_word('hello')
myTrie.add_word('hellow')
print myTrie.word_search('hello')
print myTrie.word_search('helo')
print myTrie.prefix_search('he')
myTrie.delete_word('hel')
print myTrie.prefix_search('he')
myTrie.delete_word('hello')
print myTrie.prefix_search('he')

"""
