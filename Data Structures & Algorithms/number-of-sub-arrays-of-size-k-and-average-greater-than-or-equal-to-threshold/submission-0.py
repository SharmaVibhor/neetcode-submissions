class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        sum = 0
        l = 0

        for i in range(len(arr)):
            avg = 0
            if i < k-1:
                sum+=arr[i]
                continue
            elif i == k-1:
                sum+= arr[i]
                avg = sum//k
            else:
                sum += arr[i]
                sum -= arr[l]
                l = l+1
                avg = sum/k
            
            if avg >=threshold:
                res+=1
        
        return res


        