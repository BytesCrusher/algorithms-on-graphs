from DijkstraNodeDecorator import *
from BinaryTree import *
from MinHeap import *
from Graph import *

class Node:
    def __init__(self, data, indexloc = None):
        self.data = data
        self.index = indexloc