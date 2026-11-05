class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        right = -1
        left = -1

        max_value = nums[0]
        for i in range(n):
            if nums[i] < max_value:
                right = i
            else:
                max_value = nums[i]

        min_value = nums[-1]
        for i in range(n - 1, -1, -1):
            if nums[i] > min_value:
                left = i
            else:
                min_value = nums[i]

        return 0 if right == -1 else right - left + 1