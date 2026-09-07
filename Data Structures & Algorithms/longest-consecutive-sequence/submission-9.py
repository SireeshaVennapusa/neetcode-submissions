class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lst=list(set(nums))
        lst.sort()
        #lst=set(lst)
        count=1
        max_count=0
        if len(lst)==0:
            return 0
        for i in range(1,len(lst)):
            
            if lst[i]-1==lst[i-1]:
                
                max_count=max(max_count,count)
                count+=1

            else:
                    count=1
                     
        return max_count+1            

