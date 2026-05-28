class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(len(nums)):
            ans=1
            for j in range(len(nums)):
                if i!=j:
                    ans=ans*nums[j]
            l.append(ans)
        return l
            
        