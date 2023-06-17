def majorityElement(nums):
    hp = {}
    l = len(nums)//2
    for num in nums:
        if num not in hp:
            hp[num] = 1
        else:
            hp[num] += 1
    
    for k,v in hp.items():
        if v > l:
            return k