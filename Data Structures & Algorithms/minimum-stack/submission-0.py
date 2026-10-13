class MinStack:

    def __init__(self):
        self.elements = []
        self.min_elements = []
        

    def push(self, val: int) -> None:
        self.elements.append(val)
        if self.min_elements:
            tmp = min(val,self.min_elements[-1])
            self.min_elements.append(tmp)
        else:
            self.min_elements.append(val)
        

    def pop(self) -> None:
        self.elements.pop()
        self.min_elements.pop()
        

    def top(self) -> int:
        return self.elements[-1]
        

    def getMin(self) -> int:
        return self.min_elements[-1]
        
