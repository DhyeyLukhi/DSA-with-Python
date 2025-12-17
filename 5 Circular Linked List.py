class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class CLL:
    def __init__(self, last=None):
        self.last = last
    
    def __iter__(self):
        if self.last.next:
            return CllIterator(self.last.next)
        else:
            return CllIterator(None)
    
    def is_empty(self):
        if self.last == None:
            return True
        
        else:
            return False
    
    def insert_start(self, data):
        if self.is_empty():
           newNode = Node(data=data)
           self.last = newNode
           self.last.next = newNode
        else:
            newNode = Node(data=data, next=self.last.next)
            self.last.next = newNode

    def insert_last(self, data):
        if self.is_empty():
            self.insert_start(data=data)
        
        else:
            newNode = Node(data=data, next=self.last.next)
            self.last.next = newNode
            self.last = newNode

    
    def insert_after(self, data, dataAfter):
        node = self.search(target=dataAfter)
        if node:
            if node == self.last:
                self.insert_last(data=data)
            else:
                newNode = Node(data=data, next=node.next)
                node.next = newNode
        
        else:
            print("Node not found")


    
    def search(self, target):
        temp = self.last
        if temp.data == target:
            return temp
        else:
            temp = temp.next
            while temp is not self.last:
                if temp.data == target:
                    return temp
                else:
                    temp = temp.next
            return None

    def delete_first(self):
        if self.is_empty():
            return None
        else:
            if self.last.next == self.last:
                self.delete_last()
            else:
                newFirst = self.last.next.next
                self.last.next.next = None
                self.last.next = newFirst
    
    def delete_last(self):
        if self.is_empty():
            return None

        else:
            
            temp = self.last
            while temp.next is not self.last:
                temp = temp.next
            if temp == self.last:
                self.last = None
                return None
            else:
                temp.next = self.last.next
                self.last.next = None
                self.last = temp
        
    def delete_item(self, data):
        if self.is_empty():
            return None
        
        else:
            temp = self.last
            while temp.next.data is not data:
                temp = temp.next
            if temp.next == self.last.next:
                self.delete_first()
            elif temp.next == self.last:
                self.delete_last()
            else:
                tempo = temp.next
                temp.next = tempo.next
                tempo.next = None
                


    def show(self):
        if self.is_empty():
            return None
        
        temp = self.last.next
        print(temp.data, end=' ')
        while temp is not self.last:
            temp = temp.next
            print(temp.data, end=' ')
        print()

class CllIterator:
    def __init__(self, start):
        self.current = start
        self.first = start
        self.count = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if None == self.current:
            raise StopIteration
        
        if self.current == self.first and self.count == 1:
                raise StopIteration
        else:
            self.count = 1
        
        data = self.current.data
        self.current = self.current.next
        return data
        


cll = CLL()
print(cll.is_empty())
cll.insert_start(data=30)
cll.insert_start(data=20)
cll.insert_last(data=40)
cll.insert_last(data=50)
cll.insert_after(data=25, dataAfter=20)
cll.show()
# cll.delete_last()
cll.delete_item(data=50)
cll.show()

