class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        if len(s)!= len(t):
            return False

        a={}
        for i in s:
            if i in a :
                a[i]+=1
            else:
                a[i]=1

        b={}
        for i in t:
            if i in b :
                b[i]+=1
            else:
                b[i]=1


        if a == b:
            return True
        return False
