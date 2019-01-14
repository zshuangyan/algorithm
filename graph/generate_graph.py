# -*- coding: UTF-8 -*-
import random


class ValidationError(Exception):
    pass


class Graph:
    def __init__(self, num_of_point, edges=None, directed=0):
        self.directed = directed
        if self.directed:
            self.type_str = "有向图"
        else:
            self.type_str = "无向图"
        self.num_of_point = num_of_point
        if edges is not None and edges:
            self.edges = edges
        else:
            self.edges = self.generate_edges(self.num_of_point)

    def check_num_of_edge_and_point(self, num_of_point, num_of_edge):
        """
        check point and edge num correct according to graph type.

        Args:
            num_of_point
            num_of_edge

        Returns:
            a bool variable indicate whether pass or not and a description str
        """

        if num_of_edge <= 0 or num_of_point <= 0:
            return False, "点或边的数量都要大于0"

        # 如果是无环图, 边的数量有上限
        if (self.directed and num_of_edge > num_of_point*(num_of_point-1)) or (
                not self.directed and num_of_point > num_of_point*(num_of_point-1) // 2):
            return False, "当图形类型为: %s, 点的个数为: %s时, 边的个数为: %s不符合要求" % (
                self.type_str, num_of_point, num_of_point)

        return True, "点和边的数量通过校验"

    def generate_num_of_edge(self, num_of_point):
        """generate num of edge according to num of point.

        Args:
            num_of_point

        Raises:
            ValidationError: If num_of_point less than or equal to 0

        Returns:
            num of edge
        """
        if num_of_point <= 0:
            raise ValidationError("点的个数需要大于0")

        if self.directed:
            return random.randint(1, num_of_point*(num_of_point - 1))
        else:
            return random.randint(1, num_of_point*(num_of_point - 1) // 2)

    def generate_possible_edges(self, num_of_point):
        """generate all possible edge according to num of point.

        Args:
            num_of_point

        Raises:
            ValidationError: If num_of_point less than or equal to 0

        Returns:
            list of all possible edges, edge is a two element list formed by start point and end point
        """
        if num_of_point <= 0:
            raise ValidationError("点的个数需要大于0")

        if self.directed:
            return [[i, j] for i in range(num_of_point) for j in range(num_of_point) if i != j]
        else:
            return [[i, j] for i in range(num_of_point-1) for j in range(i+1, num_of_point)]

    def generate_edges(self, num_of_point=5, **kwargs):
        """
        generate random edges according to num of point.

        Args:
            num_of_point
            kwargs: num of edge could be set in kwargs

        Raises:
            ValidationError: If num_of_point or num_of_point is not legitimate

        Returns:
            list of edges, edge is a tuple formed by start point and end point
        """

        # 获取点和边的个数病校验, 如果用户没有提供边的个数, 则根据图的类型随机生成边的个数
        num_of_edge = kwargs.pop("num_of_edge", 0)
        if num_of_edge != 0:
            flag, msg = self.check_num_of_edge_and_point(num_of_point, num_of_edge)
            if not flag:
                raise ValidationError(msg)
        else:
            num_of_edge = self.generate_num_of_edge(num_of_point)

        possible_edges = self.generate_possible_edges(num_of_point)
        return random.sample(possible_edges, num_of_edge)

    @property
    def adjacency_matrix(self):
        """
        represent graph as adjacency matrix.

        Returns:
            a two-dimensional array m, with m[i][j] set to 1 if there is an edge from i to j otherwise 0.
        """
        ad_matrix = [[1 if i == j else 0 for i in range(self.num_of_point)] for j in range(self.num_of_point)]
        for start, end in self.edges:
            ad_matrix[start][end] = 1
            # 无环图
            if not self.directed:
                ad_matrix[end][start] = 1

        return ad_matrix

    @property
    def adjacency_list(self):
        """
        represent graph as adjacency list

        Returns:
             a two-dimensional array m, with m[i] contains all points connected by point i
        """
        ad_list = [[] for i in range(self.num_of_point)]
        for start, end in self.edges:
            ad_list[start].append(end)
            # 无环图
            ad_list[end].append(start)

        return ad_list


if __name__ == "__main__":
    g = Graph(num_of_point=5)
    print("Edges of graph: ", g.edges)
    print("Represent as Adjacency matrix: ", g.adjacency_matrix)
    print("Represent as Adjacency list: ", g.adjacency_list)












