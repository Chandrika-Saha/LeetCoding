class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = {}
        for i in nums:
            d[i] = 1 + d.get(i, 0)

        ds = dict(sorted(d.items(), key= lambda item: -item[1]))
        print(ds)

        return list(ds.keys())[:k]