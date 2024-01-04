import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def longest_path_with_path(adj_matrix, start_vertex, end_vertex):
    num_vertices = len(adj_matrix)

    # Функция для вычисления топологической сортировки графа.
    def topological_sort():
        visited = [False] * num_vertices
        stack = []

        # Запускаем поиск в глубину (DFS) из каждой непосещенной вершины.
        def dfs(vertex):
            visited[vertex] = True
            for neighbor in range(num_vertices):
                if adj_matrix[vertex][neighbor] > 0 and not visited[neighbor]:
                    dfs(neighbor)
            stack.append(vertex)

        for vertex in range(num_vertices):
            if not visited[vertex]:
                dfs(vertex)

        return stack[::-1]  # Разворачиваем стек, чтобы получить топологическую сортировку.

    topological_order = topological_sort()

    # Инициализируем массивы для хранения длин путей и предков для каждой вершины.
    max_lengths = [-float('inf')] * num_vertices
    predecessors = [-1] * num_vertices
    max_lengths[start_vertex] = 0  # Начальная вершина имеет длину 0.

    # Проходим по вершинам в топологическом порядке и вычисляем максимальные длины путей.
    for vertex in topological_order:
        for neighbor in range(num_vertices):
            if adj_matrix[vertex][neighbor] > 0:
                if max_lengths[neighbor] < max_lengths[vertex] + adj_matrix[vertex][neighbor]:
                    max_lengths[neighbor] = max_lengths[vertex] + adj_matrix[vertex][neighbor]
                    predecessors[neighbor] = vertex

    # Построим путь, начиная с конечной вершины и двигаясь к начальной.
    path = [end_vertex]
    current_vertex = end_vertex
    while current_vertex != start_vertex:
        current_vertex = predecessors[current_vertex]
        path.append(current_vertex)

    path.reverse()  # Разворачиваем путь, чтобы он начинался с начальной вершины.

    # Возвращаем максимальную длину пути и сам путь.
    return max_lengths[end_vertex], path
