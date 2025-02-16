from test_cases import check_test_cases

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        missing = []

        #Below loop's work: [4,3,2,7,8,2,3,1] -> [-4,-3,-2,-7,8,2,-3,-1]
        for num in nums:
            ind = abs(num)-1
            nums[ind] = -1*abs(nums[ind])
        
        #5,6th positions in [-4,-3,-2,-7,8,2,-3,-1] are positive
        for i, num in enumerate(nums):
            if num>0:
                missing.append(i+1)
        
        return missing

if __name__ == "__main__":
    solution = Solution()
    check_test_cases(solution.findDisappearedNumbers)
