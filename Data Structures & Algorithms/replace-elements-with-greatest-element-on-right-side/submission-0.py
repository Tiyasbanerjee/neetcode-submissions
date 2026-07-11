class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = -1
        pre_i = 0
        
        for i in range(len(arr)-1, -1 , -1):
            p = arr[i]
            arr[i] = right_max
            pre_i = p
            
            if pre_i > right_max:
                right_max = pre_i
        
        return arr
