from test_cases import check_test_cases

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for num in nums:
            d[num] = None
        
        for i in range(len(nums)+1):
            if i not in d:
                return i

if __name__ == "__main__":
    solution = Solution()
    check_test_cases(solution.missingNumber)
