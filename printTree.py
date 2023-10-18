from pathlib import Path
import networkx as nx

# prefix components:
space =  '    '
branch = '│   '
# pointers:
tee =    '├── '
last =   '└── '

def print_as_tree(D, n, prefix: str=''):
    """A recursive generator, given networkX Digraph object
        will yield a visual tree structure line by line
        with each line prefixed by the same characters
        Doesn't check for valid input, cycle in given graph
        will brake.
        """
    neighbours = [_ for _ in D.neighbors(n)]
    # contents each get pointers that are ├── with a final └── :
    pointers = [tee] * (len(neighbours) - 1) + [last]
    builder = ''
    for pointer, neighbour in zip(pointers, neighbours):
        builder = prefix + pointer + D.nodes[neighbour]['title'] + ' ' + D.nodes[neighbour]['content']
        yield builder
        if D.neighbors(neighbour): # extend the prefix and recurse:
            extension = branch if pointer == tee else space
            # i.e. space because last, └── , above so no more |
            yield from print_as_tree(D, neighbour, prefix=prefix+extension)
