# -*- coding: utf-8 -*-
"""
Task 2: the height of the Pile, h(t; L)

"""


import json
from multiprocessing import Pool
import Pile


L = (4, 8, 16, 32, 64, 128, 256, 512)
oslo = tuple(map(Pile.Pile, L))

def f(p):
    heights = []
    avas = []
    d = {}
    while not p.crossover:
        heights.append(p.get_height())
        avas.append(p.ava_size)
        p.simulate()
    d["crossover time"] = p.grains
    for i in range(10**6):
        p.simulate()
        heights.append(p.get_height())
        avas.append(p.ava_size)
    d["heights"] = heights
    d["avalance size"] = avas
    path = ".\\data for {}".format(p.length)
    with open(path, 'w') as datafile:
        json.dump(d, datafile)



if __name__ == "__main__":
    # Task 2a:
    with Pool(8) as pool:
        pool.map(f, oslo)
