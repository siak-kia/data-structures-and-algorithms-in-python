class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums.sort()

        frequency_dict = {}
        frequency = 1
        result = []
        if len(nums) == 1:
            return [1]
        for j in range(0, len(nums) -1):
            if  nums[j] == nums[j+1]:
                frequency += 1

            else:
                frequency_dict[nums[j]] = frequency
                frequency = 1


        if nums[len(nums) -1] != nums[len(nums) - 2]:
            frequency_dict[nums[len(nums) -1]] = 1
        list_of_frequency = []
        for v in frequency_dict.values():
            list_of_frequency.append(v)

        list_of_frequency.sort(reverse=True)
        list_of_frequency = list_of_frequency[0:k]
        for h, v in frequency_dict.items():
            if v in list_of_frequency:
                result.append(h)
        return result
if __name__ == '__main__':
    solution = Solution()
    print(solution.topKFrequent([-1,-1], 1))


