from typing import List

class Solution:
    def maxEqualSum(self, s1: List[int], s2: List[int], s3: List[int]) -> int:
        sum1 = sum(s1)
        sum2 = sum(s2)
        sum3 = sum(s3)

        n1, n2, n3 = len(s1), len(s2), len(s3)
        top1 = top2 = top3 = 0

        while top1 < n1 and top2 < n2 and top3 < n3:
            # If all sums are equal, return the sum
            if sum1 == sum2 == sum3:
                return sum1

            # Reduce the stack having the maximum sum
            if sum1 >= sum2 and sum1 >= sum3:
                sum1 -= s1[top1]
                top1 += 1
            elif sum2 >= sum1 and sum2 >= sum3:
                sum2 -= s2[top2]
                top2 += 1
            else:
                sum3 -= s3[top3]
                top3 += 1

        return 0