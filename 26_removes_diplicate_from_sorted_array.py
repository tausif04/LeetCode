

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        flag = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[flag] = nums[i]
                flag += 1

        return flag
    
# Example usage:
sol = Solution()
print(sol.removeDuplicates([1,1,2,2,3,4,4]))
