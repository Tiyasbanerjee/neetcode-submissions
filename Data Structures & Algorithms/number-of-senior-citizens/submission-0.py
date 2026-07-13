class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for passenger in details:
            age = int(passenger[11])*10 + int(passenger[12])
            if age>60:
                count+=1
        return count