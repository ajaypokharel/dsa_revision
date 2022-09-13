# Indegree Calculation for a Vertex

def get_degree(vertex, adj_list):
    if vertex not in adj_list:
        raise KeyError

    indegree = 0

    for v in adj_list:
        if vertex in adj_list[v]:
            indegree += 1

    return indegree


def topological_sort(adj_list, current, topo_list):
    if current not in adj_list:
        return

    for i in range(len(adj_list)):
        ...