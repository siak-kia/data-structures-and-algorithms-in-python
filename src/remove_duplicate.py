class RemoveDuplicate:
    def remove_duplicate(self, nums):
        j = 0
        for i in range(0, len(nums) -1):
            # print (len(nums) -1 )
            if nums[i] == nums[i+1]:
                 j += 1
        return len(nums) - j


    def removeDuplicates(arr, n):
        if n == 0 or n == 1:
            return n

        # To store index of next
    # unique element
        j = 0

    # Doing same as done
    # in Method 1 Just
    # maintaining another
    # updated index i.e. j
        for i in range(0, n-1):
            if arr[i] != arr[i+1]:
                arr[j] = arr[i]
                j += 1

        arr[j] = arr[n-1]
        j += 1
        print arr
        return j

class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        num_moves = 0
        prev = keyboard[0]
        keyboard_dict = {}
        j = 0
        for h in keyboard:
            keyboard_dict[h] = j
            j  = j + 1
        for i in word:
            num_moves += abs(keyboard_dict[i]  - keyboard_dict[prev])
            prev = i
        return num_moves


if __name__ == '__main__':

    solution = Solution()
    solution.calculateTime("abcdefghijklmnopqrstuvwxyz", "cba")

#  remove_duplicate = RemoveDuplicate()
# # print(remove_duplicate.remove_duplicate([0, 1,1,1,2,3,3]))
#  arr = [0, 1,1,1,2,3,3]
#  print(removeDuplicates(arr, 7))
#  for i in range(0, 7):
#      print (" %d "%(arr[i]))

