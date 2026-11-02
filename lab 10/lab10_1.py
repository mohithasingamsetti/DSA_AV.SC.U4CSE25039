class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def insert(self, key):
        index = key % self.size
        self.table[index].append(key)

    def display(self):
        print("\nSeparate Chaining:")
        for i in range(self.size):
            print(i, ":", self.table[i])


class LinearProbing:
    def __init__(self, size):
        self.size = size
        self.table = [-1] * size

    def insert(self, key):
        index = key % self.size
        i = 0
        while i < self.size:
            new_index = (index + i) % self.size
            if self.table[new_index] == -1:
                self.table[new_index] = key
                return
            i += 1
        print("Hash Table is full")

    def display(self):
        print("\nLinear Probing:")
        for i in range(self.size):
            print(i, ":", self.table[i])


class QuadraticProbing:
    def __init__(self, size):
        self.size = size
        self.table = [-1] * size

    def insert(self, key):
        index = key % self.size
        i = 0
        while i < self.size:
            new_index = (index + i * i) % self.size
            if self.table[new_index] == -1:
                self.table[new_index] = key
                return
            i += 1
        print("Hash Table is full")

    def display(self):
        print("\nQuadratic Probing:")
        for i in range(self.size):
            print(i, ":", self.table[i])


size = 7
keys = [10, 20, 15, 7, 22]

h1 = HashTable(size)
h2 = LinearProbing(size)
h3 = QuadraticProbing(size)

for key in keys:
    h1.insert(key)
    h2.insert(key)
    h3.insert(key)

h1.display()
h2.display()
h3.display()
