class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        
        def count(list_):

            contener = {}

            for i in list_:

                if i in contener:
                    contener[i]+=1
                else:
                    contener[i] = 1
            
            return contener
        
        if count(s) == count(t):
            return True
        else:
            return False
        
