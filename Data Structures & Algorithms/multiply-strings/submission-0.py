class Solution:
    def multiply(self, num1: str, num2: str) -> str:
    
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        # The max possible length of the result is m + n
        result = [0] * (m + n)
        
        # Traverse both strings from right to left (backwards)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                
                # Multiply single string characters as integers
                multiply = int(num1[i]) * int(num2[j])
                
                # The positions in our result array
                # p1 is for the carry, p2 is for the single digit
                p1 = i + j
                p2 = i + j + 1
                
                # Add the multiplication to whatever is already at p2 (from previous calculations)
                current_sum = multiply + result[p2]
                
                # Put the single digit at p2
                result[p2] = current_sum % 10
                
                # Carry the tens digit over to p1
                result[p1] += current_sum // 10
                
        # The result array might have a leading zero (e.g., [0, 8, 1])
        # Convert list of ints to a string and strip any leading zeros
        result_str = "".join(map(str, result)).lstrip("0")
        
        return result_str