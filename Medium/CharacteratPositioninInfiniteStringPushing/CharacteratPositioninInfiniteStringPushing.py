class Solution:
    def posInfinite(self, s: str, pos: int) -> str:
        base_len = len(s)
        if pos <= base_len:
            return s[pos - 1]

        cur_len = base_len
        prev_lens = []
        step = 0

        while cur_len < pos:
            step += 1
            prev_lens.append(cur_len)
            cur_len = 2 * cur_len + step

        for k in range(step, 0, -1):
            prev_len = prev_lens[k - 1]
            if pos <= prev_len:
                continue
            elif pos <= prev_len + k:
                return '$'
            else:
                offset = pos - (prev_len + k)
                pos = prev_len - offset + 1

        return s[pos - 1]