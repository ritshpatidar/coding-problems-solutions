#When I ran the below, didn't expect it to be accepted but it got accepted on leetcode. LOL.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {} #If it was list instead of dict, time complexity would be O(n^3)
        _max = 0
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] not in d:
                    d[s[j]] = None
                else:
                    break
            
            _max = max(_max, len(d))
            d = {}
        
        return _max

#Test
if __name__ == "__main__":
    sol = Solution()
    example = "abcabcbb"
    true_ans = 3
    
    ans = sol.lengthOfLongestSubstring(example)
    print(f"IN:{example}\nANS: {ans}, WORKED: {ans==true_ans}")
        