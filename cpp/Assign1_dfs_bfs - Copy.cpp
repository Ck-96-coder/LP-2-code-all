#include <iostream>
#include <vector>
#include <queue>
#include <stack>

using namespace std;

// Depth-First Search
void dfs(vector<vector<int>>& graph, int start) {
    vector<bool> visited(graph.size(), false);
    stack<int> stk;

    stk.push(start);
    visited[start] = true;
    cout << "DFS Traversal: ";
    while (!stk.empty()) {
        int node = stk.top();
        stk.pop();
        cout << node << " ";
        for (int neighbor : graph[node]) {
            if (!visited[neighbor]) {
                stk.push(neighbor);
                visited[neighbor] = true;
            }
        }
    }
    cout << endl;
}

// Breadth-First Search
void bfs(vector<vector<int>>& graph, int start) {
    vector<bool> visited(graph.size(), false);
    queue<int> que;
    que.push(start);
    visited[start] = true;
    cout << "BFS Traversal: ";
    while (!que.empty()) {
        int node = que.front();
        que.pop();
        cout << node << " ";
        for (int neighbor : graph[node]) {
            if (!visited[neighbor]) {
                que.push(neighbor);
                visited[neighbor] = true;
            }
        }
    }
    cout << endl;
}

int main() {
    int n, m; // n is the number of nodes, m is the number of edges
    cout << "Enter the number of nodes and edges: ";
    cin >> n >> m;
    vector<vector<int>> graph(n);
    cout << "Enter the edges: " << endl;
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u); // If it's a directed graph, remove this line
    }

    int start_node;
    cout << "Enter the starting node for DFS and BFS: ";
    cin >> start_node;

    dfs(graph, start_node);
    bfs(graph, start_node);

    return 0;
}


// Enter the number of nodes and edges: 5 6
// Enter the edges:
// 0 1
// 0 2
// 1 3
// 1 4
// 2 3
// 3 4
// Enter the starting node for DFS and BFS: 0
