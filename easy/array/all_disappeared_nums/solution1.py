from test_cases import check_test_cases

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        missing = []

        for num in nums:
            if num not in d:
                d[num] = None
        
        for i in range(1,len(nums)+1):
            if i not in d:
                missing.append(i)
        
        return missing

if __name__ == "__main__":
    solution = Solution()
    check_test_cases(solution.findDisappearedNumbers)
