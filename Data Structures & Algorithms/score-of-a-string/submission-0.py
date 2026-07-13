class Solution:
    def scoreOfString(self, s: str) -> int:
        sum_ = 0
        for i in range(len(s)-1):
            value1 = ord(s[i])
            value2 = ord(s[i+1])
            sum_ += abs(value1-value2)
        return sum_