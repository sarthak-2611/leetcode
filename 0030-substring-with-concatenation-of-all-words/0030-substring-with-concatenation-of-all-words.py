from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words: return []
        w_len, w_cnt, req, res = len(words[0]), len(words), Counter(words), []
        for i in range(w_len):
            l, r, curr, count = i, i, Counter(), 0
            while r + w_len <= len(s):
                w = s[r:r + w_len]
                r += w_len
                if w in req:
                    curr[w] += 1
                    count += 1
                    while curr[w] > req[w]:
                        curr[s[l:l + w_len]] -= 1
                        count -= 1
                        l += w_len
                    if count == w_cnt:
                        res.append(l)
                else:
                    curr.clear()
                    count, l = 0, r
        return res