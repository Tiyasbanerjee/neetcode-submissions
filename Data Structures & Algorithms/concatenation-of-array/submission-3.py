class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = list(nums)
        ans.extend(nums)
        return ans
        