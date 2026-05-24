import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = "".join(filter(lambda c: c in set(string.ascii_letters + string.digits), s))
        ss = re.sub(r"[^A-Za-z0-9]", "", s).lower()
        if len(ss) <= 1:
            return True

        l, r = 0, len(ss) - 1
        while l <= r:
            if ss[l] != ss[r]:
                return False
            l += 1
            r -= 1
        return True
