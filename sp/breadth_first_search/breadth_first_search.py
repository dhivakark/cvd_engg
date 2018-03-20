import sys

def bfs(n, m, edges, s):
    '''
    '''
    adjacency_list = dict.fromkeys([i+1 for i in range(n)] , [])
    
    for node1, node2 in edges:
        adjacency_list[node1] = adjacency_list.get(node1, []) + [node2]
        adjacency_list[node2] = adjacency_list.get(node2, []) + [node1]
   
    visited_nodes = []
    next_nodes = []
    node_dist = [-1 for i in range(n)]
    frontier = [s] 
    dist = 0
    while frontier != []:
        current_node = frontier[0]
        next_nodes +=  [ node for node in adjacency_list[current_node]\
                         if (node not in next_nodes and node not in visited_nodes)]
        frontier.remove(current_node)
        node_dist[current_node - 1] = dist 
        visited_nodes.append(current_node)
        if frontier == []:
            frontier = next_nodes
            next_nodes = []
            dist += 1
    return node_dist
     

if __name__ == "__main__":
    # q = int("2 4 2 1 2 1 3 1 3 1 2 3 2".strip())
    # q = int("2
    # 4 2
    # 1 2
    # 1 3
    # 1
    # 3 1
    # 2 3
    # 2".strip())
    # # q = int(raw_input().strip())
    # for a0 in xrange(q):
    #     n, m = raw_input().strip().split(' ')
    #     n, m = [int(n), int(m)]
    #     edges = []
    #     for edges_i in xrange(m):
    #         edges_temp = map(int,raw_input().strip().split(' '))
    #         edges.append(edges_temp)
    #     s = int(raw_input().strip())
    #  result = bfs(n, m, edges, s)
    #     print " ".join(map(str, result))
    n = 4
    m = 2
    edges = [[1,3], [1,2]]
    s = 1
    result = bfs(n, m, edges, s)
    print " ".join(map(str, result))

