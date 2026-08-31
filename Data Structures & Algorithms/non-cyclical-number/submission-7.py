class Solution:
    def isHappy(self, n: int) -> bool:
        lst=[]
        while n not in lst:
            lst.append(n)
            tot=0
            while(n>0):
                rem=n%10
                tot=tot+(rem*rem)
                n//=10
            n=tot        
            if tot==1:
                return True
        return False
             
            
        
                  
         

        
                   