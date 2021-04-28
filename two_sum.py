from typing import Dict, List, Set


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        possible_numbers: Dict[int, int] = {}
        for current_index, number in enumerate(nums):
            diffrence_number: int = target - number
            if diffrence_number in possible_numbers:
                matching_index: int = possible_numbers[diffrence_number]
                return [matching_index, current_index]
            possible_numbers[number] = current_index
        raise (ValueError("Not really good arguments"))


sol = Solution().twoSum([-3, 4, 3, 90], 0)
print(sol)
