from SinglyLinkedList3 import *

class Deque:
    def __init__(self):
        self.start = None
        self.items = 0
    
    def is_empty(self):
        return SLL.is_empty(self=self)
    
    def insert_front(self, data):
        self.items += 1
        SLL.insert_at_last(self=self, data=data)
    
    def insert_rear(self, data):
        self.items += 1
        SLL.insert_at_start(self=self, data=data)
    
    def delete_front(self):
        if self.is_empty():
            return None
        
        else:
            self.items -= 1
            return SLL.delete_last(self=self)
    
    def delete_rear(self):
        if self.is_empty():
            return None

        else:
            self.items -= 1
            return SLL.delete_first(self=self)
    
    def get_front(self):
        front = self.start
        while front.next is not None:
            front = front.next
        return front
    
    def get_rear(self):
        return self.start

    def size(self):
        return self.items


mydeque = Deque()
mydeque.insert_front(10)