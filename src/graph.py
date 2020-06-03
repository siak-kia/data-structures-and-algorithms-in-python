class Graph:
    def __init__(self, adj_list):
        self.adj_list = adj_list

    def is_connected(self, i ,j):
        visited = [0] * len(self.adj_list)
        self.dfs(i,  visited)
        return visited[j] == 1

    def dfs(self, i,  visited):
        visited[i] = 1
        for k in self.adj_list[i]:

            if not visited[k]:
                self.dfs(k, visited)

    def is_connected(self, i, j, visited):

        visited[i] = 1
        for k in self.adj_list[i]:

            if not visited[k]:
                self.is_connected(k, j, visited)
        return visited[j]

if __name__ == '__main__':

    adj_list = [[1], [2,0], [1], []]
    graph = Graph(adj_list)
    #print(graph.is_connected(0, 3))
    visited = [0] * len(adj_list)
    print graph.is_connected( 0, 2, visited)