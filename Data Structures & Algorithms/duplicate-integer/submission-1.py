class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(1,len(nums)):
            nums.sort()
            if nums[i]==nums[i-1]:
                return True
        else:
            return False        