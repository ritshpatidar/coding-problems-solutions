from test_cases import check_test_cases

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for num_i in range(len(nums)+1):
            if num_i not in nums: #linear search
                return num_i

if __name__ == "__main__":
    solution = Solution()
    check_test_cases(solution.missingNumber)
