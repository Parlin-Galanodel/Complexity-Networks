"""
The data analysis process.

This file contains the functions needed for data analysis and generate
plottings.

"""


import numpy as np
from matplotlib import pyplot as plt
import json
from collections import Counter
from collections import OrderedDict
from scipy import optimize as oz
import math
import log_bin as lb  # the logbin function in this module does not always work
                      # and just try another time if it does not work.
                      # I can't figure out why because it could run
                      # and the error does not make sense because it said my
                      # avalance array is an integer.

sizes = (4, 8, 16, 32, 64, 128, 256, 512)

def moving_average(data, temporal_window=100):
    """the moving average of a sequence implemented by convolution.
    with temperal window = 100 to smooth the data
    """
    window = np.ones(temporal_window) / temporal_window
    return np.convolve(data, window, 'valid')

def calc_prob(data):
    """calculate the probability in the data sequence and store them in
    a dictionary"""
    total = len(data)
    frequencies = sorted(Counter(data).items())
    probabilities = OrderedDict()
    for (key, value) in frequencies:
        probabilities[key] = value / total
    return probabilities

# # task 2a.
# for s in sizes:
#     with open(r"data for {}".format(s), 'r') as d:
#         data = json.load(d)
#         plt.plot(data["heights"], '.', label="{}".format(s))

# plt.xlabel("$t$(time as grains droped")
# plt.ylabel("$h(t;L)$")
# plt.legend(title="system size L")

# # task 2b-d.
# h, l = [], []
# for s in sizes:
#     with open(r"data for {}".format(s), 'r') as d:
#         data = json.load(d)
#         ct = data["crossover time"]+1
#         heights = np.array(data["heights"][ct:])
#         mean = np.mean(heights)
#         # h.append(mean)
#         # l.append(s)
#         std = np.std(heights)
#         # h.append(std)
#         p = calc_prob(heights)
#         x = [(i - mean)/std for i in p.keys()]
#         y = [i*std for i in p.values()]

#         plt.plot(x, y,label = "{}".format(s))
#         # print("for size {}: the average height: {} \n\t std:{}".format(s,
#         #                                                         mean, std))

#         # ah = sum(heights[ct:]) / len(heights[ct:])
#         # print("crossover time is {} and average height is {} for system" \
#         #       " size {}".format(ct, ah, s))
#         # data_smoothed = moving_average(np.array(heights), temporal_window=50)
#         # times = np.arange(25, len(data_smoothed)+25)
#         # plt.figure(1)
#         # plt.plot(times, data_smoothed, label = "{}".format(s))
#         # plt.figure(2)
#         # plt.loglog(times, data_smoothed, label = "{}".format(s))
#         # plt.figure(3)
#         # plt.semilogy(times, data_smoothed, label = "{}".format(s))
#         # plt.figure(4)
#         # plt.loglog(times/s**2, data_smoothed/s, label="{}".format(s))
# # plt.figure(1)
# # plt.xlabel("$t$(time as grains droped)")
# # plt.ylabel("$h(t;L)$")
# # plt.legend(title="system size L")
# # plt.figure(2)
# # plt.xlabel("$t$(time as grains droped")
# # plt.ylabel("$h(t;L)$")
# # plt.legend(title="system size L")
# # plt.figure(3)
# # plt.xlabel("$t$(time as grains droped")
# # plt.ylabel("$h(t;L)$")
# # plt.legend(title="system size L")
# # plt.figure(4)
# # plt.xlabel("$t/L^2$(time as grains droped")
# # plt.ylabel("$h(t;L)/L$")
# # plt.legend(title="system size L")
# # plt.show()
# # (a0,a1,w), cov = oz.curve_fit(lambda x, a0, a1, w: a0*x*(1-a1*x**(-w)), l, h)
# # std = np.sqrt(np.diag(cov))
# # def f(x, a0=a0, a1=a1, w=w):
# #     return a0*x*(1-a1*x**(-w))

# # x = np.linspace(0, 500, 100)
# # y = f(x)

# # plt.loglog(l, h, 'r.', label = "data")
# # plt.xlabel("$L$(the system size)")
# # plt.ylabel('$std(<h(t;L))$')
# def G(x):
#     return math.e**(-0.5*x**2)/math.sqrt(2*math.pi)
# x = np.linspace(-4,4,20)
# y = G(x)
# plt.plot(x,y, label = "normal dist")
# plt.xlabel("$h$")
# plt.ylabel("$P(h;L) with trans formation")
# plt.legend(title = "system size")
# plt.grid()


# Task 3:
# extract the avalance sequence
for s in (sizes):
    with open(r"data for {}".format(s), 'r') as d:
        data = json.load(d)
        ct = data["crossover time"]+1  # start analysis from recurrent state
        avalance = np.array(data["avalance size"][ct:]) # use diff number
                                                        # of points
        s1 = np.mean(avalance)
        s2 = np.mean(np.square(avalance))
        s3 = np.mean(np.power(avalance, 3))
        s4 = np.mean(np.power(avalance, 4))
        print("for size {}".format(s))
        print("\ts1: {}".format(s1))
        print("\ts2: {}".format(s2))
        print("\ts3: {}".format(s3))
        print("\ts4: {}".format(s4))
#         x, y = lb.logbin(data=avalance, scale = 1.05)
#         plt.loglog(x, y, '.', label = "{}".format(s))
# plt.xlabel("$S$(avalance size)")
# plt.ylabel("$P(s;L)")
# plt.grid()
# plt.legend()
# plt.show()

