class Solution:
    def countSubstrings(self, s: str) -> int:
        dp=[]
        for i in range(len(s)):
            row=[]
            for j in range(len(s)):
                row.append(False)
            dp.append(row)
        c=0
        for i in range(len(s)):
            dp[i][i]=True
            c+=1
        for length in range(2,len(s)+1):
            for i in range(len(s)-length+1):
                j=length+i-1
                if(s[i]==s[j] and (length<=2 or dp[i+1][j-1])):
                    dp[i][j]=True
                    c+=1
                    
        return c

        
        