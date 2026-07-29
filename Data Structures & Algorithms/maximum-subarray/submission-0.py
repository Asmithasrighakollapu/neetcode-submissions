class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum=nums[0]
        maxi_sum=nums[0]
        for i in range(1,len(nums)):
            if(curr_sum+nums[i]>nums[i]):
                curr_sum=curr_sum+nums[i]
            else:
                curr_sum=nums[i]
            if curr_sum>maxi_sum:
                maxi_sum=curr_sum
        return maxi_sum