class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0:
            print("Stack is empty")
        
    def push(self, data):
        self.items.append(data)

    def pop(self):
        if self.is_empty():
            raise IndexError("")
        
        else:
            self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("")

        else:
            print(f"{self.items[-1]}")

    def size(self):
        if self.is_empty():
            return 0
        
        else:
            print(f"The size of Stack is {len(self.items)}")

mystack = Stack()
mystack.is_empty()
mystack.push(1)
mystack.push(2)
mystack.push(3)
mystack.push(4)
mystack.peek()
mystack.pop()
mystack.peek()
mystack.size()