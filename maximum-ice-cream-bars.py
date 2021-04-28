from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        result = 0
        costs.sort()
        for val in costs:
            coins -= val
            if coins < 0:
                break
            result += 1
        return result
