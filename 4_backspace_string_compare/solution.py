class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        
        for ch in s:
            if ch != "#":
                stack_s.append(ch)
            else:
                if len(stack_s)>0:
                    stack_s.pop()
        
        for ch in t:
            if ch != "#":
                stack_t.append(ch)
            else:
                if len(stack_t)>0:
                    stack_t.pop()
        
        if len(stack_s) != len(stack_t):
            return False
        else:
            for i in range(len(stack_s)):
                if stack_s[i] != stack_t[i]:
                    return False
        
        return True

#Test
if __name__ == "__main__":
    sol = Solution()
    s, t = "ab#c", "ad#c"
    true_ans = True
    
    ans = sol.backspaceCompare(s, t)
    print(f"IN:{s, t}\nANS: {ans}, WORKED: {ans==true_ans}")