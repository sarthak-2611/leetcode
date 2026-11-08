class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        for d in num:
            while k and st and st[-1] > d:
                st.pop()
                k -= 1
            st.append(d)
        return "".join(st[:-k] if k else st).lstrip("0") or "0"

        