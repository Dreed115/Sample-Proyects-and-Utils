class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)
    
    def is_empty(self):
        return len(self.data) == 0
        
    def push(self, a):
        self.data.append(a)

    def pop(self):
        if self.is_empty():
            raise "Empty Stack"
        
        return self.data.pop()

    def top(self):
        if self.is_empty():
            raise "Empty Stack"
        
        return self.data[-1]
    
S = ArrayStack()
S.push(5)
S.push(3)
print(len(S))
print(S.pop())
print(S.is_empty())
print(S.pop())
print(S.is_empty())
S.push(7)
S.push(9)
print(S.top())
S.push(4)
print(len(S))
print(S.pop())
S.push(6)