"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy = {None:None}
        if not head:
            return head
        cur = head
        while(cur):
            temp = Node(cur.val)
            copy[cur] = temp
            cur = cur.next
        
        cur = head
        while cur:
            temp = copy[cur]
            temp.next = copy[cur.next]
            temp.random = copy[cur.random]
            cur = cur.next
        
        return copy[head]

        