class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            s.add(n)
        
        maxSeq = 0
        for n in nums:
            seq = 1
            t = n + 1
            while t in s:
                seq += 1
                t += 1
            maxSeq = max(maxSeq, seq)
        return maxSeq
        

        