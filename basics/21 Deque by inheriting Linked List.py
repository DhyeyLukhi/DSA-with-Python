from SinglyLinkedList3 import *

class Deque(SLL):
    def __init__(self, start=None):
        super().__init__(start)
        self.items = 0
    
    def is_empty(self):
        return super().is_empty()
    
    def insert_front(self, data):
        self.items += 1
        return super().insert_at_last(data=data)

    def insert_rear(self, data):
        self.items += 1
        return super().insert_at_start(data=data)

    def delete_front(self):
        if self.is_empty():
            return None
        
        else:
            self.items -= 1
            return super().delete_last(self=self)
    
    def delete_rear(self):
        if self.is_empty():
            return None
        
        else:
            self.items -= 1
            return super().delete_first(self=self)
        
    def get_front(self):
        front = self.start
        while front.next is not None:
            front = front.next
        
        return front

    def get_rear(self):
        return self.start

    def size(self):
        return self.items
    
