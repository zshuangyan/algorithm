def least_distance_of_not_weighted_graph(ad_list, s, e):
    """
    Get shortest path of two points in not weighted graph

    Args:
        ad_list: adjacency list represent of graph
        s: start point
        e: end point

    Returns:
        shortest length of start and end
        nodes on path from start to end(not encluded end)

    Exceptions:
        if there is not a path from start to end return -1, []
    """
    d = [-1 for i in range(len(ad_list))]
    prev = {s: []}
    d[s] = 0
    nodes = [s]
    while nodes:
        node = nodes.pop(0)
        for p in ad_list[node]:
            if d[p] == -1:
                d[p] = d[node] + 1
                prev[p] = prev[node] + [node]
                nodes.append(p)
            if p == e:
                return d[p], prev[p]
    return d[e], []
                
if __name__ == "__main__":
    import random
    from graph import Graph
    for i in range(10):
        g = Graph(6)
        g.printGraph()
        ad_list = g.adjacency_list
        start, end = random.sample(range(g.num_of_point), 2)
        print("start: %s, end: %s" % (start, end))
        length, prev = least_distance_of_not_weighted_graph(ad_list, start, end)
        path = prev + [end]
        print("length: %s, path: %s" % (length, path))
        print()
