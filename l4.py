class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


class SingleEnded:
    def __init__(self):
        self.start = None
        self.length = 0

    def insert_beg(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
        else:
            new_node.link = self.start
            self.start = new_node

        self.length += 1

    def insert_end(self, data):
        new_node = Node(data)
        if self.start == None:
            self.start = new_node
        else:
            self.start = Node

# public void insertBeg(int data){
# Node newNode = new Node(data);
# if(start == null)
# start = newNode; // creating new linked list and pointing starting reference to newNode
# else {
# newNode.link = start;
# // pointing start pointer to newNode, start is pointing to current first node, which means newNode link is now
# pointing to current Node
# start = newNode; // updating start to point to newNode
# }
# length++;
# }

# public void insertEnd(int data){
# Node newNode = new Node(data);
# if(start == null)
# start = newNode; // creating new linked list and pointing starting reference to newNode
# else{
# Node n = start; // copying start pointer to n for traversing
# while (n.link !=null) // stops at last node
# n = n.link; // moving through nodes by assigning next node link to n
# n.link = newNode; // pointing last node link to newNode
# }
# length++;
# }
