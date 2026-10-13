class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)]+=1
        

    def count(self, point: List[int]) -> int:
        res = 0
        px,py = point[0],point[1]
        for p in self.points:
            x,y=p[0],p[1]
            if(abs(py-y)!=abs(px-x) or x==px or y==py):
                continue
            
            res += self.points[p]*self.points.get((x,py),0)*self.points.get((px,y),0)
        
        return res
