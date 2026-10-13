class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 1
        l = 0
        r = 1
        sign = ""

        while r < len(arr):
            if arr[r-1] > arr[r] and sign!= ">":
                res = max(res,r-l+1)
                r +=1
                sign = ">"
            elif arr[r-1] < arr[r] and sign != "<":
                res = max(res,r-l+1)
                r+=1
                sign = "<"
            else:
                sign = ""
                if arr[r-1] == arr[r]:
                    r+=1
                l = r - 1
        
        return res
        