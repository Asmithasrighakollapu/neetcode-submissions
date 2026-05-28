class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=""
        for i in range(len(s)):
            if s[i].isalnum():
                n+=s[i]
        n=n.lower()
        l=0
        h=len(n)-1
        while l<h and l!=h:
            if n[l]!=n[h]:
                return False
            else:
                l+=1
                h-=1
        return True

        