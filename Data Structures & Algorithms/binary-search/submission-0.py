class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        #mid=(low+high)//2
        def part(low,high,target):
            if low>high:
                return -1
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                return part(low,mid-1,target)
            else:
               return part(mid+1,high,target)
        return part(low,high,target)