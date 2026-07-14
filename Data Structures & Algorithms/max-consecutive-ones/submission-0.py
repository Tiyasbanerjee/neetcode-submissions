class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        # this logic is working but except if the last element is 1, because its 1 , 
        # our program is not getting a chance to update the max_element
        # i can add a extra 0 at the end of the list, it will not affect anything 

        nums.append(0)
        count = 0
        max_element = 0

        for i in nums:
        
            if i:
                count+=1
        
            else:

                if count==0:
                    continue
                else:
        
                
                    if count>max_element:
                        max_element = count
                    
                    count = 0
        

        return max_element