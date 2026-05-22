class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        l = [v[0] for v in sorted(d.items(), key=lambda x: x[1], reverse=True)]
        return l[0:k]
