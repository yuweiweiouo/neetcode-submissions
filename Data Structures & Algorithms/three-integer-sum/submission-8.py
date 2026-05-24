class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
        d = defaultdict(set)
        for i, n in enumerate(nums):
            d[n].add(i)
        
        s = set()
        for i in range(len(nums) - 1):
            for ii in range(i + 1, len(nums)):                
                for iii in d[(-(nums[i] + nums[ii]))]:
                    if i != iii and ii != iii:
                        n3 = sorted([nums[i],nums[ii],nums[iii]])
                        s.add(tuple(n3))
                        break

        return [*s]





