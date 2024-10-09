from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        for s in strs:
            # Sort each string and use it as a key
            sorted_str = ''.join(sorted(s))
            anagrams[sorted_str].append(s)
        
        # Return all the values in the hash map (i.e., lists of anagrams)
        return list(anagrams.values())
    
        
o = Solution()
print(o.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))