class Solution:
    def countSubstrings(self, s: str) -> int:
        total_count = 0

        def palin(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count

        for i in range(len(s)):
            total_count += palin(i,i)
               

            total_count += palin(i, i+1)
             
        
        return total_count