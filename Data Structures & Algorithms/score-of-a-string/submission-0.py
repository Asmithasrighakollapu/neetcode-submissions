class Solution:
    def scoreOfString(self, s: str) -> int:
        sums=0
        for i in range(1,len(s)):
            sums=sums+abs(ord(s[i])-ord(s[i-1]))
        return sums
        