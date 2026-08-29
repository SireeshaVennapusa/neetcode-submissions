class Solution:
    def reverse(self, x: int) -> int:
        temp=abs(x)
        rev=0
        MAX=2147483647
        MIN=-2147483648          
        while temp>=1:
               rem=temp%10
               rev=rev*10+rem
               temp//=10
        if rev > MAX  or rev < MIN :
            return 0       
        elif x>0:
            return rev
        else:
            return -rev         



