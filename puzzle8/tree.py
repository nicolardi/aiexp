# I need a structure to representa a tree
class Node:
    def __init__(self, state, prev):
        self.children = []
        self.state = state
        self.prev = prev
        self.printyBehavour = None

    def getPath(self):
        moves = []
        curr = self
        while True:
            moves = moves + [curr]
            if (curr.prev == None):
                break
            curr = curr.prev
        return moves[::-1]
        
class Tree:
    def __init__(self):
        self.start_node = None 

    def printTree(self):
        children = [self.start_node]
        while len(children):
            n = children[0]
            print(n)
            children.remove(n)
            children = children + n.children 

    def add(self, state, prev):
        newNode = Node(state, prev)
        if prev == None:
            self.start_node = newNode
        else:
            prev.children.append(newNode)
        return newNode
    
if __name__ == '__main__':
    tree = Tree()
    start_node = tree.add('712843065', None)

    n2 = tree.add('712043865', start_node)
    n3 = tree.add('712843605', start_node)

    print("Whole tree")
    tree.printTree()

    print("Path to start_node from n3")
    n3.print_path()
