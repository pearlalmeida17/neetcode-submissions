class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_len = 0
        seen = set()

        r = 0
        l = 0

        while r < len(s):
            
            if s[r] in seen:
                seen.remove(s[l])
                l += 1
            else:
                seen.add(s[r])
                r += 1

            max_len = max(max_len, len(seen))

        return max_len