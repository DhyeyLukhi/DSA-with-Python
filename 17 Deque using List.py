class Deque:
    def __init__(self):
        self.deque = []
    
    def is_empty(self):
        return len(self.deque) == 0
    
    def insert_front(self, data):
        self.deque.insert(0, data)
        
    def insert_rear(self, data):
        self.deque.append(data)
    
    def delete_front(self):
        if self.is_empty():
            return None
        
        else:
            return self.deque.pop(0)
        
    def delete_rear(self):
        if self.is_empty():
            return None
        
        else:
            return self.deque.pop()

    def get_front(self):
        if self.is_empty():
            return None
        
        else:
            return self.deque[0]
        
    def get_rear(self):
        if self.is_empty():
            return None
        
        else:
            return self.deque[-1]

    def size(self):
        return len(self.deque)
