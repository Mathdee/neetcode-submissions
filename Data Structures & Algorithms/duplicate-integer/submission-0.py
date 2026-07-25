class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        count = 0
        for i,value in enumerate(nums):
            if value in seen:
                return True
            else:
                seen[value] = i
                
        return False