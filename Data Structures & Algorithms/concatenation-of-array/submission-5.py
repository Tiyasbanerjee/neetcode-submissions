class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        ans = [0 for i in range(length*2)] # or create a list of length 2n

        # map the numbers

        for i,j in enumerate(nums):
            ans[i] = j
            ans[i+length] = j 

        return ans
        