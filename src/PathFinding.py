class PathFinding(object):
    def print_path(self, dict_path, goal_node):
        search_node = goal_node
        path = []
        while search_node in dict_path.keys():
            path.append(search_node)
            search_node = dict_path[search_node]

        path.append(0)
        print(path.reverse())
        print path
        return path


    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        queue = [0]
        dict_path={}
        all_paths=[]
        while len(queue) != 0:
            expanding_node = queue.pop(0)
            for j in graph[expanding_node]:
                queue.append(j)
                dict_path[j] = expanding_node
                if j == len(graph) - 1:
                    print "bingo"
                    print(dict_path)
                    all_paths.append(self.print_path(dict_path, len(graph) - 1))
        return  all_paths

pathFinder = PathFinding()
all_paths = pathFinder.allPathsSourceTarget([[1,2], [3], [3], []] )
print(all_paths)