import sys

class Solution:
    def reverse(self, x: int) -> int:
        # Define 32-bit integer bounds
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Extract sign and work with absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reverse the integer
        rev = 0
        while x != 0:
            pop = x % 10
            x = x // 10
            
            # Check for overflow before adding the digit
            if rev > INT_MAX // 10:
                return 0
            
            rev = rev * 10 + pop
        
        # Apply sign and check final overflow
        result = sign * rev
        if result < INT_MIN or result > INT_MAX:
            return 0
            
        return result


# Test cases
sol = Solution()

# Test case 1: Positive number
print(f"reverse(123) = {sol.reverse(123)}")  # Expected: 321

# Test case 2: Negative number
print(f"reverse(-123) = {sol.reverse(-123)}")  # Expected: -321

# Test case 3: Trailing zeros
print(f"reverse(120) = {sol.reverse(120)}")  # Expected: 21

# Test case 4: Overflow case
print(f"reverse(1534236469) = {sol.reverse(1534236469)}")  # Expected: 0 (overflow)

# Test case 5: Edge case - zero
print(f"reverse(0) = {sol.reverse(0)}")  # Expected: 0