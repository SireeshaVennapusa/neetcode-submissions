class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        count=0
        for i in range(n+1):
            b=bin(i)
            count=b.count('1')
            res.append(count)
        return res    