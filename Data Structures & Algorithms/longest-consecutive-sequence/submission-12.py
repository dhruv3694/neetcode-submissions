class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Remove duplicates and sort the unique elements
        sorted_unique_nums = sorted(set(nums))

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(sorted_unique_nums)):
            # Since duplicates are gone, check if elements are consecutive
            if sorted_unique_nums[i] == sorted_unique_nums[i - 1] + 1:
                current_streak += 1
            else:
                # Sequence broken, save max and reset
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1

        return max(longest_streak, current_streak)
