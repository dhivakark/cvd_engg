#import numpy as np

# class AutoVivification(dict):
#     """Implementation of perl's autovivification feature."""
#     def __getitem__(self, item):
#         try:
#             return dict.__getitem__(self, item)
#         except KeyError:
#             value = self[item] = type(self)()
#             return value

def shortestReach(n, edges, s):

  '''
  '''
  s = s - 1
  edges = [[u - 1, v - 1, w] for u, v, w in edges]
  shortest_dist = np.full(n,  np.inf)
  shortest_dist[s] = 0
  nodes_to_visit = [i for i in range(n)]
  priority_queue = [[i, shortest_dist[i]] for i in nodes_to_visit]
  weight_matrix = {}

  for u,v,w in edges:
    if weight_matrix.get(u, '') == '':
      weight_matrix[u] = {}
    if weight_matrix[u].get(v, -1) < w:
      weight_matrix[u][v] = w

    if weight_matrix.get(v, '') == '':
      weight_matrix[v] = {}
    if weight_matrix[v].get(u, -1) < w:
      weight_matrix[v][u] = w

  while nodes_to_visit != []:

    priority_queue = sorted(priority_queue, key = lambda x:x[1])
    chosen_vertex, dist = priority_queue[0]
    nodes_to_visit.remove(chosen_vertex)
    shortest_dist[chosen_vertex] = dist
    edges_to_relax = weight_matrix[chosen_vertex]

    for node, weight in edges_to_relax.items():
      if shortest_dist[node] > shortest_dist[chosen_vertex]\
              + weight_matrix[chosen_vertex][node]:
        shortest_dist[node] = shortest_dist[chosen_vertex] + weight_matrix[chosen_vertex][node]

    priority_queue = [[i, shortest_dist[i]] for i in nodes_to_visit]

  shortest_dist = [int(dist) for dist in shortest_dist]
  return shortest_dist

if __name__=='__main__':
  t = 1
  n = 3
  m = 3
  edges = [[1,2,1],[1,3,5],[2,3,2]]
  print shortestReach(n, edges, s=1)
