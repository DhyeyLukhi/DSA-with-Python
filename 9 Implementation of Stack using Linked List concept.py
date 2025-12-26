class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self, start=None):
        self.start = start
        self.item_count = 0
        self.head = start

    def is_empty(self):
        return self.item_count == 0
    
    def push(self, data):
        newNode = Node(data=data)
        if self.is_empty():
            self.head = self.start = newNode
            
        
        else:
            self.head.next = newNode
            self.head = newNode
        
        self.item_count += 1
    
    def pop(self):
        if self.is_empty():
            print("Stack is empty, nothing to remove")
        
        else:
            temp = self.start
            while temp.next is not self.head:
                temp = temp.next
            
            temp.next = None
            self.head = temp
            self.item_count -= 1
    
    def peek(self):
        if self.is_empty():
            print("Stack is Empty, there is nothing")

        
        else:
            print(f"The top element is {self.head.data}")


    def size(self):
        if self.is_empty():
            print("Stack is Empty")

        else:
            print(f"Size of Stack is {self.item_count}")
        
        
    



myStack = Stack()
myStack.push(data=10)
myStack.push(data=20)
myStack.push(data=30)
myStack.push(data=40)
myStack.size()
myStack.peek()
myStack.pop()
myStack.peek()
myStack.size()