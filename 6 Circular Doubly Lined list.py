class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class CDll:
    def __init__(self, start=None):
        self.start = start
    
    def is_empty(self):
        if self.start == None:
            return True
        else:
            return False

    def insert_start(self, data):
        if self.is_empty():
            newNode = Node(data=data)
            newNode.prev = newNode
            newNode.next = newNode
            self.start = newNode
        
        # only one node in list when start.next == start
        elif self.start.next == self.start:
            newNode = Node(prev=self.start, data=data, next=self.start)
            self.start.prev = newNode
            self.start.next = newNode
            self.start = newNode
        
        else:
            newNode = Node(prev=self.start.prev, data=data, next=self.start)
            self.start.prev.next = newNode
            self.start.prev = newNode
            self.start = newNode

    def insert_last(self, data):
        if self.is_empty():
            self.insert_start(data=data)
        
        elif self.start.prev == self.start:
            newNode = Node(prev=self.start, data=data, next=self.start)
            self.start.prev = self.start.next = newNode
        
        else:
            newNode = Node(prev=self.start.prev, data=data, next=self.start)
            self.start.prev.next = self.start.prev = newNode


    def insert_after(self, data, dataAfter):
        if self.is_empty():
            print("List is empty")
            return None
        else:
            datanode = self.search(target=dataAfter)
            if datanode:
                newNode = Node(prev=datanode, data=data, next=datanode.next)
                datanode.next.prev = newNode
                datanode.next = newNode
            
            else:
                return None
    
    def search(self, target):
        temp = self.start
        while True:
            if temp.data == target:
                print("Node found")
                return temp
            else:
                temp = temp.next
                if temp is self.start:
                    print("Node isn't present in the list")
                    return None
    
    def delete_first(self):
        if self.start.next == self.start:
            self.start = None
        
        else:
            self.start.prev.next = self.start.next
            self.start.next.prev = self.start.prev
            self.start = self.start.next
    
    def delete_last(self):
        if self.start.next == self.start:
            self.start = None
        
        else:
            self.start.prev.prev.next = self.start
            self.start.prev = self.start.prev.prev


    def delete_item(self, to_delete):
        if self.start.next == self.start and self.start.data == to_delete:
            self.start = None
        
        else:
            delnode = self.search(target=to_delete)
            if delnode:
                
                delnode.prev.next = delnode.next
                delnode.next.prev = delnode.prev
                delnode.next = delnode.prev = None
                temp = None

        
    def show(self):
        if self.is_empty():
            print("List is empty")
            return
        temp = self.start
        while True:
            print(temp.data)
            temp = temp.next
            if temp == self.start:
                break
        
    def __iter__(self):
        CDLLIterator(self)


class CDLLIterator:
    def __init__(self, start):
        self.current = self.start
        self.temp = self.start
    def __iter__(self):
        return self

    def __next__(self):
        if self.is_empty():
            print("There is nothing in the list")
        data = self.data
        self.current = self.current.next
        if self.current == self.temp:
            return None
        else:
            return data
        
    

cdll = CDll()
# print(cdll.is_empty())
cdll.insert_start(data=40)
cdll.insert_start(data=30)
cdll.insert_last(data=50)
cdll.insert_start(data=20)
cdll.insert_after(data=25, dataAfter=20)
cdll.delete_item(to_delete=30)
# cdll.search(target=50)
# cdll.delete_last()
cdll.show()
