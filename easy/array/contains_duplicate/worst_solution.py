from test_cases import check_test_cases

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bools
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        
        return False

if __name__ == "__main__":
    solution = Solution()
    check_test_cases(solution.containsDuplicate)
