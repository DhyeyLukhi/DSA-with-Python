class ProrityQueue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, data, proirity=10):
        if self.is_empty():
            self.items.append((data, proirity))
        
        else:
            index=0
            while index<len(self.items) and self.items[index][1] <= proirity:
                index+= 1

            self.items.insert(index, (data, proirity))

    def pop(self):
        if self.is_empty():
            return None
        
        else:
            return self.items.pop(0)
        
    def size(self):
        return len(self.items)


myProQueue = ProrityQueue()
myProQueue.push(2, 1)
print(myProQueue.items)
myProQueue.push(3, 4)
myProQueue.push(10, 0)
print(myProQueue.items)
print(myProQueue.pop())
print(myProQueue.items)