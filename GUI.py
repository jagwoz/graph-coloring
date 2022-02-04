import matplotlib.pyplot as plt
import networkx as nx
import random
from graph_generator import *
import main


class b_colors:
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'


def start_interaction():
    print("1. Add the first two items.\n2. Add the first n elements using a generator.")
    chose = input('└—→ ')
    match chose:
        case "1":
            elements = 0
            while elements < 2:
                new_node = input('\tEnter the name of item number ' + str(elements + 1) + ':\n\t└—→ ')
                if main.labels.__contains__(new_node):
                    print(b_colors.FAIL + "\tThe item has already been added." + b_colors.END + "\n\t↓")
                    continue
                else:
                    main.labels.append(new_node)
                    elements += 1
            main.generator = graph_generator(percent=1)
            main.graph = main.generator.next_graph(2)
        case "2":
            while True:
                nodes_number = input('\tEnter number of nodes:\n\t└—→ ')
                try:
                    nodes_number = int(nodes_number)
                    if 1 < nodes_number < 101:
                        break
                    else:
                        print(b_colors.FAIL + "\tThe number of nodes must be in the range [2 ; 100]" + b_colors.END + "\n\t↓")
                        continue
                except:
                    print(b_colors.FAIL + "\tIncorrectly entered data." + b_colors.END + "\n\t↓")
                    continue

            while True:
                percent = input('\t\tEnter percentage of nodes (0.0 ; 1.0]:\n\t\t└—→ ')
                try:
                    percent = float(percent)
                    if 0 < percent <= 1:
                        break
                    else:
                        print(b_colors.FAIL + "\t\tThe number to be entered must be in the range (0.0-1.0]:"
                              + b_colors.END + "\n\t\t↓")
                        continue
                except:
                    print(b_colors.FAIL + "\t\tIncorrectly entered data." + b_colors.END + "\n\t\t↓")
                    continue

            main.generator = graph_generator(percent=percent)
            main.graph = main.generator.next_graph(nodes_number)
            main.labels = ["Node nr " + str(i + 1) for i in range(nodes_number)]
        case _:
            print(b_colors.FAIL + "Incorrectly entered data." + b_colors.END + "\n↓")
            start_interaction()


def verify(list_of_indexes, number_of_nodes):
    try:
        list_tmp = list(map(int, list_of_indexes.split()))
        if max(list_tmp) > number_of_nodes:
            return False
        return True
    except:
        return False


def print_list(lab):
    print(b_colors.WARNING + "\n\tList of items:" + b_colors.END)
    for i in range(len(lab)):
        print("\t{:d}. {:s}".format(i + 1, lab[i]))


def print_boxes(col, lab, num_col):
    print(b_colors.WARNING + "\n\tList of rooms:" + b_colors.END)
    for i in range(num_col):
        box = []
        for j in range(len(col)):
            if col[j] == i:
                box.append(lab[j])
        print("\t{:d}. {}".format(i + 1, box))


def show_graph_with_labels(adjacency_matrix, colours, labels, chromatic):
    adjacency_matrix = np.array(adjacency_matrix)
    rows, cols = np.where(adjacency_matrix == 1)
    edges = zip(rows.tolist(), cols.tolist())
    gr = nx.Graph()
    gr.add_edges_from(edges)

    c = ["#" + "".join((random.choice("789ABCDEF")) for _ in range(6)) for _ in range(chromatic)]
    color_map = []
    for node in gr:
        color_map.append(c[colours[node]])

    label_dict = {}
    for i in range(len(adjacency_matrix)):
        label_dict[i] = str(i + 1) + ". " + str(labels[i])

    nx.draw(gr, node_color=color_map, labels=label_dict, node_size=750, with_labels=True)
    plt.show()
