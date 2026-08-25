class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        res=0
        if len(height)==2:
            mini=min(height[0],height[1])
            ans=1*mini
            return ans
        while(left<right):
            width=right-left
            mini=min(height[left],height[right])
            ans=width*mini
            if ans>res:
                res=ans
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return res
            

        