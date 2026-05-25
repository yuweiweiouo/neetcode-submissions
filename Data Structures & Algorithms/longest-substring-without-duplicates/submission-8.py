# s 為 ASCII  
# 0 <= s.len <= 1000
# 
# 貪婪思路, 慢指針
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        if len(s) == 2:
            if s[0] == s[1]:
                return 1
            else:
                return 2

        max_substring = 0
        seen_letter_dict = dict()

        cursor = 0
        for i, c in enumerate(s):
            # 判斷局部最優終點
            # 出現重複的字元
            if c in seen_letter_dict and seen_letter_dict[c] >= cursor:
                # 當前長度 [cursor, i)
                max_substring = max(max_substring, i - cursor)
                cursor = seen_letter_dict[c] + 1
            # 如果是最後的話強制結算
            elif i == len(s) - 1: 
                # 長度 [cursor, i]
                max_substring = max(max_substring, i - cursor + 1)
                break
                
            seen_letter_dict[c] = i

        return max_substring
            
        
