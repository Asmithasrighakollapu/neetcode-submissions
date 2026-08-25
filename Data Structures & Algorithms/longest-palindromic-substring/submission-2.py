class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        dp=[]
        start=0
        maxilen=1
        for i in range(len(s)):
            row=[]
            for j in range(len(s)):
                row.append(False)
            dp.append(row)
        for i in range(len(s)):
            dp[i][i]=True
        for length in range(2,len(s)+1):
            for i in range(n-length+1):
                j=i+length-1
                if s[i]==s[j] and(length<=2 or dp[i+1][j-1]):
                    dp[i][j]=True
                    if length>maxilen:
                        start=i
                        maxilen=length
        return s[start:start+maxilen]

        