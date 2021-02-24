package graph;

import java.util.ArrayList;
import java.util.NoSuchElementException;

public class Graph {
    // the nodes list is archaic, but it doesn't break anything so I'll leave it in.
    private ArrayList<Node> nodes;
    private boolean[][] adjMatrix;


    /**
     * Generic Graph constructor
     */
    public Graph() {
        this.nodes = new ArrayList<>();
        this.adjMatrix = new boolean[0][0];
    }

    /**
     * Graph constructor initialized with nodes
     * @param nodes array of Node objects
     */
    public Graph(Node[] nodes) {
        this.nodes = new ArrayList<>();
        this.adjMatrix = new boolean[nodes.length][nodes.length];

        for (Node node : nodes) {
            addNode(node);
        }
    }

    /**
     * Graph constructor initialized with nodes and edges
     * @param nodes array of Node objects
     * @param edges array of edges, represented as integer vectors
     */
    public Graph(Node[] nodes, int[][] edges) {
        this.nodes = new ArrayList<>();
        this.adjMatrix = new boolean[nodes.length][nodes.length];

        for (Node node : nodes) {
            addNode(node);
        }
        for (int[] edge : edges) {
            addEdge(edge);
        }
    }

    /**
     * Adds a node to the graph
     * @param node
     */
    public void addNode(Node node) {
        // make sure node doesn't already exist
        for (Node item : nodes){
            if (item.equals(node)){
                System.out.printf("Node %d already exists.\n", item.getID());
                return;
            }
        }
        nodes.add(node);
    }

    /**
     * Adds an edge to the graph by modifying the adjacency matrix
     * @param edge edge to be added, as an integer vector
     * @return Whether the edge was successfuly added
     */
    public boolean addEdge(int[] edge) {
        //Note that this graph does not allow duplicate edges.

        // edges must have exactly two nodes
        if (edge.length != 2) {
//            System.out.println("Not a valid edge."); //debug
            return false;
        }

        // no self loops
        if (edge[0] == edge[1]){
//            System.out.println("Self loops are disallowed."); //debug
            return false;
        }

        // make sure nodes exist in the graph
        boolean existsA = false;
        boolean existsB = false;
        for (Node node : nodes) {
            if (edge[0] == node.getID())
                existsA = true;
            if (edge[1] == node.getID())
                existsB = true;
        }
        if (!existsA) {
//            System.out.printf("Node %d does not exist; no edge added.\n", edge[0]); //debug
            return false;
        }
        if (!existsB) {
//            System.out.printf("Node %d does not exist; no edge added.\n", edge[1]); //debug
            return false;
        }

        // attempt to add the edge
        if (adjMatrix[edge[0]][edge[1]]) return false;
        adjMatrix[edge[0]][edge[1]] = true;
        adjMatrix[edge[1]][edge[0]] = true;
        return true;
    }

    /**
     * Remove an edge from the graph (not used)
     * @param a
     * @param b
     * @return
     */
    public boolean removeEdge(int a, int b) {
        if (!adjMatrix[a][b]) return false;

        adjMatrix[a][b] = false;
        adjMatrix[b][a] = false;

        return true;
    }

    public boolean getEdge(int a, int b) {
        return adjMatrix[a][b];
    }

    /**
     * Retrieve a Node object from the graph (not used)
     * @param id
     * @return the Node, if found
     * @throws NoSuchElementException
     */
    public Node getNode(int id) throws NoSuchElementException {
        // find node, remove it and return it
        Node temp;
        for (int i = 0; i < nodes.size(); i++) {
            if (nodes.get(i).getID() == id);
                temp = nodes.get(i);
                return temp;
        }

        // node does not exist
        System.out.printf("Node %d not found.\n", id);
        return null;
    }

    /**
     * List all nodes in the graph (not used)
     * @return Node array
     */
    public Node[] listNodes() {
        Node[] temp = new Node[nodes.size()];
        for (int i = 0; i < temp.length; i++)
            temp[i] = nodes.get(i);

        return temp;
    }

    /**
     * Retrieve the adjacency matrix as a (potentially large) string
     * @return adjacency matrix, as String
     */
    public String matrixAsString() {
        StringBuilder rtnStr = new StringBuilder();
        for (boolean[] i : adjMatrix) {
            rtnStr.append("[");
            for (boolean j : i) {
                if (j) rtnStr.append("1, ");
                else rtnStr.append("0, ");
            }
            rtnStr.replace(rtnStr.length()-2, rtnStr.length(), "]\n");
        }
        return rtnStr.toString();
    }

    /**
     * Check if the graph has edges (not used)
     * @return if the graph has edges
     */
    public boolean hasEdges() {
        for (boolean[] i : adjMatrix) {
            for (boolean j : i) {
                if (j) return true;
            }
        }
        return false;
    }

    /**
     * Depth first search algorithm
     * @param start Node to start from
     * @param visited array of previously visited nodes (must be length of nodes in graph)
     * @return array of connected nodes, as booleans
     */
    public boolean[] dfs(int start, boolean[] visited) {
        visited[start] = true;

        ArrayList<Integer> next = new ArrayList<>();
        for (int i = 0; i < visited.length; i++) {
            if (!visited[i]) {
                if(adjMatrix[start][i]) {
                    visited = dfs(i, visited);
                }
            }
        }

        return visited;
    }

}
