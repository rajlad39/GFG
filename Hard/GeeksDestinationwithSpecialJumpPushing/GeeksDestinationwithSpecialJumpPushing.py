class Solution:
    def minTime(self, a: int, b: int, d: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = a - b

        def get_t(x: int) -> int:
            if x <= a:
                return x
            k = (x - b - 1) // m
            return x + 2 * b * k

        def floor_div_sum(n: int, div: int) -> int:
            if n < 0:
                return 0
            t, rem = divmod(n, div)
            return div * t * (t - 1) // 2 + (rem + 1) * t

        def sum_t_range(lo: int, hi: int) -> int:
            if lo > hi:
                return 0
            total = 0
            if lo <= a:
                end_linear = min(hi, a)
                cnt = end_linear - lo + 1
                total += cnt * (lo + end_linear) // 2
                lo = end_linear + 1
            if lo <= hi:
                cnt = hi - lo + 1
                total += cnt * (lo + hi) // 2
                s1 = lo - b - 1
                s2 = hi - b - 1
                k_sum = floor_div_sum(s2, m) - floor_div_sum(s1 - 1, m)
                total += 2 * b * k_sum
            return total

        normal_time = get_t(d)
        left_x = d - r
        right_x = d - l
        total_count = r - l + 1

        # Find largest x in [left_x, right_x] such that get_t(x) + 1 <= normal_time
        low, high = left_x, right_x
        split_x = left_x - 1
        while low <= high:
            mid = (low + high) // 2
            if get_t(mid) + 1 <= normal_time:
                split_x = mid
                low = mid + 1
            else:
                high = mid - 1

        ans = 0
        if split_x >= left_x:
            jump_count = split_x - left_x + 1
            ans += sum_t_range(left_x, split_x) + jump_count

        rem_count = total_count - max(0, split_x - left_x + 1)
        if rem_count > 0:
            ans += rem_count * normal_time

        return ans % MOD