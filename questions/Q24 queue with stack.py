class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        if not self.queue:
            self.queue.insert(0, x)
            return

        tempstack = [x]
        while self.queue:
            tempstack.insert(0, self.queue.pop(0))

        for i in range(len(tempstack),0):
            self.queue.insert(0, tempstack[i])


    def pop(self) -> int:
        return self.queue.pop(0)        

    def peek(self) -> int:
        return self.queue[0] if self.queue else None

    def empty(self) -> bool:
        return False if self.queue else True


obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()


"""
Stack:
Addition: Front
Deletion: Front
Restrictions: cannot see bottom elements
cannot slice elements

Queue:
Addition: Read
Deletion: Front
"""