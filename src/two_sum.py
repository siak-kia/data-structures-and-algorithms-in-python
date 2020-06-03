class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ############
        
        nums_dict = {}

        for ele in enumerate(nums):
            nums_dict[ele[1]] = ele[0]
        for i in range (len(nums)):
            if nums_dict.get(target - nums[i]) and i <>  nums_dict.get(target - nums[i]):
                return [ i , nums_dict.get(target - nums[i])]
        return None
if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([3,3], 6))