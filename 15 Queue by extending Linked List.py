from SinglyLinkedList3 import *

class Queue:
    def __init__(self):
        self.queue = SLL()
        self.items = 0
    
    def is_empty(self):
        return self.queue.is_empty()
    
    def enqueue(self, data):
        self.queue.insert_at_last(data=data)
        self.items += 1
    
    def dequeue(self):
        if self.is_empty():
            return None
        
        else:
            self.items -= 1
            removed = self.queue.start
            self.queue.delete_first()
            return removed
    
    def get_front(self):
        if self.is_empty():
            print("Queue is Empty")
        
        else:
            front = self.queue.start
            while front.next is not None:
                front = front.next

            return front

    def get_rear(self):
        if self.is_empty():
            print("Queue is Empty")
        
        else:
            return self.queue.start

    def size(self):
        return self.items


myqueue = Queue()
# myqueue.is_empty()
# print(myqueue.get_front())
myqueue.dequeue()
myqueue.enqueue(10)
myqueue.enqueue(20)
myqueue.enqueue(30)
print(myqueue.dequeue().data)
# myqueue.dequeue()
# myqueue.dequeue()
print(myqueue.get_front().data)
print(myqueue.get_rear().data)
print(myqueue.size())