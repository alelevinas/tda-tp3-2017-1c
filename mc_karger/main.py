import os
from common.graph import create_graph_from_file
from mc_karger.karger import KargerMC


def main(argv):
    file = argv
    g = create_graph_from_file(os.getcwd() + "/" + file, False)  # no dirigido
    d = KargerMC(g)

    print("Minimum cut of graph {} is: {}".format(file, d))
    # print("Path to 9: {}  from {}".format(d.path_to(9), s))


if __name__ == "__main__":

    main("10.txt")
