class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        arr = [[" " for x in range(200)] for y in range(200)]
        result = []
        ## intialize the columns
        words = s.split(" ")
        i = 0
        j = 0
        for word in words:
            i = 0
            for char in word:
                arr[i][j] = char
                i += 1
            j += 1
        for i in range(len(arr)):

             s = "".join(arr[i]).rstrip()
             if len(s) > 0:
                 result.append(s)
        return result
if __name__ == '__main__':
    sol = Solution()
    s = "CONTEST IS COMING"
    result = sol.printVertically(s)
    print result
