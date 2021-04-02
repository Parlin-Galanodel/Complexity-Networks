# for degree distribution, we need to count the occurrance
# of each degree, this could easily and fastly done by
# python stdlib
from collections import Counter
# C-array like data structure supported by numpy
import numpy as np


def k_distri(G):
    """
    Find the degree distribution of a graph G

    Parameters
    ----------
    G : networkx.Graph
        the targeted graph we want to find degree distribution

    Returns
    -------
    None.

    """

    # degree data
    degree = np.array([d for n, d in G.degree])
    degree.sort()
    total = degree.size

    # count the degree occurance
    degree, occurance = zip(*Counter(degree).items())

    degree, occurance, frequencies = np.array(degree),\
        np.array(occurance), np.array(occurance) / total
    return (degree, occurance, frequencies)

