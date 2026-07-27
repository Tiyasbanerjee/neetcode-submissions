class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        lis = []
        privios = -999
        su = 0

        for i in nums:
            if i>privios:
                su += i
            else:
                lis.append(su)
                su = i
            privios = i
        
        lis.append(su)
        return max(lis)