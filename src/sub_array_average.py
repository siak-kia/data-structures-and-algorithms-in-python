class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        num = 0
        sub_array = arr[0: k ]
        window_sum  = sum(sub_array)
        if window_sum >= threshold * k:
            num += 1
        for i in range(1, len(arr) - k + 1):
            window_sum = window_sum - arr[i-1] + arr[i+k - 1]
            if window_sum >= threshold * k:
                num += 1

        return num

if __name__ == '__main__':
    s = Solution()
    s.numOfSubarrays([1,1,1,1,1],1, 0)
