import time

start = time.perf_counter()


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SLL:
    def __init__(self):
        self.start = None

    def insert(self, value):
        node = ListNode(val=value)
        if not self.start:
            self.start = node

        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next

            temp.next = node

        return self.start
            


class Solution:
    def middleNode(self, head=None):
        temp = head
        items = []
        while temp is not None:
            items.append(temp)
            temp = temp.next

        size = len(items)
        return items[size//2]

link = SLL()
point = link.insert(1)
link.insert(2)
link.insert(3)
link.insert(4)
link.insert(5)

test = Solution()
ans = test.middleNode(head=point)
print(f"Answer is {ans}")

end = time.perf_counter()
print(f"Time taken is {((end-start)*1000):.6f} ms")