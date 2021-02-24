package graph;

// This is kinda pointless now but I'll leave it in anyway.
public class Node {
    private int nodeID;

    public Node(int id){
        this.nodeID = id;
    }

    public int getID(){
        return this.nodeID;
    }

    @Override
    public boolean equals(Object o) {
        if(!(o instanceof Node))
            return false;

        Node temp = (Node) o;
        return this.nodeID == temp.nodeID;
    }

    @Override
    public String toString() {
        return String.format("N(%d)", getID());
    }
}
