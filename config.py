#!/usr/bin/env python2
"""
    Project settings & configuration.
    These values DO NOT CHANGE during runtime.

"""

# colors
GREEN = color(155, 255, 157)
RED   = color(255, 155, 157)
BLUE  = color(155, 157, 255)
BLACK = color(0, 0, 0)

# environment settings
WIDTH, HEIGHT = 1200, 600          # window width & height
BACKGROUND = color(245, 250, 250)    # background color

# text settings
TEXT_COLOR = BLACK    # text color
TEXT_SIZE    = 15     # text size

# target settings
TARGET            = PVector(WIDTH/2, 40) # position of the target
TARGET_COLOR      = BLACK                # target color
TARGET_HUE_COLOR  = color(50, 100)       # hue color (around the target)
TARGET_RADIUS     = 20                   # the radius of the target
TARGET_HUE_RADIUS = TARGET_RADIUS + 20   # the radius of the hue around the target

# shadow settings
SHADOW_RADIUS = 30    # shadow radius around the best/worst individuals

# barrier settings
BARRIER_STROKE_WEIGHT  = 2
BARRIER_COLOR          = BLACK     # the color of the barier object
MINIMUM_BARRIER_LENGTH = 30        # minimum barrier length

# sprite animation settings
SPRITE_SHEET       = "animation/ant.png"    # the sprite sheet
SPRITE_SHEET_DATA  = "animation/ant.json"   # sprite sheet json data
FRAME_WIDTH        = 20                     # sprite animation frame width
FRAME_HEIGHT       = 26                     # sprite animation frame height

# dot animation settings
DOT_RADIUS = 7     # check the ant show function

# initial ants values
INIT_POSITION     = PVector(WIDTH//2, HEIGHT) # initial ants position
INIT_VELOSITY     = PVector(0, 0)             # initial ants velosity
INIT_ACCELERATION = PVector(0, 0)             # initial ants acceleration

# genetic algorithm settings
POP_SIZE                     = 50       # population size
LIFE_SPAN                    = 250      # ants life span
INIT_MUTATION_RATE           = 0.01     # initial mutation rate for each ant
TOURNAMENT_SAMPLE_PERCENTAGE = 50       # tournament selection sample percentage

# physics constants
# DO NOT CHANGE THESE VALUES, AS IT MIGHT BREAK THE COLLISION DETECTION IN THE BARRIERS
MAX_FORCE = 0.8       # maximum force applied to an ant
MAX_VELOSITY = 5      # maximum ant velosity
