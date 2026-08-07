
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SLL:
    def __init__(self):
        self.start = None

    def insert(self, val):
        if self.start is None:
            node = ListNode(val=val)
            self.start = node
            return self.start

        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next

            node = ListNode(val=val)
            temp.next = node
            return self.start

    def iterate(self):
        temp = self.start
        while temp.next is not None:
            print(temp.val)
            temp = temp.next
        print(temp.val)

class Solution:
    def deleteDuplicates(self, head):
        if head is None:
            return None

        temp = head
        temp2 = head.next

        while temp2 is not None:
            if temp.val == temp2.val:
                temp.next = temp2.next
                temp2 = temp2.next
            else:
                temp = temp.next
                temp2 = temp2.next

        return head

            
        

sll = SLL()
head = sll.insert(1)
sll.insert(1)
sll.insert(2)
sll.insert(3)
sll.insert(3)
sll.insert(4)
sll.insert(4)

test = Solution()

ans = test.deleteDuplicates(head=head)