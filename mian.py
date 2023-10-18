from tkinter.filedialog import askopenfilename
# -*- coding: utf-8 -*-
import json
import codecs
import re
import matplotlib.pyplot as plt
import matplotlib as mpl

from typing import List

import networkx as nx


def get_node_info(txt):
    counter = 0
    numbers = []
    while re.search("^\d", txt):
        match = re.search("(^\d\.)|(^\d)", txt)
        txt = match.string[match.end()::]
        number = match.group().replace('.', '')
        counter += 1
        numbers.append(number)
    return counter, numbers, txt

def linesToTree(lines: List[str]):
    G = nx.DiGraph()
    G.add_node(0)
    G.nodes[0]['title'] = 'root'
    G.nodes[0]['parents'] = []
    G.nodes[0]['content'] = ''
    current_node = 0
    all_counters =[]
    all_numbers =[]
    all_lines = []
    for line in lines:
        if re.search("^\d", line):
            counter, numbers, txt = get_node_info(line)
            id = int(''.join(numbers))
            lvl = counter
            current_node = id
            G.add_node(id)
            G.nodes[id]['lvl'] = lvl
            G.nodes[id]['parents'] = numbers
            G.nodes[id]['title'] = txt
            G.nodes[id]['content'] = ''
            if len(numbers) > 1:
                G.add_edge(int(''.join(numbers[:len(numbers) - 1:])), id)
            else:
                G.add_edge(0, id)
        else:
            G.nodes[current_node]['content'] += line
            # all_counters.append(counter)
            # all_numbers.append(numbers)
            # all_lines.append(line)

    F = nx.complete_graph(5)
    # for i in range(len(all_lines)):
    #     id = int(''.join(all_numbers[i]))
    #     G.add_node(id)
    #     G.nodes[id]['lvl'] = all_counters[i]
    #     G.nodes[id]['parents'] = all_numbers[i]
    #     G.nodes[id]['txt'] = all_lines[i]
    #     if len(all_numbers[i]) > 1:
    #         G.add_edge(id, int(''.join(all_numbers[i][:len(all_numbers[i]) - 1:])))

    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    nx.draw(G)
    plt.show()
    print([G.nodes[n]['title'] for n in G.neighbors(1)])
def main():
    filename = askopenfilename(initialdir=r'C:\Users\qwerty\Desktop\Bartosz Wolak\D&D\DM')
    with codecs.open(filename, 'r', 'utf-8') as f:
        linesToTree(f.read().replace('\r','').split('\n'))



if __name__ == '__main__':
    main()