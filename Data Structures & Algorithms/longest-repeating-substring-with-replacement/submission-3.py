class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1:
            return len(s)

        max_repeated_count = 0
        l, r = 0, 0

        while r < len(s):
            # 符合目標子串 就向右推
            curr_len = r - l + 1
            cnt = Counter(s[l : r + 1]).most_common(1)[0][1]
            if cnt + k >= curr_len:
                max_repeated_count = max(max_repeated_count, curr_len)
                r += 1
            elif max_repeated_count >= curr_len:
                r += 1
            else:
                l += 1
        return max_repeated_count