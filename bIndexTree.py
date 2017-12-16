class binaryIndexTree:
    """
    Important Notes:
        - Used for prefix sums (could be prefix anything)
        - Need to utilize bit manipulation to get parent
        - Why is Next operating the way it is? Why not just get next pow 2?
            -> get_next seems like it's incrementing by each set bit 
                => i.e. 9 -> 10 -> 12 -> 16 -> ...
                =>    1001 -> 1010 -> 1100 -> 10000
        - Update -> logn
        - Init fill -> n * logn (n updates)
        - prefix sum -> logn
    """
    def __init__(self, arr):
        self.elems = arr
        self.sums = [0 for _ in range(len(arr) + 1)]
        self.fill()

    def fill(self):
        for i in range(len(self.elems)):
            self.update(i+1, self.elems[i])

    def update(self, i, net):
        while i < len(self.sums):
            self.sums[i] += net
            i = self.get_next(i)

    def getsum(self, i):
        if i < len(self.elems):
            s = 0
            pos = i + 1
            while pos > 0:
                s += self.sums[pos]
                pos = self.get_parent(pos)
            return s

    def leastSetBit(self, i):
        return i & -i

    def get_next(self, i):
        return i + self.leastSetBit(i)

    def get_parent(self, i):
        return i ^ self.leastSetBit(i) if i else 0

    def elem_at(self, i):
        return self.elems[i]
    
    def size(self):
        return len(self.elems)

    def print_arr(self):
        print(self.elems)

if __name__ == '__main__':
    arr = [3,2,-1,6,5,4,-3,3,7,2,3]
    bit = binaryIndexTree(arr)
    print(bit.getsum(5))
    print(bit.getsum(8))
    