class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        tot=sum(nums)
        n_sum=(n*(n+1)//2)
        if n_sum==tot:
            return 0
        else:
            return n_sum-tot
