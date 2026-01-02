class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.start = None
        self.items = 0
        self.rear = None

    def is_empty(self):
        return self.start == None
    
    def enqueue(self, data):
        newNode = Node(data=data)
        if self.is_empty():
            self.start = newNode
            
        else:
            self.rear.next = newNode
        
        self.rear = newNode   
        self.items += 1
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
        
        else:
            removed = None
            removed = self.start
            self.start = self.start.next
            self.items -= 1
            return removed

    def get_front(self):
        if self.is_empty():
            return None
        
        else:
            front = self.start
            while front.next is not None: front = front.next
            
            return front

    def get_rear(self):
        return self.start
    
    def size(self):
        return self.items


myqueu = Queue()
myqueu.dequeue()
myqueu.get_front()
print(myqueu.size())
myqueu.enqueue(10)
myqueu.enqueue(20)
myqueu.enqueue(30)
myqueu.enqueue(40)
print(myqueu.size())
myqueu.dequeue()
print(myqueu.size())
print(myqueu.get_front().data)
print(myqueu.get_rear().data)