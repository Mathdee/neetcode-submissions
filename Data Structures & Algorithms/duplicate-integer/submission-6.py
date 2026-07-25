class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for i, val in enumerate(nums):
            if val in seen:
                return True

            seen[val] = i
        return False
        
        '''
        Time complexity: O(n)
        Dictionnary has O(1) lookup, but we traverse the list until we hit True, 
        or traverse the whole list until false. so that gives us O(n), linear time.
        '''