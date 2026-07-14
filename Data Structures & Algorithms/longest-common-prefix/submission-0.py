class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        min_len_str =  min(map(len,strs))
        len_of_list = len(strs)
        a_global_str = ""

        for i in range(min_len_str): # prifix cannt be bigger than the smallest word...
            a_list = [] 
            
            for k in strs:
                a_list.append(k[i])

            if sum(map(ord, a_list)) == ord(a_list[0]) * len_of_list:
                a_global_str+=a_list[0]
               
                # the idea is that if we have n p's like
                # [p,p,p...] , then its avrage should be euqal to p.
                # avrage = (add all p's) and devide with the length = (n*p)/n = p 
            
            
            else:
                # if any of the element fails , its no more prifix, so break.
                break
        
        return a_global_str