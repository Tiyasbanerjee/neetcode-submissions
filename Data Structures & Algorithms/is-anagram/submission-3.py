class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t) and sum([ord(i) for i in s]) == sum([ord(i) for i in t]):
            
            if sorted(s) == sorted(t):
                return True
            else:
                return False

        else:
            return False