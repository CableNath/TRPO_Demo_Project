import networkx as nx
import numpy as np
import pytest
from services.solution_backpack import longest_path_with_path

@pytest.fixture
def adjacency_matrix():
    # Пример матрицы смежности графа.
    adj_matrix = np.array([
        [0, 1, 3, 0, 0],
        [0, 0, 2, 4, 0],
        [0, 0, 0, 2, 5],
        [0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0]
    ])
    return adj_matrix

def test_longest_path_with_path(adjacency_matrix):
    start_vertex = 0
    end_vertex = 4
    expected_length = 8
    expected_path = [0, 2, 4]

    length, path = longest_path_with_path(adjacency_matrix, start_vertex, end_vertex)

    assert length == expected_length
    assert path == expected_path