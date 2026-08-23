from SinglyLinkedList3 import *

class Stack(SLL):
    def __init__(self):
        super().__init__()
        self.item_count = 0
    def is_empty(self):
        if super().is_empty():
            print("Stack is empty")
        
        else:
            return
    
    def push(self, data):
        self.insert_at_start(data=data)
        self.item_count += 1
    
    def pop(self):
        if super().is_empty():
            print("Stack is empty")

        else:
            self.delete_first()
            self.item_count -= 1

    def peek(self):
        if super().is_empty():
            print("Stack is Empty")
        
        else:
            print(f"Top Element is {self.start.data}")

    def size(self):
        print(f"Size of Stack is {self.item_count}")
    

mystack = Stack()
mystack.is_empty()
mystack.push(10)
mystack.push(20)
mystack.push(30)
mystack.push(40)
mystack.is_empty()
mystack.peek()
mystack.pop()
mystack.peek()