class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,max_len=0,0
        se=set()
        for r in range(len(s)):
            while s[r] in se:
              se.remove(s[l])
              l+=1
            w=(r-l)+1    
            max_len=max(max_len,w)
            se.add(s[r])
        return max_len    
         

                            