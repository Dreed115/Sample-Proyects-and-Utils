class LinkedStack:

    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def push(self, e):
        self.head = self._Node(e, self.head)
        self.size += 1

    def top(self):
        if self.is_empty():
            raise "Linked List empty"
        
        return self.head._element
    
    def pop(self):
        if self.is_empty():
            raise "Linked List Empty"
        answer = self.head._element
        self.head = self.head._next
        self.size -= 1
        return answer
    
L = LinkedStack()

L.push("a")
L.push(10)
L.push(True)
L.push(10.0)

print(L.top())
print(len(L))
print(L.is_empty())

print(L.pop())
