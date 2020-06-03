class Solution(object):
    def matrixBlockSum(self, mat, K):
        result =  [ [ 0 for j in range(0,len(mat[0]))] for i in range(0,len(mat))]
        interval =  [[0 for j in range(0,len(mat[0]))] for i in range(0,len(mat))]
        m = len(mat)
        n = len(mat[0])

        for i in range(0, m):
            for j in range(0, n):

                interval[i][j] = self.calculate_range(i, j , K,m, n) # list of length 4
                for k in range(interval[i][j][0], interval[i][j][1]+ 1 ):
                    for h in range(interval[i][j][2], interval[i][j][3] + 1):
                        result[i][j]  += mat[k][h]
        return result
    def calculate_range(self, i, j , k,m,n):
        result = []
        result.append(max(0, i - k))
        result.append(min(i+ k , m -1))
        result.append(max(0, j-k))
        result.append(min(j+k, n-1))
        return result

if __name__ == '__main__':
 solution = Solution()
 mat= [[1,2,3],[4,5,6],[7,8,9]]
 k = 2
 print(solution.matrixBlockSum(mat,k))