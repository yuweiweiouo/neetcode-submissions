class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1:
            return len(s)
            
        count = {}  # 用來記錄目前視窗內各字元的出現次數
        max_f = 0   # 目前視窗內「出現次數最多」的字元的頻率
        l = 0
        max_len = 0
        
        for r in range(len(s)):
            # 1. 將右指標移入的字元加入計數
            count[s[r]] = count.get(s[r], 0) + 1
            # 2. 更新目前視窗中最多字元的數量
            max_f = max(max_f, count[s[r]])
            
            # 3. 檢查目前視窗是否合法
            # (目前視窗長度 - 出現最多的字元數量) > k，代表需要替換的字元超過 k 個，視窗不合法
            if (r - l + 1) - max_f > k:
                count[s[l]] -= 1  # 左指標字元移出視窗
                l += 1            # 縮小視窗
                
            # 4. 更新最大長度
            max_len = max(max_len, r - l + 1)
            
        return max_len