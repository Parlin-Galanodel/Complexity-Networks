# -*- coding: utf-8 -*-
"""
This is the class describe each site in a pile in 1-d oslo model

"""

# import the default random number generator from numpy random pakage
import numpy as np

class Site(object):
    # set a random number generator as class variable
    rng = np.random.default_rng()

    # initialise the site as 0 height, therehold with probability p as first
    # choice, (1-p) as second choice, the initial slope is 0 as height are
    # always initialised to 0 in this case
    def __init__(self, height = 0, therehold_slope = (1,2), p = 0.5):
        self.height = height
        self.slope_choice = therehold_slope
        self.therehold = p
        self.therehold_slope = self.slope_choice[0] if Site.rng.uniform() < \
                self.therehold else self.slope_choice[1]
        self.slope = 0

    # define the frequently used method add_grain to add 1 grain to the site
    def add_grain(self):
        self.height += 1
        self.slope += 1

    # the site lose grain by toppling
    def topple(self):
        # the height decrease by 1 if lose a grain, but the slope decrease by
        # 2 as the next site gain a grain, after toppling, the therehold slope
        # should be updated
        self.height -= 1
        self.slope -= 2
        self.therehold_slope = self.slope_choice[0] if Site.rng.uniform() < \
                self.therehold else self.slope_choice[1]

    # method to reset the site
    def reset(self):
        self.height = 0
        self.therehold_slope = self.slope_choice[0] if Site.rng.uniform() < \
                self.therehold else self.slope_choice[1]
        self.slope = 0
