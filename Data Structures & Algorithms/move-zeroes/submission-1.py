class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l=0
        r=0
        while l<len(nums) and r<len(nums):
            if nums[r]==0:
                r+=1
            else:
                temp=nums[l]
                nums[l]=nums[r]
                nums[r]=temp
                l+=1
                r+=1
        return nums

        