class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, node, neighbor, weight):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []
        self.adjacency_list[node].append((neighbor, weight))

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def h(self, n):
        # Heuristic function definition
        H = {
            'A': 11,
            'B': 6,
            'C': 99,
            'D': 1,
            'E': 7,
            'G': 0
        }
        return H[n]

    def a_star_algorithm(self, start_node, stop_node):
        open_list = set([start_node])
        closed_list = set([])
        g = {}
        g[start_node] = 0
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            for v in open_list:
                if n is None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v

            if n is None:
                print('Path does not exist!')
                return None

            if n == stop_node:
                reconst_path = []
                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]
                reconst_path.append(start_node)
                reconst_path.reverse()
                print('Path found:', reconst_path)
                return reconst_path

            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

# Creating a graph instance
graph = Graph()

# User input for defining the graph
num_edges = int(input("Enter the number of edges: "))
for _ in range(num_edges):
    node, neighbor, weight = input("Enter edge (node neighbor weight): ").split()
    graph.add_edge(node, neighbor, int(weight))

# User input for start and goal nodes
start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")

# Running A* algorithm
graph.a_star_algorithm(start_node, goal_node)


# Enter the number of edges: 8
# Enter edge (node neighbor weight): A B 2
# Enter edge (node neighbor weight): A D 3
# Enter edge (node neighbor weight): B C 1
# Enter edge (node neighbor weight): D E 1
# Enter edge (node neighbor weight): D G 1
# Enter edge (node neighbor weight): E G 7
# Enter edge (node neighbor weight): E D 6
# Enter edge (node neighbor weight): G B 9
# Enter the start node: A
# Enter the goal node: G4