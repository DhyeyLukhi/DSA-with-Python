class Queue(list):
    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
            return None
        
        else:
            return self.queue.pop(0)
    
    def get_front(self):
        return self.queue[-1] if not self.is_empty() else None
    
    def get_rear(self):
        return self.queue[0] if not self.is_empty() else None

    def size(self):
        return len(self.queue)
    

myqueue = Queue()
myqueue.dequeue()
myqueue.enqueue(10)
myqueue.enqueue(20)
myqueue.enqueue(30)
myqueue.enqueue(40)
print(myqueue.size())
myqueue.dequeue()
print(myqueue.size())