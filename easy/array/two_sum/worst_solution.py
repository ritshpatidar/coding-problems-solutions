from test_cases import check_test_cases

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]

if __name__ == "__main__":
    solution = Solution()
    check_test_cases(solution.twoSum)
