#!/usr/bin/env python2
"""
    Shared variables between the program files.
    THESE VALUES CHANGE AT RUNTIME.

"""

# shared global variables
BARRIERS         = []  # keeps track of the barriers
POPULATION       = []  # keeps track of the population object
ANIMATION_FRAMES = []  # stores the ant sprite animation frames

BARRIER_START = PVector(0, 0) # mark the start of the barrier
BARRIER_END   = PVector(0, 0) # mark the end of the barrier

START_TIME = 0        # used for calculating the elapsed time
