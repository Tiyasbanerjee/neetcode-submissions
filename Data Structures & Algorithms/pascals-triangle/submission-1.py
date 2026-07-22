class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        main_list = []
        holder = [1]
        for i in range(numRows):
            main_list.append(holder)
            
            x=[]
            pre = 0

            for val in holder+[0]:
                x.append(pre+val)
                pre = val
            
            holder = x
        
        return main_list