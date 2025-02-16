from test_cases import check_test_cases

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        missing = []
        for i in range(1,len(nums)+1):
            if i not in nums:
                missing.append(i)
        
        return missing

if __name__ == "__main__":
    solution = Solution()
    check_test_cases(solution.findDisappearedNumbers)
