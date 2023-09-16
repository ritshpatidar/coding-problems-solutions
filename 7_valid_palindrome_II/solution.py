class Solution:
    def isPalindrome(self, s: str, i, j) -> bool:
        while i<j:
            if s[i] != s[j]:
                return False
            i,j = i+1, j-1
        
        return True
    
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        
        while i < j:
            if s[i] == s[j]:
                i, j = i+1, j-1
            elif self.isPalindrome(s, i+1, j) or self.isPalindrome(s, i, j-1):
                return True
            else:
                return False
        
        return True