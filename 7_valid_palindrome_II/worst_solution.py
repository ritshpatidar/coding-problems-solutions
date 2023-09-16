class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j = 0, len(s)-1
        
        while i<j:
            if s[i] != s[j]:
                return False
            i,j = i+1, j-1
        
        return True
    
    def validPalindrome(self, s: str) -> bool:
        if self.isPalindrome(s):
            return True
        else:
            #Remove every char and check if palindrome
            for i in range(len(s)):
                if self.isPalindrome(s[:i] + s[i+1:]):
                    return True
        
        return False
#Test
if __name__ == "__main__":
    sol = Solution()
    example = "aabaaq"
    true_ans = True
    
    ans = sol.validPalindrome(example)
    print(f"IN:{example}\nANS: {ans}, WORKED: {ans==true_ans}")