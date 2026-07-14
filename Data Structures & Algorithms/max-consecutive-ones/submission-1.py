class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxim = 0
        for i in nums:
            if i:
                count+=1
            else:
                count = 0
            maxim = max(count,maxim)
        return maxim