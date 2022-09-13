from collections import deque

graph = {
    'a': ['c', 'b'],
    'c': ['e'],
    'b': ['d'],
    'd': ['f'],
    'e': ['f'],
    'f': []
}


def dfs(adj_list):
    visited = {}
    for item in adj_list:
        visited[item] = 0
    return dfs_helper(adj_list, visited, 'a')


def bfs(adj_list, start_vertex, visited):
    q = deque()

    q.append(adj_list[start_vertex])

    while q:
        current = q.popleft()

        for item in current:
            print(item)
            q.append(adj_list[item])


def dfs_helper(adj_list, visited, current_vertex):
    if visited[current_vertex] == 1:
        return

    visited[current_vertex] = 1

    print(current_vertex)

    for item in adj_list[current_vertex]:
        dfs_helper(adj_list, visited, item)


print('BFS')
bfs(graph, 'a', visited={})

print('DFS')
dfs(graph)
