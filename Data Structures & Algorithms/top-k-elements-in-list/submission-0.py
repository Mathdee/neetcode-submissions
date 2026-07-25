class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = Counter(nums)
        tuples = res.most_common(k)
        answer = [item[0] for item in tuples ]
        return answer


        