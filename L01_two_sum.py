def twoSum(self, nums: list[int], target: int) -> list[int] :
        for i in range(0,len(nums)):
             for j in range(i+1,len(nums)):
                 if nums[i]+nums[j] == target:
                    return (i,j)
                    

nums = list(map(int, input().split()))
target = int(input())
res= twoSum(0, nums, target)
print(res)


    

