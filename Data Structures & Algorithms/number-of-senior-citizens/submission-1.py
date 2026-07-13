class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for passenger in details:
        
            if 60 < int(passenger[11:12+1:1]):
                count+=1
        
        return count