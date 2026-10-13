class Solution:
    def reverse(self, x: int) -> int:
        def recursion(num,rev):
            if num == 0:
                return rev

            digit = num%10
            num = num//10
            rev = rev*10 + digit

            return recursion(num,rev)
        
        sign = 1 if x>0 else -1

        res = recursion(abs(x),0)


        return res*sign if res <= 2**31-1 else 0



        