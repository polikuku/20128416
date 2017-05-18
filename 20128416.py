from collections import defaultdict


class Graph(object):
    """Graph: dictionary of sets"""
    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        """connections(list of tuples) to graph"""
        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """Add connection"""
        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def remove(self, node):
        for n, connects in self._graph.iteritems():
            try:
                connects.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_connected(self, node1, node2):
        return (node1 in self._graph and
                node2 in self._graph[node1])

    def dfs(self, start):
        visited = []

        def aux(start):
            visited.append(start)
            for node in sorted(self._graph[start]):
                if node not in visited:
                    aux(node)
        aux(start)
        return visited

    def bfs(self, start):
        visited = [start]
        que = [start]
        while (len(que) > 0):
            v = que.pop(0)
            for node in sorted(self._graph[v]):
                if node not in visited:
                    que.append(node)
                    visited.append(node)
        return visited

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))

N, M, V = map(int, raw_input().split())
graph = Graph([])

for _ in range(M):
    n1, n2 = map(int, raw_input().split())
    graph.add(n1, n2)
                                  
print ' '.join(map(str, graph.dfs(V)))
print ' '.join(map(str, graph.bfs(V)))
