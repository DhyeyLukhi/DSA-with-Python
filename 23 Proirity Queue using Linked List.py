class Node:
    def __init__(self, data=None, priority=10, next=None):
        self.data = data
        self.priority = priority
        self.next = next


class ProrityQueu:
    def __init__(self, start=None):
        self.start = start
        self.items = 0
    
    def is_empty(self):
        return self.start is None
    
    def push(self, data, priority):
        newNode = Node(data=data, priority=priority)
        if self.start is None or self.start.priority > priority:
            newNode.next = self.start
            self.start = newNode
        
        else:
            temp = self.start
            while temp.next is not None and temp.next.priority <= priority:
                temp = temp.next
            
            newNode.next = temp.next
            temp.next = newNode
        
    def pop(self):
        if self.is_empty():
            return None
        
        else:
            remove = self.start
            self.start = self.start.next
            self.items -= 1
            return remove
    
    def size(self):
        return self.items

myprioqueu = ProrityQueu()
myprioqueu.is_empty()
myprioqueu.push(20, 2)
myprioqueu.push(10, 1)
myprioqueu.push(30, 3)