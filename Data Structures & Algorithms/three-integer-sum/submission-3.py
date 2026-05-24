class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
        d = defaultdict(set)
        for i, n in enumerate(nums):
            d[n].add(i)
        tried = set()
        l = list()
        for i in range(len(nums) - 1):
            for ii in range(i + 1, len(nums)):
                tp2 = tuple(sorted([nums[i] , nums[ii]]))
                if tp2 in tried:
                    continue
                tried.add(tp2)
                for iii in d[(-(nums[i] + nums[ii]))]:
                    sl3 = sorted([nums[i],nums[ii],nums[iii]])
                    tp3 = tuple(sl3)
                    if tp3 in tried:
                        continue                    
                    if i != iii and ii != iii:
                        l.append(sl3)                        
                        tried.add(tp3)
                        break

        return l





