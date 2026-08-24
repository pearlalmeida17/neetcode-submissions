class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        maxLen = 0
        maxFreq = 0

        count = [0]*26

        for right in range(len(s)):

            
            count[ord(s[right]) - ord('A')] += 1

            maxFreq = max(maxFreq, count[ord(s[right]) - ord('A')])

            while (right - left + 1) - maxFreq > k:
                left_index = ord(s[left]) - ord('A')
                count[left_index] -= 1
                left += 1

            maxLen = max(maxLen, right - left + 1 )

        return maxLen
