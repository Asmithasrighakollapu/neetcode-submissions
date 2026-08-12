class Solution:
    def countSeniors(self, details: List[str]) -> int:
        l=[]
        for i in range(len(details)):
            l.append(details[i][-4:-2])
        c=0
        for i in range(len(l)):
            if int(l[i])>60:
                c+=1
        return c

        