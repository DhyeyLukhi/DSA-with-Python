class Deque(list):
    def __init__(self):
        super().__init__()
    
    def is_empty(self):
        return len(self) == 0
    
    def insert_front(self, data):
        self.insert(0, data)
        
    def insert_rear(self, data):
        self.append(data)
    
    def delete_front(self):
        if self.is_empty():
            return None
        
        else:
            return self.pop(0)
        
    def delete_rear(self):
        if self.is_empty():
            return None
        
        else:
            return self.pop()

    def get_front(self):
        if self.is_empty():
            return None
        
        else:
            return self[0]
        
    def get_rear(self):
        if self.is_empty():
            return None
        
        else:
            return self[-1]

    def size(self):
        return len(self)


mydeque = Deque()
print(mydeque.insert_front(10))
# print(mydeque.is_empty())
print(mydeque.insert_front(20))
print(mydeque.insert_front(30))
print(mydeque.insert_rear(5))
print(mydeque.delete_front())
print(mydeque.get_front())
print(mydeque.get_rear())