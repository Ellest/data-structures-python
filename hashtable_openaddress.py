class HashTable:
    """ 
    Uses Open Addressing 

    oa_option -> flag for which collision resolving option:
        - 1: Linear Probing
        - 2: Quadratic Probing
        - 3: Double Hashing
    """
    def __init__(self, size=20, low_bound=0.15, high_bound=0.7, oa_option=1):
        self.table = [None for _ in range(size)]
        self.high_bound = high_bound
        self.low_bound = low_bound
        self.elemCount = 0

        self.dispatcher = {
            1: lambda v: self.linear_probing(v),
            2: lambda v: self.quadratic_probing(v),
            3: lambda v: self.double_hashing(v)
        }
        self.probe_types = {
            1: 'Linear',
            2: 'Quadratic',
            3: 'Double Hashing'
        }

        self.get_index = self.dispatcher[oa_option]
        self.probe = self.probe_types[oa_option]

    def insert(self, val):
        index = self.get_index(val)
        if self.table[index]: # already exists
            return False
        self.table[index] = val
        self.elemCount += 1
        loadFactor = self.elemCount / len(self.table)
        if loadFactor >= self.high_bound:
            self.double_size()
        return True
    
    def delete(self, val):
        index = self.get_index(val)
        if not self.table[index]: # elem DNE
            return False
        self.table[index] = None
        self.elemCount -= 1
        if loadFactor <= self.low_bound:
            self.shrink()
        return True

    def contains(self, val):
        index = self.get_index(val)
        return self.table[index] is not None

    def double_size(self):
        current = self.table
        self.table = [None for _ in range(len(self.table) * 2)]
        self.rehash(current)

    def shrink_size(self):
        current = self.table
        self.table = [None for _ in range(len(self.table) // 2)]
        self.rehash(current)

    def rehash(self, arr):
        self.elemCount = 0
        for val in arr:
            if val is not None:
                self.insert(val)

    def linear_probing(self, val):
        base = hash(val)
        index = base % len(self.table)
        while self.table[index] and self.table[index] != val:
            base += 1
            index = base % len(self.table)
        return index

    def quadratic_probing(self, val):
        base = hash(val)
        index = base % len(self.table)
        offset = 1
        while self.table[index] and self.table[index] != val:
            index = (base + offset ** 2) % len(self.table)
            offset += 1
        return index

    def double_hashing(self, val):
        base = factor = hash(val)
        index = base % len(self.table)
        while self.table[index] and self.table[index] != val:
            base += factor
            index = base % len(self.table)
        return index

    def display_table(self):
        print('-----------------------')
        print('Size: {}'.format(len(self.table)))
        print('Element Count: {}'.format(self.elemCount))
        print('Load Factor: {}'.format(self.elemCount / len(self.table)))
        print('Probing Method: {}'.format(self.probe))
        print('-----------------------')
        print(self.table)

if __name__ == '__main__':
    myTable = HashTable(size=5)

    myTable.insert(1)
    myTable.display_table()

    myTable.insert(3)
    myTable.display_table()

    myTable.insert(8)
    myTable.display_table()

    myTable.insert(9)
    myTable.display_table()

    print(myTable.contains(4))
    
    print(myTable.contains(8))