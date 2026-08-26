from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t) or not t:
            return ""

        count_t = Counter(t)
        window = {}

        have = 0
        need = len(count_t)

        res = [-1, -1]
        min_len = float('inf')
        left = 0
        right = 0
        
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in count_t and window[char] == count_t[char]:
                have += 1

            while have == need:
                if (right - left + 1 ) < min_len:

                    min_len = right - left + 1
                    res = [left, right]

                left_char = s[left]
                window[left_char] -= 1

                if s[left] in count_t and window[left_char] < count_t[left_char]:
                    have -= 1
                
                left += 1
        
        l, r = res
        return s[l : r + 1] if min_len != float('inf') else ""


        