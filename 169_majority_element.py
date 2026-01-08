class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        flag = None

        for num in nums:
            if count == 0:
                flag = num
            count += (1 if num == flag else -1)
        return flag
 
 