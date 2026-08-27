class Solution:
    def reverseBits(self, n: int) -> int:
        res=[]
        num=0
        n=format(n,'032b')
        for i in range(len(n)):
            res.append(n[-(i+1)])
        num=int(''.join(res),2)  
        return num