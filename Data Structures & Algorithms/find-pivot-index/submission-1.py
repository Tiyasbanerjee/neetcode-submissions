class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        pre = 0
        length = len(nums)
        
        for i in range(length):
            
            next_pointer_on = nums[i]

            left_sum += pre
            right_sum -= next_pointer_on

            if left_sum == right_sum:
                return i

            pre = next_pointer_on
        
        return -1