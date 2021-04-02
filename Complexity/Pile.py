# -*- coding: utf-8 -*-
"""
This is the class simulate the pile in 1-d oslo model

"""

from Site import *

class Pile(object):
    def __init__(self, length, height = 0, therehold_slope = (1,2), p = 0.5):
        self.data = [Site(height, therehold_slope, p) for _ in
                              range(length)]
        self.length = length
        self.ava_size = 0
        self.crossover = False
        self.crossover_position = None
        self.grains = 0

    # the reset function used to resimulate with the same case easily
    def reset(self):
        for site in self.data:
            site.reset()
        self.crossover = False

    def get_height(self):
        return self.data[0].height

    # for test use, check wether the model worked as expected, we need to get
    # height, slope and therehold slope of all sites
    def get_heights(self):
        return [i.height for i in self.data]

    def get_slope(self):
        return [i.slope for i in self.data]

    def get_therehold_slope(self):
        return [i.therehold_slope for i in self.data]

    # drop a grain, this is the driven force of this model
    def drop_grain(self, index = 0):
        # reset avalance size for each time drop grain
        self.ava_size = 0
        self.grains += 1
        self.data[index].add_grain()

    # after droping a grain, relax might be needed to fufill the slope constraints
    def relax(self, index = 0):
        self.data[index].topple()
        self.ava_size += 1
        if index == 0:
            self.data[1].add_grain()
        elif index < self.length - 1:
            self.data[index-1].slope += 1
            self.data[index+1].add_grain()
            if index == self.length - 2:
                self.data[-1].slope = self.data[-1].height
        else:
            self.data[index-1].slope += 1
            self.data[index].slope = self.data[index].height
            self.crossover = True

    # all the site need to be relaxed
    def unstable_index(self):
        return [i for i, site in enumerate(self.data) if \
                site.slope > site.therehold_slope]

    # the whole step of a simulation, drop one grain and relax until all the
    # sites stable.
    def simulate(self):
        # simulate 1 iteration which includes drop a grain and relaxation
        self.drop_grain()
        while True:
            unstable = self.unstable_index()
            if not unstable:
                break
            for i in unstable:
                self.relax(i)

