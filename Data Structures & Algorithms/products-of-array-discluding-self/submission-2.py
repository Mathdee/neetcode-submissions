class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            rest = nums[:i] + nums[i+1:]
            mul = math.prod(rest)
            res.append(mul)
        return res


        