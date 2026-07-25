class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seens = Counter(s)
        seent = Counter(t)

        if seens == seent:
            return True
        else:
            return False