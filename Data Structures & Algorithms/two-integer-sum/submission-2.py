class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        privious_seens = {}
        # we are useing dict to make the shearch a little faster then ittration
        # because here we will find the key not ittrate through
        for i,num in enumerate(nums):

            other_num_should_be = target - num
            
            if other_num_should_be in privious_seens:
                return [privious_seens[other_num_should_be],i]
            else:
                privious_seens[num] = i