class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = Counter(nums)


        s = res.most_common(k)
        lste = []
        for item in s:
            lste.append(item[0])
        return lste

        

        