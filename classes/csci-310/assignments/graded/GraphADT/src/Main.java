import graph.*;
import java.util.Random;

public class Main {

    // leftover code from a previous implementation
    private static String genArray(Object[] arr) {
        StringBuilder rtnStr = new StringBuilder();
        rtnStr.append("{");
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == null)
                rtnStr.append("null, ");
            else
                rtnStr.append(arr[i].toString()).append(", ");
            if (i % 10 == 9 && i < arr.length - 1)
                rtnStr.append("\n  ");
        }

        return rtnStr.substring(0, rtnStr.length() - 2) + "}\n";
    }

    public static void main(String[] args) {
        int graphSize;
        if (args.length < 1) {
            System.out.println("No arguments passed. Assuming 100 nodes.\n");
            graphSize = 100;
        }
        else {
            try {
                graphSize = Integer.parseInt(args[0]);
            } catch (Exception e) {
                System.out.println("Argument must be an integer.");
                return;
            }
        }


        // Step 1: Create the undirected graph
        System.out.printf("Generating graph of size %d...", graphSize);
        System.out.flush();

        // generate nodes
        Node[] graphNodes = new Node[graphSize];
        for (int i = 0; i < graphSize; i++) {
            graphNodes[i] = new Node(i);
        }

        Graph myGraph = new Graph(graphNodes);

        // generate edges
        long edgeCount = (long) (0.8 * graphSize * (graphSize - 1)/2);
        Random rng = new Random();
        int tempA;
        int tempB;
        int[] tempEdge = new int[2];

        // guarantee at least one edge per every node
        boolean control;                                    // used for while loops in case edge creation fails
        for (int i = 0; i < graphSize; i++) {
            control = false;
            while (!control) {
                tempEdge[0] = graphNodes[i].getID();
                tempEdge[1] = graphNodes[rng.nextInt(graphSize)].getID();
                control = myGraph.addEdge(tempEdge);
            }
        }

        // generate the remaining edges
        /*
         * This section of code randomly generates two integers representing possible nodes.
         * If both integers are the same, the edge is rejected.
         * If an edge for a to b (or b to a) exists, the edge is rejected.
         * If the edge is rejected, it generates a new edge.
         * This continues until the required number of edges are accepted.
         *
         * I realize by coding it this way, it may take an arbitrarily long time to complete.
         * A better implementation might instead generate a cartesian product and select from that,
         * but this works for now.
         */
        for (int i = 0; i < edgeCount - graphSize; i ++) {
            control = false;
            while (!control) {
                tempEdge[0] = rng.nextInt(graphSize);
                tempEdge[1] = rng.nextInt(graphSize);
                control = myGraph.addEdge(tempEdge);
            }
        }

        System.out.println("Done");
        System.out.print(myGraph.matrixAsString());
        System.out.println();
        // End of step 1

        // Step 2: find strongly connected sections
        // For this I'm using a depth-first search, written as a method of the graph.Graph class
        int testNode = 0; // just testing it on one node for now

        boolean[] visited = new boolean[graphSize];
        visited = myGraph.dfs(testNode, visited);

        // print results
        StringBuilder result = new StringBuilder();
        result.append("[");
        for (int i = 0; i < visited.length; i++) {
            if (visited[i]) result.append(i).append(", ");
            else System.out.printf("Node %d is not connected to node %d!\n", i, testNode);
        }
        result.replace(result.length()-2, result.length(), "]");
        System.out.println(result);
        // End of step 2

        /* In my testing, I have yet to find a case where a node is not connected
         * but it also takes unrealistically long to generate graphs with more than 10000 nodes.
         *
         * In theory, different "clusters" could be formed from the results,
         * and new starting points can be identified by "false" values in visited.
         */

        // Step 3: Forming a bipartite graph
        myGraph = new Graph(graphNodes);
        //Didn't make it this far, unfortunately


        System.out.println("Done.");
    }
}
