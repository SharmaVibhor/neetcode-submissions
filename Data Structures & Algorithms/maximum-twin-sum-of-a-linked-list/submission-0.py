# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        cur = slow
        prev = None
        temp = cur

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        res = 0
        
        while prev and head:
            res = max(prev.val+head.val, res)
            prev = prev.next
            head = head.next

        if prev:
            res = max(res,cur.val)
        return res
        