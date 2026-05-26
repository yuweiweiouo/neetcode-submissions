
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t in s:
            return t

        l, r = 0, 0
        q = deque()
        puzzle = t
        started = False
        min_matched = ""

        while r < len(s):
            # l,r 不停往右 直到找到第一個目標
            if not started:
                head, c, tail = puzzle.partition(s[r])
                if c != "":
                    puzzle = head + tail
                    started = True
                    l = r
                r += 1
                continue

            print(s[l : r + 1], min_matched, puzzle, q)
            # 找到後 l 停下, r 繼續往右，如果遇到重複的 那就讓 l 往右回到原本的第二個目標
            head, c, tail = puzzle.partition(s[r])
            if c == "":
                if s[r] in t:
                    for i, v in enumerate(list(q)):
                        if s[v] == s[r]:
                            del(q[i])
                    q.append(r)
                if s[l] == s[r]:
                    l = q.popleft()
            else:
                puzzle = head + tail
                q.append(r)

            if len(puzzle) == 0:
                min_matched = s[l : r + 1]
                puzzle += s[l]
                l = q.popleft()

            r += 1
            if min_matched != "" and r - l + 1 > len(min_matched):
                if len(q)> 0:
                    puzzle += s[l]
                    l = q.popleft()
                else:
                    l +=1
        return min_matched
