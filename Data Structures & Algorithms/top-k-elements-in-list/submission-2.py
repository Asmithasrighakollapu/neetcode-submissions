class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        res=[]
        for i in range(k):
            maxi=-1
            ele=0
            for key in d:
                if d[key]>maxi:
                    maxi=d[key]
                    ele=key
            res.append(ele)
            del d[ele]
        return res
            