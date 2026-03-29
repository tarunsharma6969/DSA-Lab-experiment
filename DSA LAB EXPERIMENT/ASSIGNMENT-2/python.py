class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.arr = [0] * self.capacity

    def append(self, x):
        if self.length == self.capacity:
            self.capacity *= 2
            new_arr = [0] * self.capacity
            for i in range(self.length):
                new_arr[i] = self.arr[i]
            self.arr = new_arr
        self.arr[self.length] = x
        self.length += 1

    def pop(self):
        if self.length > 0:
            self.length -= 1

    def display(self):
        print(self.arr[:self.length])


class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def insert(self, x):
        n = SLLNode(x)
        if not self.head:
            self.head = n
        else:
            t = self.head
            while t.next:
                t = t.next
            t.next = n

    def display(self):
        t = self.head
        while t:
            print(t.data, end=" ")
            t = t.next
        print()


class DLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None

    def insert(self, x):
        n = DLLNode(x)
        if not self.head:
            self.head = n
        else:
            t = self.head
            while t.next:
                t = t.next
            t.next = n
            n.prev = t

    def display(self):
        t = self.head
        while t:
            print(t.data, end=" ")
            t = t.next
        print()


class Stack:
    def __init__(self):
        self.top_node = None

    def push(self, x):
        n = SLLNode(x)
        n.next = self.top_node
        self.top_node = n

    def pop(self):
        if self.top_node:
            self.top_node = self.top_node.next

    def top(self):
        if self.top_node:
            return self.top_node.data
        return -1


class Queue:
    def __init__(self):
        self.front_node = None
        self.rear_node = None

    def enqueue(self, x):
        n = SLLNode(x)
        if not self.rear_node:
            self.front_node = self.rear_node = n
        else:
            self.rear_node.next = n
            self.rear_node = n

    def dequeue(self):
        if self.front_node:
            self.front_node = self.front_node.next
            if not self.front_node:
                self.rear_node = None

    def front(self):
        if self.front_node:
            return self.front_node.data
        return -1


def check_parentheses(s):
    st = []
    for c in s:
        if c in "({[":
            st.append(c)
        else:
            if not st:
                return False
            t = st[-1]
            if (c == ")" and t != "(") or (c == "}" and t != "{") or (c == "]" and t != "["):
                return False
            st.pop()
    return len(st) == 0


da = DynamicArray()
da.append(1)
da.append(2)
da.append(3)
da.pop()
da.display()

sll = SLL()
sll.insert(10)
sll.insert(20)
sll.display()

dll = DLL()
dll.insert(5)
dll.insert(15)
dll.display()

st = Stack()
st.push(1)
st.push(2)
st.pop()
print(st.top())

q = Queue()
q.enqueue(7)
q.enqueue(8)
q.dequeue()
print(q.front())

print(check_parentheses("({[]})"))