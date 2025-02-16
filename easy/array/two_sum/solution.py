from test_cases import check_test_cases

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}

        for i in range(len(nums)):
            t = target-nums[i] 
            if t not in d:
                d[nums[i]] = i
            else:
                return [d[t], i]



if __name__ == "__main__":
    solution = Solution()
    check_test_cases(solution.twoSum)
