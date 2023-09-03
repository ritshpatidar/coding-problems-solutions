class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = 0
        p2 = 0
        seen = {}
        _max = 0
        
        while p2<len(s):
            if s[p2] not in seen: #not seen: never saw it before
                seen[s[p2]] = p2
            elif seen[s[p2]] < p1: #not seen: not seen if saw it before p1
                seen[s[p2]] = p2
            else: #seen
                _max = max(_max, p2 - p1)
                p1 = seen[s[p2]] + 1
                seen[s[p2]] = p2
            p2+=1
        
        _max = max(_max, p2-p1)
        
        return _max

#Test
if __name__ == "__main__":
    sol = Solution()
    example = "abcabcbb"
    true_ans = 3
    
    ans = sol.lengthOfLongestSubstring(example)
    print(f"IN:{example}\nANS: {ans}, WORKED: {ans==true_ans}")