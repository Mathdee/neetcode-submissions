class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = Counter(nums) #builds frequency map

        #Create buckets where the index = frequency
        # index 0 is not used, so max frequency is len(nums); we do len(nums) + 1 to get that.
        bucket = [[] for _ in range(len(nums)+ 1)]

        for num, freque in res.items():
            bucket[freque].append(num)

        # Go through the buckets backward to find top k 
        lis = []
        for i in range(len(bucket)- 1, 0, -1):
            for num in bucket[i]:
                lis.append(num)
                if len(lis) == k:
                    return lis 






        