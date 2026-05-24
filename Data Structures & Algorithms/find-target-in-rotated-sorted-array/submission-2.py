class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) <= 5:
            for i, n in enumerate(nums):
                if n == target:
                    return i
        
        l, r = 0, len(nums) - 1
       
        
        while l < r:
            mid = (l + r) // 2
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:
                if nums[l] < target and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target and target < nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1

