class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)

        ans = max(count.items(), key = lambda x: x[1])
        return ans[0]