class Solution:
    def isValid(self, s: str) -> bool:
        lst=[]
        top=-1
        for sym in s:
            if sym=='[' or sym=='{' or sym=='(':
                lst.append(sym)
                top+=1
            
            elif sym==']' or sym=='}' or sym==')':
                if top==-1:
                    return False
                if(sym==')' and lst[top]=='(') or (sym ==']' and lst[top]=='[')or (sym =='}' and lst[top]=='{'):
                    lst.pop()
                    top-=1
                else:
                    return False   
        return top==-1                
