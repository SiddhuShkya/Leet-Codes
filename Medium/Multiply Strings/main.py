def multiply(num1, num2):
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    int_num1 = 0
    int_num2 = 0

    for i in range(len(num1)):
        j = 0
        while num1[i] != nums[j]:
            j += 1
        int_num1 = int_num1*10 + j

    for i in range(len(num2)):
        j = 0
        while num2[i] != nums[j]:
            j += 1
        int_num2 = int_num2*10 + j
    
    return str(int_num1*int_num2)

print(multiply('132', '431'))
