def addBinary(a, b):
    # Initialize an empty string to hold the result
    res = ''
    # Reverse the input strings
    a = a[::-1]
    b = b[::-1]
    # Initialize a carry variable to 0
    carry = 0
    # Loop through the digits of the longer input string
    for i in range(max(len(a), len(b))):
        # Get the i-th digit of each input string, or 0 if it doesn't exist
        da = int(a[i]) if i < len(a) else 0
        db = int(b[i]) if i < len(b) else 0
        # Add the digits and the carry from the previous iteration
        total = da + db + carry
        # Calculate the current digit and add it to the result string
        ch = total % 2
        res = str(ch) + res
        # Update the carry for the next iteration
        carry = total//2
    # If there is a carry after the final iteration, add it to the result string
    if carry == 1:
        res = "1" + res  
    # Return the final result string
    return res
# Example usage
print(addBinary('110', '111'))  # Output: '1101'
