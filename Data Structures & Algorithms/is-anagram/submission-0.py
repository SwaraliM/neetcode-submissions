class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s = {}
        counts_t = {}
        if len(s) != len(t): 
            return False
        for char in s:
            counts_s[char] = counts_s.get(char, 0) + 1
        for char in t:
            counts_t[char] = counts_t.get(char, 0) + 1
        
        if counts_s == counts_t:
            return True
        return False
        

        