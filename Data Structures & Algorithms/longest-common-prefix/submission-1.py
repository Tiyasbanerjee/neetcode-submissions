class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # even though privious could fail if the characters somehow avarage to the value we asked for.
        # 1st we can split the list and find avarage of both sides and cheak if they are same.. 
        # still it could fail
        # and other option if to loop and cheak every element
        # we can smartly add this...

        min_len_str =  min(map(len,strs))
        a_global_str = ""

        for i in range(min_len_str): 
            point_value = strs[0][i] # i did this insted of doing pre_value="" , is because of some effecineny
            
            for k in strs:
                if k[i] != point_value:
                    return a_global_str

            # if this process ends without breaking means that char is same at everywhere, so add it
            a_global_str += point_value
            
            
        # this is here for safety, say we have , ["ab","ab"] , then for no char our if will activate and return, 
        # then this return will do the work...
        return a_global_str