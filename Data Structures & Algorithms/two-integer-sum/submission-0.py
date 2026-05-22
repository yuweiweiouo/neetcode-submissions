class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()

        for i, n in enumerate(nums):
            wanted = target - n
            if wanted in d:
                return sorted([i, d[wanted]])
            
            if n not in d:
                d[n] = i
        
        return [0,0]
            