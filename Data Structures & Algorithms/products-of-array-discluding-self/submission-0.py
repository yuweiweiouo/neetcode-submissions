class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCnt = 0
        total = None 
        for n in nums:
            if n == 0:
                zeroCnt += 1
            elif total is None:
                total = n
            else:
                total *= n
        result = list()
        for n in nums:
            if n == 0:
                if zeroCnt == 1:
                    result.append(total)
                else:
                    result.append(0)
            else:
                if zeroCnt > 0:
                    result.append(0)
                else:
                    result.append(total // n)
        return result