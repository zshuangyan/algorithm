class Solution:
    """
    here are N network nodes, labelled 1 to N.

    Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

    Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

    Note:

    N will be in the range [1, 100].
    K will be in the range [1, N].
    The length of times will be in the range [1, 6000].
    All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100
    """

    def adjacency_list(self, edges, N):
        ad_list = [[] for i in range(N)]
        for start, end, length in edges:
            ad_list[start-1].append((end-1, length))
            # according to test case, the graph is directed
            # ad_list[end-1].append((start-1, length))
        return ad_list
    
    def dijkstra(self, ad_list, N, start):
        visited = [0 for i in range(N)]
        d = [-1 for i in range(N)]
        d[start] = 0
        queue = [start]
        while queue:
            node = queue.pop(0)
            for p, length in ad_list[node]:
                tmp = length + d[node]
                if d[p] == -1 or d[p] > tmp:
                    d[p] = tmp
                    queue.append(p)
        print("distances: %s" % d)
                    
        longest = -1
        for distance in d:
            if distance == -1:
                return -1
            if distance > longest:
                longest = distance
                
        return longest
    
    def networkDelayTime(self, times: list, N: int, K: int) -> int:
        ad = self.adjacency_list(times, N)
        return self.dijkstra(ad, N, K-1)

if __name__ == "__main__":
    result = Solution().networkDelayTime([[1,2,1],[2,1,3]], 2, 2)
