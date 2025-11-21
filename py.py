def greedy_vertex_cover(edges):
    cover = set()
    remaining_edges = edges.copy()
    
    while remaining_edges:
        u, v = remaining_edges[0]
        
        cover.add(u)
        cover.add(v)
        
        remaining_edges = [edge for edge in remaining_edges 
                          if u not in edge and v not in edge]
    
    return cover

# Входные данные
edges = [(0,1), (1,2), (2,3), (3,4), (4,5), (5,6), (6,7), (7,8), (8,9), (9,0)]

result = greedy_vertex_cover(edges)
print("Вершинное покрытие:", sorted(result))
print("Размер покрытия:", len(result))

Вывод из консоли GDB:
Вершинное покрытие: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Размер покрытия: 10
