
def is_valid(s):
    if len(s) % 2 == 0:
        stack = []
        pairs = {'(': ')', '{': '}', '[': ']'}
        for bracket in s:
            if bracket in pairs.keys():
                stack.append(bracket)
            elif stack == [] and bracket != pairs[stack.pop()]:
                return False
        return stack == []
    else:
        return False


print(is_valid('(){[]}'))
