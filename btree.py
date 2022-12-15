from operator import index
from node import Node
from prob import Prob

class BTree(object):
    def __init__(self, d : int, h : int) -> None:
        self.root = 0
        self.node = Node(d, True)
        self.d = d
        self.h = h
        super().__init__()
    
    def print(self, node_index = 0, depth = 0) -> None:
        self.node.load(node_index)
        for children_node_index in self.node.children:
            if children_node_index != -1:
                self.print(children_node_index, depth + 1)
        self.node.load(node_index)
        print("  " * depth, self.node.get_keys_to_print())

    
    def search(self, key: int) -> tuple:
        self.node.load(self.root)
        while True:
            key_index, node_index = self.node.find(key)
            if key_index != -1:
                return True, self.node.dm.get_value(key_index)
            if key_index == -1 and self.node.leaf == 1:
                return False, Prob(-1,-1, -1)
            if key_index == -1 and self.node.leaf != 0:
                if node_index  != -1:
                    self.node.load(node_index)
    
    def split_node(self, xnode : Node, index : int, ynode : Node):
        pass

    def insert(self, key : int, address : int) -> bool:
        # Already exists
        if(self.search(key)[0]):
            return False
        # Since we called search function, our current node is a leaf
        if self.node.m < 2 * self.d:
        # Insert (x, a) on the current page
            index = -1
            for i in range(self.node.keys):
                if self.node.keys[i] > key or self.node.keys[i] == self.node.max_key:
                    index = i
                    break
            self.node.keys[index] = key
            self.node.adds[index] = address
            return True
        elif self.node.can_compensate():
        #Try compensation
            return True
        else:
            if self.node.split():
                return True
            else:
                return False

    def update(self, key: int) -> None:
        pass

    def delete(self, key : int) -> None:
        pass