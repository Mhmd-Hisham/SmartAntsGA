#!/usr/bin/env python2
"""
    Smart Ants using Genetic Algorithm.
    The project is written in python2 since the processing IDE only runs python2.
    But the code itself can run in both python2 & python3 without any editing.
"""

import time
import random

from config import *
from utilities import sec_to_hms_format

from Ant import Ant
from AntPopulation import AntPopulation

from Barrier import Barrier
from Sprites import load_frames

def setup():
    global POPULATION, FRAMES, START_TIME

    # size of the window
    size(WIDTH, HEIGHT)
    
    # background color
    background(BACKGROUND)

    # load the ant animation frames into memory and put them into the FRAMES list
    FRAMES.extend(load_frames(SPRITE_SHEET, SPRITE_SHEET_DATA)[0])
    
    # Create the initial ant population
    POPULATION = AntPopulation(population_size=POP_SIZE)
    
    # calculate the start time
    START_TIME = time.time()

def draw():
    background(BACKGROUND)

    # Draw barrieers
    for barrier in BARRIERS:
        barrier.show()

    # get the best of the current generation
    best_ant = POPULATION.get_best_individual()
    worst_ant = POPULATION.get_worst_individual()
    
    # draw a green shadow around the current best ant
    fill(155, 255, 157)
    noStroke()
    ellipse(best_ant.pos.x, best_ant.pos.y, 30, 30)

    # draw a red shadow around the current worst ant
    fill(255, 155, 157)
    # fill(155, 157, 255)
    noStroke()
    ellipse(worst_ant.pos.x, worst_ant.pos.y, 30, 30)

    # Draw the ants population
    POPULATION.update_and_show()

    # Draw the target
    fill(0)
    noStroke()
    ellipse(TARGET.x, TARGET.y, 20, 20)
    fill(50, 100)
    ellipse(TARGET.x, TARGET.y, 40, 40)
    
    # get which frame is currently playing
    frame = max(POPULATION.population, key=lambda ant: ant.gene_index).gene_index
    time_elapsed = sec_to_hms_format(time.time()-START_TIME)

    # Draw statistics text    
    fill(0)
    textSize(15)
    text("Frame: {}".format(frame), 10, 30)
    text("Lifespan: {}".format(best_ant.lifespan), 10, 50)
    text("Generation: {}".format(POPULATION.generation_number), 10, 70)
    text("Population size: {}".format(POPULATION.population_size), 10, 90)
    text("Max fitness: {}".format(round(best_ant.fitness, 4)), 10, 110)
    text("Time elapsed: {}".format(time_elapsed), 10, 130)

############################# Adding and removing barriers #############################
def mouseReleased():
    barrier_length = BARRIER_START.dist(BARRIER_END)
    
    if (barrier_length > MINIMUM_BARRIER_LENGTH and BARRIER_START.x != mouseX):
        BARRIERS.append(Barrier(BARRIER_START, BARRIER_END))

def mousePressed():
    global BARRIER_START
    BARRIER_START = PVector(mouseX, mouseY)

def mouseDragged():
    global BARRIER_END
    BARRIER_END = PVector(mouseX, mouseY)

def keyPressed():
    if (key == BACKSPACE):
        if len(BARRIERS) != 0:
            BARRIERS.pop()
########################################################################################
