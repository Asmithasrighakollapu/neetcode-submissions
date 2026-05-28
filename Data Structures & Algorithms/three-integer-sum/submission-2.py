class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l1=[]
        nums.sort()
        for i in range(len(nums)-2):
            l=i+1
            h=len(nums)-1
            while l<h:
                tot=nums[i]+nums[l]+nums[h]
                if tot==0:
                    temp=[nums[i],nums[l],nums[h]]
                    if temp not in l1:
                        l1.append(temp)
                    l+=1
                    h-=1
                elif tot>0:
                    h-=1
                else:
                    l+=1
        return l1


        