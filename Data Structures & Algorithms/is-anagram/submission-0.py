class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()

        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        
        for c in t:
            found = d.get(c)
            if found is None:
                d[c] = -1
            if found == 1:
                del d[c]
            else:
                d[c] -= 1
        
        return not d


