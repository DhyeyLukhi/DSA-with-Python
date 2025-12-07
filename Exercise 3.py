class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SLL:
    def __init__(self, start=None):
        self.start=start
    
    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self, data):
        new_Node = Node(data, self.start)
        self.start=new_Node
    
    def insert_at_last(self, data):
        new_Node = Node(data)
        if self.is_empty():
            self.start=new_Node
        
        else:
            temp = self.start
            while(temp.next != None):
                temp = temp.next
            
            temp.next = new_Node
        

    def search(self, value):
        temp = self.start
        while temp is not None:
            if temp.data == value:
                return temp
            else:
                temp = temp.next
        print(f"Value {value} not found in the Linked List")
        return None

    def insert_after(self, data, value_after):
        temp = self.start
        while temp is not None:
            if temp.data == value_after:
                new_Node = Node(data=data, next=temp.next)
                temp.next = new_Node
                return  # insert after the first matching node and exit
            temp = temp.next

    def showSLL(self):
        temp = self.start
        while temp is not None:
            print(f"{temp.data}", end=' ')
            temp = temp.next
        print()
    
    def delete_first(self):
        if self.start is None:
            print('List is already empty')
            return
        self.start = self.start.next

    def delete_last(self):
        if self.start == None:
            pass
        elif self.start.next is None:
            self.start = None
        
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
    
    def delete_item(self, value):
        if self.is_empty():
            pass
        
        elif (self.start.next == None) and (self.start.data == value):
            self.start = None
        
        else:
            temp = self.start
            if self.start.data == value:
                self.start = self.start.next
            else:
                while temp.next is not None:
                    if temp.next.data == value:
                        temp.next = temp.next.next
                        return None
                    temp = temp.next                  
        
        


# Test Cases
sll = SLL()
sll.insert_at_start(20)
sll.insert_at_last(30)
sll.insert_at_start(10)
sll.insert_after(data=25, value_after=20)
sll.showSLL()
#sll.delete_first()
# sll.delete_last()
sll.delete_item(value=20)
sll.showSLL()
