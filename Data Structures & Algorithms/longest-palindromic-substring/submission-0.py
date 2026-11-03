class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        res = ""

        def palin(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left + 1: right]

        for i in range(len(s)):
            odd_palin = palin(i,i)
            if len(odd_palin) > resLen:
                res = odd_palin
                resLen = len(odd_palin)
            
            even_palin = palin(i, i +1)
            if len(even_palin) > resLen:
                res = even_palin
                resLen = len(even_palin)
            
        return res
        
                 
        

        