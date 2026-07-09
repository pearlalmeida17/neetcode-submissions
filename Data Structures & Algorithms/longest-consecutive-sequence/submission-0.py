class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        nums_set = set(nums)

        for num in nums_set:
            if ((num - 1)  in nums_set):
                continue
            else:
                current_num = num
                current_streak = 1

                while (current_num + 1) in nums_set:
                    current_num += 1
                    current_streak += 1

                longest = max(longest, current_streak)  
        
        return longest


