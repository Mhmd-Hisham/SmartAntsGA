#!/usr/bin/env python2
"""
    Project settings & shared variables.

"""

# environment settings
WIDTH, HEIGHT = 1200, 600           # window width & height
BARRIER_COLOR = color(0, 0, 0)      # barrier color
BACKGROUND = color(255, 255, 184)   # background color

# shared global variables
BARRIERS   = []       # keeps track of the barriers
POPULATION = []       # keeps track of the population object
FRAMES     = []       # stores the ant sprite animation frames

START_TIME = 0        # used for calculating the elapsed time

BARRIER_START = PVector(0, 0) # mark the start of the barrier
BARRIER_END   = PVector(0, 0) # mark the end of the barrier
MINIMUM_BARRIER_LENGTH = 30   # minimum barrier length

# sprite animation files
SPRITE_SHEET       = "animation/ant.png"    # the sprite sheet
SPRITE_SHEET_DATA  = "animation/ant.json"   # sprite sheet json data

# sprite animation properties
FRAME_WIDTH = 20     # sprite animation frame width
FRAME_HEIGHT = 26    # sprite animation frame height

# initial positions
TARGET            = PVector(WIDTH/2, 40)      # position of the target
INIT_POSITION     = PVector(WIDTH//2, HEIGHT) # initial ants position
INIT_VELOSITY     = PVector(0, 0)             # initial ants velosity
INIT_ACCELERATION = PVector(0, 0)             # initial ants acceleration

# genetic algorithm settings
POP_SIZE           = 50          # population size
LIFE_SPAN          = 250          # ants life span
INIT_MUTATION_RATE = 0.01         # initial mutation rate for each ant

# physics constants
# DO NOT CHANGE THESE VALUES, AS IT MIGHT BREAK THE COLLISION DETECTION IN THE BARRIERS
MAX_FORCE = 0.8       # maximum force applied to an ant
MAX_VELOSITY = 5      # maximum ant velosity
