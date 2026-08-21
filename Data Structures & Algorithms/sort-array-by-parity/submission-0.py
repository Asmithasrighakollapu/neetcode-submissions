class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left=0
        right=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right+=1
            else:
                right+=1
        return nums
        