class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #nums.sort()
        for num in nums:
            idx=abs(num)-1
            if nums[idx]<0:
                return abs(num)
            nums[idx]=-nums[idx]
        return -1    