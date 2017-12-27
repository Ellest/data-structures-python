class MaxHeap:
    
    def __init__(self):
        self.elems = []
    
    def get_parent(self, i):
        return i // 2

    def get_left(self, i):
        return 2 * i + 1

    def get_right(self, i):
        return 2 * i + 2

    def bubble_up(self, ind):
        parent = self.get_parent(ind)
        while ind > 0 and self.elems[parent] < self.elems[ind]:
            self.elems[parent], self.elems[ind] = self.elems[ind], self.elems[parent]
            ind, parent = parent, self.get_parent(parent)

    def heapify(self, ind):
        biggest = ind
        left, right = self.get_left(ind), self.get_right(ind)
        if left < len(self.elems) and self.elems[biggest] < self.elems[left]:
            biggest = left
        if right < len(self.elems) and self.elems[biggest] < self.elems[right]:
            biggest = right
        if biggest != ind:
            self.elems[biggest], self.elems[ind] = self.elems[ind], self.elems[biggest]
            self.heapify(biggest)

    def extract_max(self):
        if not self.isEmpty():
            if len(self.elems) == 1:
                return self.elems.pop()
            self.elems[0], self.elems[-1] = self.elems[-1], self.elems[0]
            temp = self.elems.pop()
            self.heapify(0) 
            return temp

    def get_max(self):
        if not self.isEmpty():
            return self.elems[0]
    
    def insert(self, val):
        self.elems.append(val)
        self.bubble_up(len(self.elems)-1)

    def isEmpty(self):
        return len(self.elems) == 0

    def printHeap(self):
        print(self.elems)

if __name__ == '__main__':
    heap = MaxHeap()
    arr = [1, 3, 2, 5, 7, 4, 3]
    for i in arr:
        heap.insert(i)
    while not heap.isEmpty():
        print(heap.extract_max())