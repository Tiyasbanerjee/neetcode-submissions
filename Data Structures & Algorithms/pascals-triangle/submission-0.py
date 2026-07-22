class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        main_list = []
        holder = [1]
        for i in range(numRows):
            main_list.append(holder)
            
            x=[]
            pre = 0

            for i in holder+[0]:
                x.append(pre+i)
                pre = i
            
            holder = x
        
        return main_list