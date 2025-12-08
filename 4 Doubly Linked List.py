class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DLL:
    def __init__(self, start):
        self.start = start
    
    def is_empyt(self):
        if not self.start:
            print("DLL is Empty")

newn = Node(data=10)
dll = DLL(newn)
dll.is_empyt()


if __name__ == '__main__':
    pass