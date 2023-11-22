import random
import sys

def calculate_min_distances_matrix(G):
    size_G = len(G)
    min_distances_matrix = []

    for v in range(size_G):
        distances = [float('inf')] * size_G
        distances[v] = 0
        visited = [False] * size_G

        for _ in range(size_G):
            current_vertex = find_min_distance_vertex(distances, visited)
            visited[current_vertex] = True

            for i in range(size_G):
                if not visited[i] and G[current_vertex][i] > 0:
                    distances[i] = min(distances[i], distances[current_vertex] + G[current_vertex][i])

        min_distances_matrix.append(distances)

    return min_distances_matrix

def find_min_distance_vertex(distances, visited):
    min_distance = float('inf')
    min_vertex = -1

    for v in range(len(distances)):
        if not visited[v] and distances[v] < min_distance:
            min_distance = distances[v]
            min_vertex = v

    return min_vertex

def calculate_graph_properties(min_distances_matrix):
    diameters = [max(distances) if max(distances) != float('inf') else 0 for distances in min_distances_matrix]
    radius = min(diameters)

    peripheral_vertices = [i for i, distance in enumerate(diameters) if distance == max(diameters)]
    central_vertices = [i for i, distance in enumerate(diameters) if distance == min(diameters)]

    return max(diameters), radius, peripheral_vertices, central_vertices

def main():
    if len(sys.argv) != 4:
        print("Использование: python L10.py <размер матрицы> <в - взвешенный, -в - невзвешенный> <о - ориентированный, -о - неориентированный>")
        sys.exit(1)

    size1 = int(sys.argv[1])
    weight_type = sys.argv[2]
    orientation = sys.argv[3]

    M1 = []
    for i in range(size1):
        row = [0] * size1
        M1.append(row)

    if weight_type == "-в":
        if orientation == "-о":
            for i in range(size1):
                for j in range(i + 1, size1):
                    M1[i][j] = M1[j][i] = random.randint(0, 1)
        elif orientation == "о":
            for i in range(size1):
                for j in range(size1):
                    if i != j:
                        M1[i][j] = random.randint(0, 1)
    elif weight_type == "в":
        if orientation == "-о":
            for i in range(size1):
                for j in range(i + 1, size1):
                    M1[i][j] = M1[j][i] = random.randint(0, 10)
        elif orientation == "о":
            for i in range(size1):
                for j in range(size1):
                    if i != j:
                        M1[i][j] = random.randint(0, 10)

    print("Матрица смежности для M1:")
    for row in M1:
        print(row)

    min_distances_matrix = calculate_min_distances_matrix(M1)

    print("\nМатрица минимальных расстояний:")
    for row in min_distances_matrix:
        print(row)

    diameter, radius, peripheral_vertices, central_vertices = calculate_graph_properties(min_distances_matrix)

    print(f"\nДиаметр графа: {diameter}")
    print(f"Радиус графа: {radius}")
    print(f"Периферийные вершины: {peripheral_vertices}")
    print(f"Центральные вершины: {central_vertices}")

if __name__ == "__main__":
    main()
