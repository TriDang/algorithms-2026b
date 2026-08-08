# Problem 1
# Implement a hashtable data structure that supports
# insert(), delete(), and search() operations
# Use linear probing for collision resolution
# Assume: keys contain only uppercase letters
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    # simple hash function
    def hash(self, key):
        result = 0
        for char in key:
            result = result * 26 + (ord(char) - ord('A'))
        return result % self.size

    def insert(self, item):
        key, value = item
        index = self.hash(key)
        probe_count = 1 # use to show the number of probes for each insert operation
        while self.table[index] is not None and self.table[index][0] != "DELETED":
            if self.table[index][0] == key:  # duplicate key, update value
                self.table[index] = (key, value)
                print(f"Updated {item} at index {index} with {probe_count} probes")
                return
            index = (index + 1) % self.size  # linear probing
            probe_count += 1
        print(f"Inserted {item} at index {index} with {probe_count} probes")
        self.table[index] = (key, value)

    def delete(self, key):
        index = self.hash(key)
        probe_count = 1
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = ("DELETED", None)  # mark as deleted
                print(f"Deleted {key} from index {index} after {probe_count} probes")
                return
            index = (index + 1) % self.size
            probe_count += 1
        print(f"Key {key} not found for deletion after {probe_count} probes")

    def search(self, key):
        index = self.hash(key)
        probe_count = 1
        while self.table[index] is not None:
            if self.table[index][0] == key:
                print(f"Found {key} at index {index} with {probe_count} probes")
                return self.table[index][1]
            index = (index + 1) % self.size
            probe_count += 1
        print(f"Key {key} not found after {probe_count} probes")
        return None

# client code
hash_table = HashTable()
hash_table.insert(("A", 1))
hash_table.insert(("B", 2))
hash_table.insert(("C", 3))
hash_table.insert(("M", 4)) # collision with "C"
hash_table.insert(("K", 5)) # collision with "A", "B", "C", "M"
hash_table.insert(("U", 6)) # collision with "A", "B", "C", "M", "K"
hash_table.search("B") # 1 probe
hash_table.search("M") # 2 probes
hash_table.delete("K") # deleted after 5 probes
hash_table.search("K") # not found after 7 probes
hash_table.search("U") # 6 probes

# Problem 2
# Implement a Min-Heap data structure that supports
# insert(), extract_min(), and peek() operations.

class MinHeap:
    def __init__(self):
        self.heap = []
    
    # use item to wrap both: value (actual content) and key (priority, for comparison)
    def insert(self, item):
        # insert item at the end
        # to maintain the SHAPE property
        self.heap.append(item)
        self.heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        min_value = self.heap[0]
        # move the last element to root
        self.heap[0] = self.heap[-1]
        # remove the last element
        self.heap.pop()
        self.heapify_down(0)
        return min_value

    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]
    
    def heapify_up(self, index):
        while index > 0:
            parent_index = self.parent(index)
            if self.heap[index]["key"] < self.heap[parent_index]["key"]:
                # swap
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break
    def heapify_down(self, index):
        smallest = index
        left_child = self.left_child(index)
        right_child = self.right_child(index)

        if left_child < len(self.heap) and self.heap[left_child]["key"] < self.heap[smallest]["key"]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child]["key"] < self.heap[smallest]["key"]:
            smallest = right_child
        
        if smallest != index: # at least smaller than one child
            # swap
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)

    # utility methods to get parent, left child, and right child indices
    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

# client code
# min_heap = MinHeap()
# min_heap.insert({"key": 5, "value": "Five"})
# min_heap.insert({"key": 3, "value": "Three"})
# min_heap.insert({"key": 8, "value": "Eight"})
# print(min_heap.peek())  # Output: {'key': 3, 'value': 'Three'}
# print(min_heap.extract_min())  # Output: {'key': 3, 'value': 'Three'}
# print(min_heap.peek())  # Output: {'key': 5, 'value': 'Five'}

# Problem 3
# Application of the min-heap data structure above
class ShoppingOrder:
    def __init__(self):
        self.order_heap = MinHeap()

    # In this problem, higher amount means higher priority
    # So we can negate the amount in order to use the min-heap
    def add(self, name, amount):
        self.order_heap.insert({"key": -amount, "value": name})

    def next(self):
        order = self.order_heap.extract_min()
        if order is not None:
            return order["value"]

# client code
shopping_order = ShoppingOrder()
print("Enter X to stop the program")
while True:
    line = input("Next operation: ")
    if line == "X":
        break
    if line == "NEXT":
        print(shopping_order.next())
        continue
    _, name, amount = line.split()
    shopping_order.add(name, float(amount))
print("Bye")


# Problem 4
# Implement union-find (disjoint set) data structure that supports
# union(), find(), and connected() operations.
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, index):
        if self.parent[index] != index:
            self.parent[index] = self.find(self.parent[index]) # path compression
        return self.parent[index]
    
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP == rootQ:
            return

        # union by rank
        if self.rank[rootP] > self.rank[rootQ]:
            self.parent[rootQ] = rootP
        elif self.rank[rootP] < self.rank[rootQ]:
            self.parent[rootP] = rootQ
        else:
            self.parent[rootQ] = rootP
            self.rank[rootP] += 1

    def connected(self, index1, index2):
        return self.find(index1) == self.find(index2)

# client code
# union_find = UnionFind(6) # [0, 1, 2, 3, 4, 5]
# print(union_find.connected(0, 5)) # False
# union_find.union(0, 1)
# union_find.union(2, 3)
# print(union_find.connected(0, 3)) # False
# union_find.union(1, 2)
# print(union_find.connected(0, 3)) # True
# print(union_find.connected(0, 5)) # False
# union_find.union(2, 5)
# print(union_find.connected(0, 5)) # True

# Problem 5
# size = input("Number of user: ")
# print("Users:", *list(range(1, int(size) + 1)))
# union_find = UnionFind(int(size))
# print("Enter X to stop the program")
# while True:
#     line = input("Next operation: ")
#     if line == "X":
#         break
#     tokens = line.split()
#     if tokens[-1] == "?":
#         # minus 1 because user index starts from 1
#         # but our union-find implementation starts from 0
#         print(union_find.connected(int(tokens[0]) - 1, int(tokens[1]) - 1))
#     else:
#         union_find.union(int(tokens[0]) - 1, int(tokens[1]) - 1)
# print("Bye")
