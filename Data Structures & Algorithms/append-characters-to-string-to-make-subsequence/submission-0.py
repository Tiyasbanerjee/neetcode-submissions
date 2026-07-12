class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # i am noticeing that if we have some t , the elements of it should obay the order
        # of the elements in the string s, means we can add two pointers, 
        # pointing one to our string t , because we are cheaking on t to make it 
        # contain the character order of t.
        # and we will move the pointer every time it hits the same element in s or we
        # will move the pointer in s. and if we have reached all the way to the end of s 
        # but still missing the element then we will return the length of the rest of the 
        # string of t which have been unmatched includeing the point pointer is pointing
        # and return length. 
        pointer_t = 0
        pointer_s = 0
        while pointer_s<len(s) and pointer_t<len(t):
            if t[pointer_t] == s[pointer_s]:
                pointer_t+=1
            
            pointer_s+=1
        
        return len(t)-pointer_t