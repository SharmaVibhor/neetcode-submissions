# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        if len(lists)==1:
            return lists[0]

        def merge_helper(node1,node2):
            if not node1:
                return node2
            if not node2:
                return node1
            
            temp = ListNode(0)
            cur = temp

            while node1 and node2:
                if node1.val < node2.val:
                    cur.next = node1
                    node1=node1.next
                else:
                    cur.next = node2
                    node2=node2.next
                
                cur = cur.next
            
            if node1:
                cur.next = node1
            
            if node2:
                cur.next = node2

            return temp.next
        
        while len(lists)>1:
            merged = []

            for i in range(0,len(lists),2):
                l1 = lists[i]

                l2 = lists[i+1] if i+1 < len(lists) else None

                merged.append(merge_helper(l1,l2))
                
            lists = merged

        return lists[0]
        