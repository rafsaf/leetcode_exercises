from typing import List, Set


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dup_list: List[int] = []
        nums_set: Set[int] = set()
        while len(nums) > 0:
            number = nums.pop()
            if number in nums_set:
                dup_list.append(number)
            else:
                nums_set.add(number)
        return dup_list


sol = Solution().findDuplicates(nums=[4, 3, 2, 7, 8, 2, 3, 1])
print(sol)
