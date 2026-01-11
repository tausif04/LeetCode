from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        flag = None

        for num in nums:
            if count == 0:
                flag = num
                print(f"flag updated to {flag}")
            count += (1 if num == flag else -1)
            print(f"num: {num}, count: {count}, flag: {flag}")
        return flag
 
# Example usage:
sol = Solution()
print(sol.majorityElement([2,2,1,1,1,2,2]))  