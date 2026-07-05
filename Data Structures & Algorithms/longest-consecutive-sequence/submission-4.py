class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums=sorted(set(nums))
        if not nums:
            return 0
        c=1
        longest=1
        for i in range(1,len(nums)):
            if(nums[i]==nums[i-1]+1):
                c+=1
            else:
                c=1
            if(c>longest):
                longest=c
        return longest


            
        