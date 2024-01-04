from services.solution_salesmen import tsp_bellman_held_karp
import numpy as np

#Тест на корректность результата
def test_tsp_bellman_held_karp():
    graph = np.array([
        [0, 29, 20, 21],
        [29, 0, 15, 18],
        [20, 15, 0, 28],
        [21, 18, 28, 0]
    ])
    min_tour_length, tour_path = tsp_bellman_held_karp(graph)
    assert min_tour_length == 74
    assert tour_path == [2, 1, 3, 0, 0]

#Тест на обработку графа с двумя городами
def test_tsp_bellman_held_karp_single_city():
    graph = np.array([[0]])
    min_tour_length, tour_path = tsp_bellman_held_karp(graph)
    assert min_tour_length == float('inf')
    assert tour_path == [0]

#Тест на обработку графа с тремя городами
def test_tsp_bellman_held_karp_three_cities():
    graph = np.array([
        [0, 10, 15],
        [10, 0, 20],
        [15, 20, 0]
    ])
    min_tour_length, tour_path = tsp_bellman_held_karp(graph)
    assert min_tour_length == 45
    assert tour_path == [1, 2, 0, 0]

#Тест на обработку графа с четырьмя городами
def test_tsp_bellman_held_karp_four_cities():
    graph = np.array([
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ])
    min_tour_length, tour_path = tsp_bellman_held_karp(graph)
    assert min_tour_length == 80
    assert tour_path == [1, 3, 2, 0, 0]