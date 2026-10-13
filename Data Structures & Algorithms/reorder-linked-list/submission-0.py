# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        secondList = slow.next
        prev = None
        slow.next = None        

        while(secondList):
            temp = secondList.next
            secondList.next = prev
            prev = secondList
            secondList = temp
        
        secondList = prev


        while secondList:
            temp1,temp2 = head.next,secondList.next
            head.next = secondList
            secondList.next = temp1
            head,secondList = temp1,temp2