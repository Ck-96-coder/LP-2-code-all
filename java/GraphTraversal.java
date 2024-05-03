import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;
import java.util.Scanner;

public class GraphTraversal {

    // Depth-First Search
    static void dfs(ArrayList<ArrayList<Integer>> graph, int start) {
        boolean[] visited = new boolean[graph.size()];
        Stack<Integer> stk = new Stack<>();

        stk.push(start);
        visited[start] = true;
        System.out.print("DFS Traversal: ");
        while (!stk.isEmpty()) {
            int node = stk.pop();
            System.out.print(node + " ");
            for (int neighbor : graph.get(node)) {
                if (!visited[neighbor]) {
                    stk.push(neighbor);
                    visited[neighbor] = true;
                }
            }
        }
        System.out.println();
    }

    // Breadth-First Search
    static void bfs(ArrayList<ArrayList<Integer>> graph, int start) {
        boolean[] visited = new boolean[graph.size()];
        Queue<Integer> que = new LinkedList<>();
        que.add(start);
        visited[start] = true;
        System.out.print("BFS Traversal: ");
        while (!que.isEmpty()) {
            int node = que.poll();
            System.out.print(node + " ");
            for (int neighbor : graph.get(node)) {
                if (!visited[neighbor]) {
                    que.add(neighbor);
                    visited[neighbor] = true;
                }
            }
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of nodes and edges: ");
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }

        System.out.println("Enter the edges: ");
        for (int i = 0; i < m; ++i) {
            int u = scanner.nextInt();
            int v = scanner.nextInt();
            graph.get(u).add(v);
            graph.get(v).add(u); // If it's a directed graph, remove this line
        }

        System.out.print("Enter the starting node for DFS and BFS: ");
        int startNode = scanner.nextInt();

        dfs(graph, startNode);
        bfs(graph, startNode);

        scanner.close();
    }
}
