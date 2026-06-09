class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        leng=len(digits)
        tot=0
        for num in digits:
            tot=tot*10+num
        tot=tot+1 
        l=[]
        while(tot>0):
            rem=tot%10
            l.append(rem)
            tot=tot//10
        l.reverse()
        return l

        