class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        t = ord(target)
        diff = []
        for char in letters:
            if ord(char) > t:
                diff.append(ord(char) - t)
            else:
                diff.append(30)
        if not diff:
            return ""
        idx = diff.index(min(diff))
        return letters[idx]