import random

from copy import deepcopy

random.seed()
INF = float("inf")


class KargerMC:
    def __init__(self, g):
        '''
        Calcula las el corte minimo para el grafo g utilizando el alforitmo de Karger.
        :param g: grafo implementando la interfaz de la clase MultiGraph
        '''
        self.g = g
        self.mincutK = INF
        self.mincut = []

        # to achieve a 1 − 1/(n)^c probability of getting the right answer
        c = 10
        iterations = c * nCr(g.V(), 2) * math.log(g.V())
        self.karger_min_cut(iterations)

    def karger_min_cut(self, n):
        for i in range(int(n)):
            g = deepcopy(self.g)
            cut = self.guess_min_cut(g)
            if (len(cut) / 2) < self.mincutK:  # because it has both (u,v) and (v,u) edges
                self.mincutK = len(cut) / 2
                self.mincut = cut

        print(self)

    def guess_min_cut(self, g):
        for i in range(2, g.V()):
            edges = g.iter_edges()
            e = random.sample(list(edges), 1)[0]
            g.collapse_edge(e)
        return list(g.iter_edges())

    def __str__(self):
        r = "Edges:\n"
        for e in self.mincut:
            r += str(e) + "\n"
        return r


import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)
