class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) == 2:
            return min(heights) ** 2
        
        p1, p2 = 0, len(heights) - 1 
        ans = 0
        while p1 < p2:
            ans = max(min(heights[p1], heights[p2]) * (p2 - p1), ans)
            if heights[p1] > heights[p2]:
                p2 -= 1
            else:
                p1 += 1                

        return ans

