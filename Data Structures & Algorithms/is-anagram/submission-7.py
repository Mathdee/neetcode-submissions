class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        inS = {}
        inT = {}

        for c in s:
            if c in inS:
                inS[c] += 1
            else:
                inS[c] = 1
        for c in t:
            if c in inT:
                inT[c] += 1
            else: inT[c] = 1
        
        return inT == inS




        