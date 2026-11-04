class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.curSize = 0
        self.head = None
        self.rear = None
        
    def enQueue(self, value: int) -> bool:
        if self.curSize == self.capacity:
            return False
        
        if self.curSize == 0:
            self.head = ListNode(value)
            self.rear = self.head
            self.curSize +=1
        else:
            cur = self.rear
            cur.next = ListNode(value)
            self.curSize +=1
            self.rear = cur.next

        return True
        
    def deQueue(self) -> bool:
        if self.curSize == 0:
            return False
        
        self.head = self.head.next
        self.curSize -= 1

        if self.curSize == 0:
            self.rear = None

        return True
        

    def Front(self) -> int:
        if self.curSize!=0:
            return self.head.val
        return -1

    def Rear(self) -> int:
        if self.curSize!=0:
            return self.rear.val
        return -1
        

    def isEmpty(self) -> bool:
        return self.curSize == 0
        

    def isFull(self) -> bool:
        return self.curSize == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()