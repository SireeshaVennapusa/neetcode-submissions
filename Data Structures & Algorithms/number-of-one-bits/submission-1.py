class Solution:
    def hammingWeight(self, n: int) -> int:
        binary=format(n,'032b')
        count=binary.count('1') 
        return count
        

