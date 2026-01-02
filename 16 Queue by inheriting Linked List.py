from SinglyLinkedList3 import *

class Queue(SLL):
    def __init__(self):
        super().__init__()
        self.items = 0
    
    def is_empty(self):
        return super().is_empty()

    def enqueue(self, data):
        self.insert_at_last(data=data)
        self.items += 1
    
    def dequeue(self):
        if self.is_empty():
            return None

        else:
            removed = self.start
            self.delete_first()
            self.items -= 1
            return removed
    
    def get_front(self):
        if self.is_empty():
            return None

        else:
            front = self.start
            while front.next is not None:
                front = front.next
            
            return front

    def get_rear(self):
        return self.start

    def size(self):
        return self.items
    


myqueue = Queue()
print(myqueue.is_empty())
myqueue.enqueue(10)
print(myqueue.is_empty())
print(myqueue.get_front().data)