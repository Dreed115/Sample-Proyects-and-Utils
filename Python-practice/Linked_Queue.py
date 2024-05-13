class CircularQueue:
    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def first(self):
        if self.is_empty():
            raise "Queue is empty"
        
        head = self.tail._next
        return head._element
    
    def dequeue(self):
        if self.is_empty():
            raise "Queue is empty"
        
        oldhead = self.tail._next
        if self.size == 1:
            self.tail = None
        else:
            self.tail._next = oldhead._next
        self.size -= 1
        return oldhead._element
    
    def enqueue(self, a):
        new = self._Node(a, None)
        if self.is_empty():
            new._next = new
        else:
            new._next = self.tail._next
            self.tail._next = new
        self.tail = new
        self.size += 1

    def rotate(self):
        if self.size > 0:
            self.tail = self.tail._next
        
