#!/usr/bin/env python2
"""
    Smart Ants using Genetic Algorithm.
    The project is written in python2 since the processing IDE only runs python2.
    But the code itself can run in both python2 & python3 without any editing.
"""

import time
import random

from Ant import Ant
from AntPopulation import AntPopulation
from Barrier import Barrier
import config
import shared
from Sprites import load_frames
from utilities import sec_to_hms_format

def setup():
    # size of the window
    size(config.WIDTH, config.HEIGHT)
    
    # background color
    background(config.BACKGROUND)

    # load the ant animation frames into memory and put them into the FRAMES list
    shared.ANIMATION_FRAMES = load_frames(config.SPRITE_SHEET, config.SPRITE_SHEET_DATA)[0]
    
    # Create the initial ant population
    shared.POPULATION = AntPopulation(population_size=config.POP_SIZE)
    
    # calculate the start time
    shared.START_TIME = time.time()

def draw():
    background(config.BACKGROUND)

    # update the population
    shared.POPULATION.update()
    
    # get the best of the current generation
    best_ant = shared.POPULATION.get_best_individual()
    worst_ant = shared.POPULATION.get_worst_individual()
    
    # draw a green shadow around the current best ant
    fill(config.GREEN)
    noStroke()
    ellipse(best_ant.pos.x, best_ant.pos.y, config.SHADOW_RADIUS, config.SHADOW_RADIUS)

    # draw a red shadow around the current worst ant
    fill(config.RED)
    noStroke()
    ellipse(worst_ant.pos.x, worst_ant.pos.y, config.SHADOW_RADIUS, config.SHADOW_RADIUS)

    # Draw barrieers
    for barrier in shared.BARRIERS:
        barrier.show()

    # Draw the population
    shared.POPULATION.show()

    # Draw the target
    fill(config.TARGET_COLOR)
    noStroke()
    ellipse(config.TARGET.x, config.TARGET.y, config.TARGET_RADIUS, config.TARGET_RADIUS)
    fill(config.TARGET_HUE_COLOR)
    ellipse(config.TARGET.x, config.TARGET.y, config.TARGET_HUE_RADIUS, config.TARGET_HUE_RADIUS)
    
    # get which frame is currently being displayed (maximum gene_index)
    frame = max(shared.POPULATION.population, key=lambda ant: ant.gene_index).gene_index
    time_elapsed = sec_to_hms_format(time.time()-shared.START_TIME)

    # Draw statistics text  
    fill(config.TEXT_COLOR)
    textSize(config.TEXT_SIZE)
    text("Frame: {}".format(frame), 10, 30)
    text("Lifespan: {}".format(best_ant.lifespan), 10, 50)
    text("Generation: {}".format(shared.POPULATION.generation_number), 10, 70)
    text("Population size: {}".format(shared.POPULATION.population_size), 10, 90)
    text("Max fitness: {}".format(round(best_ant.fitness, 4)), 10, 110)
    text("Time elapsed: {}".format(time_elapsed), 10, 130)

############################# Adding and removing barriers #############################
def mouseReleased():
    barrier_length = shared.BARRIER_START.dist(shared.BARRIER_END)
    
    if (barrier_length > config.MINIMUM_BARRIER_LENGTH and shared.BARRIER_START.x != mouseX):
        shared.BARRIERS.append(Barrier(shared.BARRIER_START, shared.BARRIER_END))

def mousePressed():
    shared.BARRIER_START = PVector(mouseX, mouseY)

def mouseDragged():
    shared.BARRIER_END = PVector(mouseX, mouseY)

def keyPressed():
    if (key == BACKSPACE):
        if len(shared.BARRIERS) != 0:
            shared.BARRIERS.pop()
########################################################################################
