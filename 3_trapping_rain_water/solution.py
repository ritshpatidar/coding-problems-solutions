from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        lmax, rmax = 0, 0
        lmax_ls, rmax_ls = [], []
        
        for i in range(len(height)):
            lmax_ls.append(lmax)
            rmax_ls.append(0)

            if height[i] > lmax:
                lmax = height[i]
        
        for j in range(len(height)-1, -1, -1):
            rmax_ls[j] = rmax

            if height[j] > rmax:
                rmax = height[j]

        water = 0
        for k in range(len(height)):
            water += max(0, min(lmax_ls[k], rmax_ls[k]) - height[k])
        
        return water

#Test
if __name__ == "__main__":
    sol = Solution()
    example = [0,1,0,2,1,0,1,3,2,1,2,1]
    true_ans = 6
    
    ans = sol.trap(example)
    print(f"IN:{example}\nANS: {ans}, WORKED: {ans==true_ans}")