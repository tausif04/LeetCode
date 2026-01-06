class solution:
    def moveZeroes(self, nums: list[int]) -> None:
        
        zero_index = 0  # Pointer for the position to place the next non-zero element

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero_index], nums[i] = nums[i], nums[zero_index]
                zero_index += 1
        
        return nums
