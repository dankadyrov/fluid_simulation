import math
import itertools


class Node:
    def __init__(self, id):
        self.id = id
        self.previous_node = None
        self.next_node = None

    def push(self, start):
        if self.previous_node:
            self.previous_node.next_node = self.next_node
            self.previous_node = None
        if self.next_node:
            self.next_node.previous_node = self.previous_node
            self.next_node = None

        self.next_node = start.next_node
        if self.next_node:
            self.next_node.previous_node = self

        self.previous_node = start
        start.next_node = self
        pass


class HashTable:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        self.cells = [[Node(-1) for _ in range(math.ceil(height / cell_size))] for _ in
                      range(math.ceil(width / cell_size))]
        self.xcells = len(self.cells)
        self.ycells = len(self.cells[0])
        self.nodes = {}

    def coords_to_index(self, coords):
        return int(coords[0] // self.cell_size), int(coords[1] // self.cell_size)

    def neighbours(self, coords):  # iterator
        location = self.coords_to_index(coords)
        for dx, dy in itertools.product(range(-1, 2), range(-1, 2)):
            if location[0] + dx >= len(self.cells) or location[1] + dy >= len(self.cells[location[0] + dx]):
                if node:
                    node = node.next_node
                continue
            node = self.cells[location[0] + dx][location[1] + dy].next_node
            while node:
                yield node.id
                node = node.next_node

    def move(self, id, new_coords):
        node = self.nodes.get(id)
        if node is None:
            node = Node(id)
            self.nodes[id] = node
        location = self.coords_to_index(new_coords)
        node.push(self.cells[location[0]][location[1]])
