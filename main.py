from algorithm import *
from graph_generator import *
from GUI import *


if __name__ == '__main__':
    main.labels = []
    start_interaction()

    a = algorithm(graph=main.graph)
    adjacency = main.graph.get_adjacency()
    a.calculate()
    colours = a.get_ct()
    chromatic = a.get_b()
    show_graph_with_labels(main.graph.get_adjacency(), colours, main.labels, chromatic)
    new_adjacency = copy.deepcopy(adjacency)

    while True:
        adjacency = copy.deepcopy(new_adjacency)
        print_list(main.labels)

        print_boxes(colours, main.labels, a.get_b())

        new_node = input('\n\tEnter a name for the new item:\n\t└—→ ')
        if main.labels.__contains__(new_node):
            print(b_colors.FAIL + "\tThe item has already been added." + b_colors.END + "\n\t↓")
            continue

        neighbors = input('\tEnter space-separated indexes of items with which the added '
                          'item cannot be stored.\n\t└—→ ')

        if verify(neighbors, len(main.labels)):
            list_of_indexes = list(map(int, neighbors.split()))
            for i in range(len(list_of_indexes)):
                list_of_indexes[i] = list_of_indexes[i] - 1

            main.labels.append(new_node)
            new_adjacency = []
            for i in range(len(main.labels) - 1):
                if i in list_of_indexes:
                    new_row = adjacency[i] + [1]
                else:
                    new_row = adjacency[i] + [0]
                new_adjacency.append(new_row)
            last_row = []
            for i in range(len(main.labels)):
                if i in list_of_indexes:
                    last_row.append(1)
                else:
                    last_row.append(0)
            new_adjacency.append(last_row)

            g = main.generator.get_graph(new_adjacency)

            a = algorithm(graph=g)
            adjacency = main.graph.get_adjacency()
            a.calculate()
            colours = a.get_ct()
            chromatic = a.get_b()
            show_graph_with_labels(g.get_adjacency(), colours, main.labels, chromatic)
        else:
            print(b_colors.FAIL + "\tIncorrectly entered data." + b_colors.END + "\n\t↓")
