class Queue:
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

myQueue = Queue()
myQueue.enqueue(10)
myQueue.enqueue(20)
myQueue.enqueue(30)
myQueue.enqueue(40)
print(myQueue.get_front())
print(myQueue.get_rear())
myQueue.dequeue()
myQueue.dequeue()
print(myQueue.get_front())
print(myQueue.get_rear())
print(myQueue.size())
