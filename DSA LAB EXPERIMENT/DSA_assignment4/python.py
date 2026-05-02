from collections import deque


# =====================================================
# PART 1: BINARY SEARCH TREE (BST)
# =====================================================

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def insert(self, root, key):
        if root is None:
            return BSTNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)

        return self.search(root.right, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def min_value_node(self, node):
        current = node

        while current.left:
            current = current.left

        return current

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)

        elif key > root.key:
            root.right = self.delete(root.right, key)

        else:
            # No child
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            # Two children
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        return root


# =====================================================
# PART 2: GRAPH (Adjacency List + BFS + DFS)
# =====================================================

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []

        self.graph[u].append(v)

    def print_graph(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")

    def bfs(self, start):
        visited = set()
        queue = deque([start])

        print("BFS Traversal:", end=" ")

        while queue:
            node = queue.popleft()

            if node not in visited:
                print(node, end=" ")
                visited.add(node)

                for neighbor in self.graph.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)

        print()

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
            print("DFS Traversal:", end=" ")

        visited.add(start)
        print(start, end=" ")

        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)


# =====================================================
# PART 3: HASH TABLE (Separate Chaining)
# =====================================================

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return

        self.table[index].append([key, value])

    def get(self, key):
        index = self.hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]

        return "Not Found"

    def delete(self, key):
        index = self.hash_function(key)

        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return "Deleted"

        return "Not Found"

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")


# =====================================================
# MAIN PROGRAM DEMO
# =====================================================

# BST Demo
print("\n===== BINARY SEARCH TREE =====")
bst = BST()
root = None

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    root = bst.insert(root, value)

print("Inorder Traversal:")
bst.inorder(root)

print("\nSearch 40:", "Found" if bst.search(root, 40) else "Not Found")

root = bst.delete(root, 30)

print("After Deleting 30:")
bst.inorder(root)


# Graph Demo
print("\n\n===== GRAPH =====")
g = Graph()

edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('B', 'E'),
    ('C', 'F'),
    ('E', 'F')
]

for u, v in edges:
    g.add_edge(u, v)

print("Adjacency List:")
g.print_graph()

g.bfs('A')
g.dfs('A')


# Hash Table Demo
print("\n\n===== HASH TABLE =====")
ht = HashTable(5)

ht.insert(10, "Apple")
ht.insert(15, "Banana")  # Collision with 10
ht.insert(20, "Cherry")  # Collision

ht.display()

print("Get Key 15:", ht.get(15))

print("Delete Key 15:", ht.delete(15))

ht.display()