class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        
        left = 0
        right = len(s1)

        s1_count  = [0]*26
        window_count  = [0]*26

        if len(s1) > len(s2):
            return False

        for i in  range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1
        
        if s1_count == window_count:
                return True

        if len(s1) > len(s2):
            return False
        
        for right in range(len(s1), len(s2)):

            window_count[ord(s2[right]) - ord('a')] += 1
            
            window_count[ord(s2[right - len (s1)]) - ord('a')] -= 1
            

            if s1_count == window_count:
                return True

        return False


            

             
             
        