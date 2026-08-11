class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l=[]
        k=0
        for i in range(len(s)):
            for j in range(k,len(t)):
                if s[i]==t[j]:
                    l.append(j)
                    k=j+1
                    break
    
        if len(s)==len(l):
            return True
        else:
            return False
        