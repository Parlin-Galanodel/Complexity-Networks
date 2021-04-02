# -*- coding: utf-8 -*-
"""
The nunit test for task 1

"""

import Pile
from matplotlib import pyplot as plt
import multiprocessing as mp

# p = Pile.Pile(length = 4)
# q = Pile.Pile(length = 8)
# r = Pile.Pile(length = 16)

# def test(p):
#     p.simulate()
#     print(p.get_height())
#     print(p.get_slope())
#     print(p.get_therehold_slope())
#     print(p.ava_size)

# for i in range(100):
#     test(p)
#     test(q)
#     test(r)

p = Pile.Pile(length = 16)
q = Pile.Pile(length = 32)
d1, d2 = {}, {}



def bar(p, d):
    print("enter bar")
    for i in range(10**5):
        p.simulate()
        d[i+1] = p.get_height()
    return d

def foo(args):
    print("running foo")
    return bar(*args)

if __name__ == "__main__":
    with mp.Pool(2) as pool:
        ret = pool.map(foo,((p,d1),(q,d2)))
        a, b = list(ret[0].values()), list(ret[1].values())
        mean_a = sum(a) / len(a)
        mean_b = sum(b) / len(b)





