class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # build a list of s , which will look like, [element,element...]
        # we will then ittrate through t's elements, if element matches any element of the list, 
        # we will delete the list before it, makeing it shorter.
        # then we will do counter+=1
        # if counter == len(t) return true
        counter = 0
        for i in s:
            for j in range(len(t)):
                if i == t[j]:
                    t = t[j+1:]
                    counter+=1
                    break
              
        if len(s) == counter:
            return True
        else:
            return False