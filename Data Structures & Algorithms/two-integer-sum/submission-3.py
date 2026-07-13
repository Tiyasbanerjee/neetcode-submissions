class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        privious_seens = []
        # we can also use list, dict is just for faster shearch .
        for i,num in enumerate(nums):

            other_num_should_be = target - num
            
            for p in privious_seens: # cheaking if we have encountered before
                x,y=p[0],p[1] # its a list inside a list


                if other_num_should_be == x: 
                    return [y,i]
                
            privious_seens.append([num,i]) # storeing the value in the list as [[key,value]...]
        
        # this solution and the 1st solution has no diffrence, even its worse .
        # but the diffrence is that this is cheaking history insted of forrowed
        # priviously we were doing [a,b,c,d] -> ab , ac, ad | bc , bd | cd
        # we were reduceing , like cheaking all praiers with all elements after it 
        # here what we are doing is cheaking it over all privious privious_seens
        # its like ab | bc , ac | ad , bd , cd
        # same thing but reverse...