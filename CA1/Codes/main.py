
# Press Shift+F10 to execute it.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def create_random_graphs(n):  # create random graph samples given num of nodes
    p = (np.log(n) / n) * (1 + 0.1)  # to make sure graph is connected
    print("Creating Random Graph")
    print("N: ", n)
    print("P: ", p)
    graphs = []
    s = 30
    if n < 2500:
        s = 30
    elif 2500 < n < 5000:
        s = 10
    elif 5000 < n < 1000:
        s = 5
    print("S: ", s)
    while len(graphs) < s:
        graph = nx.erdos_renyi_graph(n, p, seed=None, directed=False)
        if nx.is_connected(graph):
            graphs.append(graph)
    return graphs


def create_grid_graph(dim, n):  # create grid graphs given dimension and num of nodes
    if dim == 1:
        print("Creating 1D Lattice")
        print("N: ", n)
        return [nx.grid_graph(dim=[n])]
    if dim == 2:
        print("Creating 2D Lattice")
        print("N: ", n)
        return [nx.grid_graph(dim=[int(math.sqrt(n)), int(math.sqrt(n))])]
    if dim == 3:
        print("Creating 3D Lattice")
        print("N: ", n)
        return [nx.grid_graph(dim=[int(n ** (1. / 3.)), int(n ** (1. / 3.)), int(n ** (1. / 3.))])]


def get_average_distance(graphs):  # get average distance of given array of sample graphs
    avg_dis = []
    for graph in graphs:
        try:
            avg_dis.append(nx.average_shortest_path_length(graph))
        finally:
            continue
    return avg_dis


def get_average_degree(graphs):  # get average degree of given array of sample graphs
    avg_degrees = []
    for graph in graphs:
        graph_degrees = graph.degree
        sum_degree = 0
        for (a, b) in graph_degrees:
            sum_degree += b
        avg_degrees.append(sum_degree / len(graph_degrees))
    return avg_degrees


def calc_mean(distances):  # get mean of array of data
    return sum(distances) / len(distances)


def get_random_graph_stats(max_n):  # get random graph plot data
    n = 2
    x = []
    y1 = []
    y2 = []
    while n <= max_n:
        graph = create_random_graphs(n)
        avg_dis = calc_mean(get_average_distance(graph))
        avg_deg = calc_mean(get_average_degree(graph))
        index = np.log(n) / np.log(avg_deg) if np.log(avg_deg) > 0 else 1
        print(index)
        x.append(n)
        y1.append(avg_dis)
        y2.append(index)
        n *= 2
    return x, y1, y2


def get_1d_graph_stats(max_n):  # get 1D graph plot data
    n = 2
    x = []
    y1 = []
    y2 = []
    while n <= max_n:
        graph = create_grid_graph(1, n)
        avg_dis = calc_mean(get_average_distance(graph))
        avg_deg = calc_mean(get_average_degree(graph))
        index = n
        print(index)
        x.append(n)
        y1.append(avg_dis)
        y2.append(index)
        n *= 2
    return x, y1, y2


def get_2d_graph_stats(max_n):  # get 2D graph plot data
    n = 2
    x = []
    y1 = []
    y2 = []
    while n ** 2 <= max_n:
        graph = create_grid_graph(2, n ** 2)
        avg_dis = calc_mean(get_average_distance(graph))
        index = n
        x.append(n ** 2)
        y1.append(avg_dis)
        y2.append(index)
        n += 1
    return x, y1, y2


def get_3d_graph_stats(max_n):  # get 3D graph plot data
    n = 2
    x = []
    y1 = []
    y2 = []
    while n ** 3 <= max_n:
        graph = create_grid_graph(3, n ** 3)
        avg_dis = calc_mean(get_average_distance(graph))
        index = n
        x.append(n ** 3)
        y1.append(avg_dis)
        y2.append(index)
        n += 1
    return x, y1, y2


def calc_log(arr):  # get log of array of data
    new_arr = []
    for el in arr:
        new_arr.append(np.log(el))
    return new_arr


def get_distribution_data():  # get distribution data of graph distances from 1 node
    n = int(input("Please enter # of nodes: "))
    m = int(input("Please enter # of samples: "))
    save = input("Save result as png?:(y or n)")

    p = 0.5  # to make sure graph is connected
    graphs = []
    while len(graphs) < m:
        graph = nx.erdos_renyi_graph(n, p, seed=None, directed=False)
        if nx.is_connected(graph):
            graphs.append(graph)
    avg_dis = []
    for g in graphs:
        avg_dis.append(calc_mean(list(nx.shortest_path_length(g, source=0).values())))
    # print(avg_dis)
    plt.hist(np.array(avg_dis))
    if save == "y":
        plt.savefig('distribution.png')
        print("View file at ./distribution.png")
    else:
        plt.show()


def statics():  # main statistics function
    val = int(input("Enter max # of nodes: "))
    save = input("Save result as png?:(y or n)")
    exp_rg_data = get_random_graph_stats(val)
    exp_1d_data = get_1d_graph_stats(val)
    exp_2d_data = get_2d_graph_stats(val)
    exp_3d_data = get_3d_graph_stats(val)

    figure, axis = plt.subplots(2, 3, figsize=(30, 20))

    axis[0, 0].plot(exp_rg_data[0], exp_rg_data[1], label="Random Graph")
    axis[0, 0].plot(exp_rg_data[0], exp_rg_data[2], label="Ln(n)/Ln(<k>)")
    plt.xlabel('# of nodes')
    plt.ylabel('average distance')
    axis[0, 0].legend()
    axis[0, 0].set_title("Random Graph")

    axis[0, 1].plot(exp_1d_data[0], exp_1d_data[1], label="1D Lattice Graph")
    axis[0, 1].plot(exp_1d_data[0], exp_1d_data[2], label="N")
    plt.xlabel('# of nodes')
    plt.ylabel('average distance')
    axis[0, 1].legend()
    axis[0, 1].set_title("1D Lattice")

    axis[0, 2].plot(exp_rg_data[0], exp_rg_data[1], label="Random Graph")
    axis[0, 2].plot(exp_1d_data[0], exp_1d_data[1], label="1D Lattice Graph")
    axis[0, 2].plot(exp_2d_data[0], exp_2d_data[1], label="2D Lattice Graph")
    axis[0, 2].plot(exp_3d_data[0], exp_3d_data[1], label="3D Lattice Graph")
    plt.xlabel('# of nodes')
    plt.ylabel('average distance')
    axis[0, 2].legend()
    axis[0, 2].set_title("Overall Data")

    axis[1, 0].plot(exp_2d_data[0], exp_2d_data[1], label="2D Lattice Graph")
    axis[1, 0].plot(exp_2d_data[0], exp_2d_data[2], label="N^(1/2)")
    plt.xlabel('# of nodes')
    plt.ylabel('average distance')
    axis[1, 0].legend()
    axis[1, 0].set_title("2D Lattice")

    axis[1, 1].plot(exp_3d_data[0], exp_3d_data[1], label="3D Lattice Graph")
    axis[1, 1].plot(exp_3d_data[0], exp_3d_data[2], label="N^(1/3)")
    plt.xlabel('# of nodes')
    plt.ylabel('average distance')
    axis[1, 1].legend()
    axis[1, 1].set_title("3D Lattice")

    axis[1, 2].plot(calc_log(exp_rg_data[0]), calc_log(exp_rg_data[1]), label="Random Graph")
    axis[1, 2].plot(calc_log(exp_1d_data[0]), calc_log(exp_1d_data[1]), label="1D Lattice Graph")
    axis[1, 2].plot(calc_log(exp_2d_data[0]), calc_log(exp_2d_data[1]), label="2D Lattice Graph")
    axis[1, 2].plot(calc_log(exp_3d_data[0]), calc_log(exp_3d_data[1]), label="3D Lattice Graph")
    plt.xlabel('Log(# of nodes)')
    plt.ylabel('Log(average distance)')
    axis[1, 2].legend()
    axis[1, 2].set_title("Overall Data")

    if save == "y":
        plt.savefig('answer.png')
        print("View file at ./answer.png")
    else:
        plt.show()


def main():  # main function
    service = int(input("Please select service: (1 or 2)"))
    if service == 1:
        statics()
    elif service == 2:
        get_distribution_data()
    else:
        print("Wrong input. Please try again")


print("Social Networks Exercise: Compare average distance between random graph and lattice")
print("by: Mohammad Naseri, University of Tehran")
print("")
print("1. Get graphs statistics")
print("2. Get graphs distance distribution")
main()
