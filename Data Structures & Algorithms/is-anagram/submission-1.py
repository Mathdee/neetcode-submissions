class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seens = {}
        seent = {}

        for char in s:
            if char in seens:
                seens[char] +=1
            else:
                seens[char] = 1
        for char1 in t:
            if char1 in seent:
                seent[char1] +=1
            else:
                seent[char1] = 1
        
        if seens == seent:
            return True
        else:
            return False

            
        