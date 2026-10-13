# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newNode = ListNode()
        curr = newNode
        tens = 0

        if not l1:
            return l2
        
        if not l2:
            return l1

        while l1 or l2 or tens:
            digits = (l1.val if l1 else 0) + (l2.val if l2 else 0) + tens
            if digits >= 10:
                ones = digits - 10
                tens = 1
            else:
                ones = digits
                tens = 0

            curr.next = ListNode(ones)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return newNode.next
        