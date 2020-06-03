class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) <  2 or len (B) < 2:
            return False
        elif len(A) != len(B):
            return False

        else:
            for i in range(0, len(A)):
                for j in range(i+1, len(A)):
                    T = list(A)

                    T[j] , T[i] = T[i] , T[j]
                    str1=""
                    print T
                    print str1.join(T)
                    if str1.join(T) == B:
                        print str1
                        return True

            return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.buddyStrings("ab", "ab"))