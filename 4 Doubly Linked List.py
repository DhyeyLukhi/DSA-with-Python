class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.prev = prev
        self.data = data
        self.next = next

class DLL:
    def __init__(self, start=None):
        self.start = start
    
    def is_empyt(self):
        if not self.start:
            return self.start==None
    

    def insert_start(self, dataOnNode):
        newNode = Node(data=dataOnNode, next=self.start)
        if not self.is_empyt():
            self.start.prev = newNode
            self.start = newNode
        
        else:
            self.start = newNode


    def insert_last(self, dataOnNode):
        if self.is_empyt():
            newNode = Node(data=dataOnNode)
            self.start = newNode
        
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            newNode = Node(data=dataOnNode, prev=temp)
            temp.next = newNode

    
    def insert_after(self, datafter, dataOnNode):
        temp = self.start
        if self.is_empyt():
            print("Doubly Lined List is empy")
            return None
        
        else:
            while temp is not None:
                if temp.data == datafter:
                    newNode = Node(data=dataOnNode, next=temp.next, prev=temp)
                    temp.next.prev = newNode
                    temp.next = newNode
                temp = temp.next

    
    def search(self, target):
        temp = self.start
        while temp is not None:
            if temp.data == target:
                return temp
            else:
                temp = temp.next
        return None

    def delete_first(self):
        if self.is_empyt():
            print("There is nothing to remove")
        
        else:
            self.start = self.start.next
            if self.start is None:
                pass

            else:
                self.start.prev.next = None
                self.start.prev = None
    
    def delete_last(self):
        if self.is_empyt():
            print("There is nothing to remove")
        
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            
            if temp.prev is None:
                self.start = None
            else:
                temp.prev.next = None
                temp.prev = None
    
    def delete_item(self, dataToDelete):
        found = self.search(dataToDelete)
        if found:
            if found.next is not None and found.prev is not None:        
                found.prev.next = found.next
                found.next.prev = found.prev
                found.next = found.prev = None
            elif found.next is None:
                self.delete_last()
            elif found.prev is None:
                self.delete_first()
            
        else:
            print("Item not found in the Doubly Linked List")


    def showDLL(self):
        temp = self.start
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next

    def __iter__(self):
        return DLLIterate(self.start)


class DLLIterate:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        
        data = self.current.data
        self.current = self.current.next
        return data
        



dll = DLL()
dll.is_empyt()
dll.insert_start(dataOnNode=30)
dll.insert_start(dataOnNode=20)
dll.insert_start(dataOnNode=10)
dll.insert_last(dataOnNode=40)
dll.insert_after(dataOnNode=25, datafter=20)
# find = dll.search(40)
# print(find)
# dll.delete_first()
# dll.delete_last()
dll.delete_item(dataToDelete=30)
dll.showDLL()

for x in dll:
    print(x)


if __name__ == '__main__':
    pass