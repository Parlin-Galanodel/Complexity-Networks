import networkx as nx
import random
from numba import jit


def pref(N, m=3, n=3, seed=10):
    """This function generate a BA graph of N nodes with each added node have m
    edges.

    Parameters
    ----------
    N: total number of nodes
    m: number of edges attached to each new node, or degree of new node.
       random: a random number generator to satisfy the stochastic process.
    n: number of nodes for initial graph, when n=m+1, this methods equals to
       pure random attachment method
    seed: the random seed

    Returns
    -------
    A Barabasi Albert Graph object created by nexworkx, edges of new nodes
    determined by preferential attachment.
    """
    # first make sure the edges of new node is an legal option
    if not (isinstance(m, int) and isinstance(N, int)
            and isinstance(n, int)):
        raise Exception("N, m, n must all be an integer")
    if m >= N:
        raise Exception("too many edges, greater than N")
    if m < 1:
        raise Exception("at least 1 edge for new node")
    if n < m:
        raise Exception("at least m node in initial graph")

    random.seed(seed)

    # Creates new graph of n nodes, of equal degree
    nodes = list(range(n))
    G = nx.complete_graph(nodes)
    G.name = "PrefGraph with N = {}, m = {}".format(N, m)

    # nodes list with occurance probability proportional to k
    # the list is maintained for random sampling
    nodes_list = []
    for i in nodes:
        nodes_list.extend([i]*(n-1))  # initial degree are n-1

    target = set()

    # Target nodes for new edges
    while len(target) < m:
        target.add(random.choice(nodes_list))

    total = n

    while total < N:
        new_stubs = [total]*m
        new_edges = zip(new_stubs, target)
        G.add_edges_from(new_edges)

        # add new edges to the list
        nodes_list.extend(new_stubs)
        nodes_list.extend(list(target))

        # m nodes are chosen from the edge_list to form new targets.
        target = set()
        while len(target) < m:
            random_node = random.choice(nodes_list)
            target.add(random_node)
        # total nodes add 1
        total += 1
    # save the network
    nx.write_adjlist(G, ''.join(('.\\DATA\\', G.name)))


def ran(N, m=3, n=3, seed=10):
    """This function generate a BA graph of N nodes with each added node have m
    edges.

    Parameters
    ----------
    N: total number of nodes
    m: number of edges attached to each new node, or degree of new node.
       random: a random number generator to satisfy the stochastic process.
    n: number of nodes for initial graph, when n=m+1, this methods equals to
       pure random attachment method
    seed: the random seed

    Returns
    -------
    A Barabasi Albert Graph object created by nexworkx, edges of new nodes
    determined by preferential attachment.
    """
    # first make sure the edges of new node is an legal option
    if not (isinstance(m, int) and isinstance(N, int)
            and isinstance(n, int)):
        raise Exception("N, m, n must all be an integer")
    if m >= N:
        raise Exception("too many edges, greater than N")
    if m < 1:
        raise Exception("at least 1 edge for new node")
    if n < m:
        raise Exception("at least m node in initial graph")

    random.seed(seed)

    # Creates new graph of n nodes, and no need for edges
    G = nx.generators.classic.empty_graph(n)
    G.name = "RanGraph with N = {}, m = {}".format(N, m)

    # maintain a nodes_list to do the random choice
    # for random attachement, node i appear 1 times
    nodes_list = list(range(n))

    target = set()
    while len(target) < m:
        random_node = random.choice(nodes_list)
        target.add(random_node)

    total = n

    # generate the whole graph
    while total <= N:
        # the new node equals to the current number of nodes
        new_stubs = [total] * m
        new_edges = zip(new_stubs, target)
        G.add_edges_from(new_edges)

        # add the new node to nodes_list
        nodes_list.append(total)

        # generate new target
        target = set()
        while len(target) < m:
            target.add(random.choice(nodes_list))

        total += 1
    nx.write_adjlist(G, ''.join(('.\\DATA\\', G.name)))


def mix(N, m=3, n=3, q=0.5, seed=10):
    """This function generate a BA graph of N nodes with each added node have m
    edges.

    Parameters
    ----------
    N: total number of nodes
    m: number of edges attached to each new node, or degree of new node.
       random: a random number generator to satisfy the stochastic process.
    n: number of nodes for initial graph, when n=m+1, this methods equals to
       pure random attachment method
    seed: the random seed
    q: the probability that one edge is determined by preferential

    Returns
    -------
    A Barabasi Albert Graph object created by nexworkx, edges of new nodes
    determined by preferential attachment.
    """
    # first make sure the edges of new node is an legal option
    if not (isinstance(m, int) and isinstance(N, int)
            and isinstance(n, int)):
        raise Exception("N, m, n must all be an integer")
    if m >= N:
        raise Exception("too many edges, greater than N")
    if m < 1:
        raise Exception("at least 1 edge for new node")
    if n < m:
        raise Exception("at least m node in initial graph")
    if not (0 <= q <= 1):
        raise Exception("q should be legit probability")

    random.seed(seed)

    # Creates new graph of n nodes, of equal degree
    nodes = list(range(n))
    G = nx.complete_graph(nodes)
    G.name = "MixGraph with N={}, m={}, q={}".format(N, m, q)

    # nodes list with occurance probability proportional to k
    # the list is maintained for random sampling by preferential
    nodes_list = []
    for i in nodes:
        nodes_list.extend([i]*(n-1))  # initial degree are n-1
    # nodes set for all nodes
    # notes that node set is really a list for convinence
    nodes_set = list(range(n))

    total = n

    while total < N:
        new_stubs = [total]*m
        target = set()

        # construct the target
        while len(target) < m:
            if random.random() < q:
                # preferential
                random_node = random.choice(nodes_list)
                while random_node in target:
                    random_node = random.choice(nodes_list)
                target.add(random_node)
            else:
                # pure random
                random_node = random.choice(nodes_set)
                while random_node in target:
                    random_node = random.choice(nodes_set)
                target.add(random_node)

        new_edges = zip(new_stubs, target)
        G.add_edges_from(new_edges)

        # add new edges to the list and update nodes set
        nodes_list.extend(new_stubs)
        nodes_list.extend(list(target))
        nodes_set.append(total)

        total += 1
    nx.write_adjlist(G, ''.join(('.\\DATA\\', G.name)))

