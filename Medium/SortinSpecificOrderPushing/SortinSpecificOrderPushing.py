class Solution:
    def sortIt(self, arr: list[int]) -> None:
        odds = sorted([x for x in arr if x % 2 == 1], reverse=True)
        evens = sorted([x for x in arr if x % 2 == 0])
        arr[:] = odds + evens