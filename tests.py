import unittest
from Graph import Graph


class FordFulkersonTests(unittest.TestCase):

    def setUp(self):
        self.graph = Graph(11)
        self.graph.insert(0, 1, 25)
        self.graph.insert(0, 2, 27)
        self.graph.insert(0, 3, 15)
        self.graph.insert(1, 4, 33)
        self.graph.insert(2, 4, 17)
        self.graph.insert(2, 5, 22)
        self.graph.insert(2, 6, 50)
        self.graph.insert(3, 6, 19)
        self.graph.insert(4, 7, 40)
        self.graph.insert(4, 8, 15)
        self.graph.insert(5, 4, 5)
        self.graph.insert(5, 8, 14)
        self.graph.insert(6, 5, 7)
        self.graph.insert(6, 8, 37)
        self.graph.insert(6, 9, 51)
        self.graph.insert(7, 8, 9)
        self.graph.insert(7, 10, 45)
        self.graph.insert(8, 9, 8)
        self.graph.insert(8, 10, 44)
        self.graph.insert(9, 10, 39)

    def test_insert_exception_edge_exists(self):
        try:
            self.graph.insert(8, 9, 12)
        except Exception as e:
            self.assertEqual(str(e), "Edge already exists")

    def test_insert_exception_wrong_vertex_number(self):
        try:
            self.graph.insert(20, 1, 1)
        except Exception as e:
            self.assertEqual(str(e), "Vertex number must be non-begative and less than graph size")

    def test_insert_exception_wrong_edge_value(self):
        try:
            self.graph.insert(7, 9, -1)
        except Exception as e:
            self.assertEqual(str(e), "Edge value must be positive")

    def test_remove_exception_edge_does_not_exist(self):
        try:
            self.graph.remove(7, 9)
        except Exception as e:
            self.assertEqual(str(e), "Edge does not exist")

    def test_remove_exception_wrong_vertex_number(self):
        try:
            self.graph.remove(20, 1)
        except Exception as e:
            self.assertEqual(str(e), "Vertex number must be non-negative and less than graph size")

    def test_ford_fulkerson(self):
        self.assertEqual(self.graph.ford_fulkerson(0, 10), 67)

    def test_ford_fulkerson_exception(self):
        try:
            self.graph.ford_fulkerson(-1, 24)
        except Exception as e:
            self.assertEqual(str(e), "Source and end vertex numbers must be non-negative and less than graph size")