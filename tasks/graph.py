from typing import TypeVar, Generic

__all__ = ("Node", "Graph")


T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value

        self.outbound: list[Node] = []
        self.inbound: list[Node] = []

    @property
    def value(self) -> T:
        return self._value

    def point_to(self, other: "Node") -> None:
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self) -> str:
        return f'{repr(self.value)}'
        # return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node) -> None:
        self._root = root
        self.visited = list()  # Посещена ли вершина?
        self.Q = []  # Очередь
        self.BFS = []
    # ===============================
    def DFSUtil(self, v, visited):
        # Mark the current node as visited
        # and print it
        visited.append(v)
        # print(str(v), end=' ')
        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in v.outbound:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
        # return ''
    # ===============================
    def dfs(self) -> list[Node]:
        # Create a list to store visited vertices
        visited = list()
        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(self._root, visited)
        return visited
        # raise NotImplementedError

    # ===============================
    def BFSUtil(self, v):
        if v in self.visited:  # Если вершина уже посещена, выходим
            return
        self.visited.append(v)  # Посетили вершину v
        self.BFS.append(v)  # Запоминаем порядок обхода
        # print("v = %d" % v)
        for i in v.outbound:  # Все смежные с v вершины
            if not i in self.visited:
                self.Q.append(i)
        while self.Q:
            self.BFSUtil(self.Q.pop(0))
        return ''
    def bfs(self) -> list[Node]:
        self.BFSUtil(self._root)
        return self.visited
        # raise NotImplementedError
