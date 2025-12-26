class Stack(list):  #Stack(list) means, extending the list class, and creating a new class named Stack. So stack is child class and list is parent class
    def is_empty(self):
        return len(self) == 0
    
    def push(self, data):
        self.append(data)

    def pop(self):
        if self.is_empty():
            return None
        
        else:
            super().pop()

            #Here list class has a function pop, and we are creating a function with same name in Stack class, so while calling that function for object of Stack class, the function of Stack class will be used instead of stack class

            # And to get over from that kind of situations, we use super(), which tells to use the function or parent class instead of Stack class

    def peek(self):
        if self.is_empty():
            return None
        
        else:
            print(f"Top element: {self[-1]}")

    def size(self):
        print("Size of Stack is ", self.size())
    

    def insert(self, index, object):
        raise AttributeError(r'No attibute name "insert" in Stack')

myStack = Stack()
myStack.push(10)
myStack.push(20)
myStack.push(30)
myStack.push(40)
myStack.peek()
myStack.pop()
myStack.peek()