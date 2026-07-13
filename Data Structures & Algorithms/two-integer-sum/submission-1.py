class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        
        for i in range(length-1):
            num1=nums[i]
            
            for j in range(i+1,length):
                
                if num1 + nums[j] == target:
                    return [i,j]
                