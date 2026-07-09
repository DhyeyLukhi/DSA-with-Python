# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    
class Solution:
    def mergeTwoLists(self, l1, l2):
        mark1, mark2 = l1, l2
        head = ListNode()
        point = head
        while True:
            
            if mark1 and mark2:
                if mark1.val <= mark2.val:
                    point.next = mark1
                    point = point.next
                    if head is None:
                        head = mark1
                    mark1 = mark1.next
                
                else:
                    point.next=mark2
                    point = point.next
                    if head is None:
                        head = mark2
                    mark2 = mark2.next

            elif mark1:
                point.next = mark1
                point = point.next
                if head is None:
                        head = mark1
                mark1 = mark1.next

            elif mark2:
                point.next=mark2
                point = point.next
                if head is None:
                        head = mark2
                mark2 = mark2.next
            
            elif mark1 is None and mark2 is None:
                break

        return head.next



test = Solution()
n11=ListNode()
n12=ListNode()
n13=ListNode()
n14=ListNode()
n15=ListNode()
n16=ListNode()
n11.val=1;n11.next=n12
n12.val=2;n12.next=n13
n13.val=3;n13.next=n14
n14.val=4;n14.next=n15
n15.val=5;n15.next=n16
n16.val=6;n16.next=None


n21=ListNode()
n22=ListNode()
n23=ListNode()
n24=ListNode()
n25=ListNode()
n26=ListNode()
n21.val=2;n21.next=n22
n22.val=4;n22.next=n23
n23.val=5;n23.next=n24
n24.val=7;n24.next=n25
n25.val=8;n25.next=n26
n26.val=9;n26.next=None
ans = test.mergeTwoLists(l1=n11, l2=n21)
while ans is not None:
    print(ans.val)
    ans = ans.next