class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        fir=0
        last=len(numbers)-1
        while fir<last:
            if numbers[fir]+numbers[last]==target:
                return [fir+1,last+1]
            elif numbers[fir]+numbers[last]>target:
                last-=1
            else:
                fir+=1
                       
