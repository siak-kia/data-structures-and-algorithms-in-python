class Solution(object):

    def checkIfPrerequisite(self, n, prerequisites, queries):
        """
        :type n: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """


        def dfs(visited,  src, dst):

            if src not in visited:

                if src == dst:

                    return True
                visited.add(src)
                for i in range(len(self.prerequisites)):
                    print self.prerequisites[i]
                    if self.prerequisites[i][0] == src:
                        print self.prerequisites[i][1]
                        return dfs(visited, prerequisites[i][1], dst)
        result = []
        self.prerequisites = prerequisites
        for i in queries:
            visited = set()

            print   i[0], i[1]
            result.append(dfs(visited, i[0], i[1]))

        return result
if __name__ == '__main__':
    s = Solution()
    print s.checkIfPrerequisite(4, [[2,3],[2,1],[0,3],[0,1]],
    [[0,1],[0,3],[2,3],[3,0],[2,0],[0,2]])

