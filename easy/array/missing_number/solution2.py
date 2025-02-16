from test_cases import check_test_cases

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(range(len(nums)+1)) - sum(nums)

if __name__ == "__main__":
    solution = Solution()
    check_test_cases(solution.missingNumber)
