class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for ch in strs:
            sorteds=''.join(sorted(ch))
            if sorteds not in d:
                d[sorteds]=[]
            d[sorteds].append(ch)
        return list(d.values())


        