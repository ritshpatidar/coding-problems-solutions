from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        lmax, rmax = 0, 0
        l, r = 0, len(height)-1
        water = 0

        while l<=r:
            if lmax<=rmax:
                water += max(0, lmax - height[l])
                lmax = max(lmax, height[l])
                l+=1
            else:
                water += max(0, rmax - height[r])
                rmax = max(rmax, height[r])
                r-=1
        
        return water
#Test
if __name__ == "__main__":
    sol = Solution()
    example = [0,1,0,2,1,0,1,3,2,1,2,1]
    true_ans = 6
    
    ans = sol.trap(example)
    print(f"IN:{example}\nANS: {ans}, WORKED: {ans==true_ans}")