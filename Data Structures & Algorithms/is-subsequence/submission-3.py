class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_pointer, s_pointer = 0 , 0
        count = 0
        while t_pointer<len(t) and s_pointer<len(s):
            
            if s[s_pointer] == t[t_pointer]:
                s_pointer+=1
                count+=1
            
            t_pointer+=1

        return count == len(s)