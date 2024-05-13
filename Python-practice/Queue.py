class ArrayQueue:
    default_capacity = 10
    def __init__(self):
        self.data = [None]*ArrayQueue.default_capacity
        self.size = 0
        self.front = 0

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def first(self):
        if self.is_empty():
            raise "Queue Empty"
        
        return self.data[self.front]
        

    def dequeue(self):
        if self.is_empty():
            raise "Queue Empry"
        
        answer = self.data[self.front]
        self.data[self.front] = None
        self.front = self.front+1 % (len(self.data))
        self.size -= 1
        return answer
    
    def enqueue(self, a):
        if self.size == len(self.data):
            self.resize(2*len(self.data)
                        )
        avail = (self.front + self.size) % len(self.data)
        self.data[avail] = a
        self.size += 1

    def resize(self, size):
        old = self.data
        self.data = [None]*size
        walk = self.front
        for k in range(self.size):
            self.data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self.front = 0

Q = ArrayQueue()
Q.enqueue(5)
Q.enqueue(5)
print(len(Q))
print(Q.dequeue())
print(Q.is_empty())   
print(Q.dequeue())
print(Q.is_empty())
Q.enqueue(7)
Q.enqueue(9)
print(Q.first())
Q.enqueue(4)
print(len(Q))
print(Q.dequeue())