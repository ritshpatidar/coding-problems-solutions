from test_cases import check_test_cases

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for num in nums:
            if num in d:
                return True
            else:
                d[num]=None
        
        return False

if __name__ == "__main__":
    solution = Solution()
    check_test_cases(solution.containsDuplicate)
