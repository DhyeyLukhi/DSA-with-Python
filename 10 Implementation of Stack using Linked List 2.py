from SinglyLinkedList3 import *

class Stack:
    def __init__(self):
        self.mylist = SLL()
        self.items = 0

    def is_empty(self):
        return self.mylist.is_empty()

    def push(self, data):
        self.mylist.insert_at_last(data=data)
        self.items += 1

    def pop(self):
        if self.mylist.is_empty():
            print("Stack is Empty")
        
        else:
            self.mylist.delete_last()
            self.items -= 1

    def peek(self):
        if self.mylist.is_empty():
            print("Stack is Empty")
        
        else:
            temp = self.mylist.start
            while temp.next is not None:
                temp = temp.next
            print(temp.data)
            return temp
    
    def size(self):
        print(f"Size of Stack is {self.items}")



mystack = Stack()
mystack.pop()
mystack.push(10)
mystack.push(20)
mystack.push(30)
mystack.push(40)
mystack.size()
mystack.peek()
mystack.pop()
mystack.peek()
mystack.size()