class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Deque:
    def __init__(self):
        self.rear = None
        self.front = None
        self.items = 0
    
    def is_empty(self):
        return self.rear is None

    def insert_front(self, data):
        new = Node(data=data)
        if self.is_empty():
            self.front = self.rear = new
        
        else:
            self.front.next = self.front = new
        self.items += 1
    
    def insert_rear(self, data):
        new = Node(data=data)
        if self.is_empty():
            self.rear = self.front = new
        
        else:
            new.next = self.rear
            self.rear = new
        self.items += 1

    def delete_front(self):
        if self.is_empty():
            return None
        
        else:
            temp = self.rear
            while temp.next is not None:
                temp = temp.next
            removed = self.front
            self.front = temp
            temp.next = None
            self.items -= 1
            return removed
    
    def delete_rear(self):
        if self.is_empty():
            return None
        
        else:
            removed = self.rear
            self.rear = self.rear.next
            self.items -= 1
            return removed

    def get_front(self):
        return self.front

    def get_rear(self):
        return self.rear

    def size(self):
        return self.items
    

mydeque = Deque()
mydeque.is_empty()
mydeque.delete_front()
mydeque.insert_front(10)
mydeque.insert_front(20)
mydeque.insert_front(30)
# print(mydeque.delete_rear().data)
print(mydeque.size())