class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged_array = sorted(nums1 + nums2)
        a = len(merged_array)
        if a % 2 == 0:
            b = a // 2
            median = (merged_array[b - 1] + merged_array[b]) / 2
            return median
        else:
            b = a // 2
            median = float(merged_array[b])
            return median


def main():
    sol = Solution()
    print(sol.findMedianSortedArrays([1, 3], [2]))
    print(sol.findMedianSortedArrays([1, 2], [3, 4]))


if __name__ == "__main__":
    main()

