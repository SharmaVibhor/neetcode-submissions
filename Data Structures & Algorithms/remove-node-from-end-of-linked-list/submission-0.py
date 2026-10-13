# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        t1 = head
        t2 =dummy= ListNode(0,head)

        for i in range(n):
            t1 = t1.next
        
        while(t1):
            t1 = t1.next
            t2 = t2.next

        t2.next = t2.next.next

        return dummy.next
        