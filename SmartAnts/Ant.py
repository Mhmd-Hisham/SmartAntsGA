#!/usr/bin/env python2
"""
    The ant class.

"""

import random

from GA.Chromosome import Chromosome

import config
import shared
from Sprites import SpriteAnimation

class Ant(Chromosome):
    """ The ant creature class. """
    
    lifespan = config.LIFE_SPAN                    # the lifespan of the ant creature
    
    mutation_rate = config.INIT_MUTATION_RATE      # ant initial mutation rate
    
    max_force    = config.MAX_FORCE                # maximum force applied to the ant
    max_velosity = config.MAX_VELOSITY             # maximum ant velosity

    initial_pos = config.INIT_POSITION             # initial ant position                                             
    initial_vel = config.INIT_VELOSITY             # initial ant velosity
    initial_acc = config.INIT_ACCELERATION         # initial ant acceleration

    target = config.TARGET                         # the target position

    # the initial distance from the target
    dist_from_target = initial_pos.dist(target)

    def __init__(self, genes_length=lifespan, genes=[]):
        """ Initialization of the ant creature/object. """
        Chromosome.__init__(self, genes_length, genes)
        
        # list of fitnesses for each gene, 
        # helps in picking the best genes in the crossover function
        self.genes_fitness = [0]*self.genes_length

        # keeps track of the last distance before applying a force(gene) to the ant,
        # this helps in calculating the gene fitness, check the update function for more.
        self.last_distance = self.dist_from_target

        # set the initial ant velosity, acceleration, position
        self.vel = self.initial_vel.copy()
        self.acc = self.initial_acc.copy()
        self.pos = self.initial_pos.copy()

        # 
        self.dead = False
        self.reached_target = False
        
        # each frame, a gene is applied for the simiulation,
        # so this helps in keeping track of which gene to apply in any given frame
        self.gene_index = 0

        # the ant sprite animation frames
        self.animation = SpriteAnimation(shared.ANIMATION_FRAMES, config.FRAME_WIDTH, config.FRAME_HEIGHT)

    @property
    def fitness(self):
        """
            The fitness function. 
            The fitness is a number between [0.0, 1.0]
                  1- distance fitness between [0.0, 0.5]
                  2- a bouns fitness between [0.0, 0.5]

            It's calculated as follows, 
            
            1- calculate the percentage of the distance between the ant and the target.
            2- calculate the percentage of the no. remaining genes that were not used.
            
            
            If the ant made it to the target, fitness = (distance_percentage + n_remainig_genes_percentage)/200
            otherwise,                        fitness = (distance_percentage - (n_remainig_genes_percentage/4.0))/200
            
            so if the ant didn't make it to the target, it's fitness becomes how close it is to the target,
            if it did, it's given a bouns fitness based on the number of steps(genes) it has used to reach the goal. (the fewer the better).
        """
        current_dist = self.pos.dist(self.target)
        walked_distance = self.dist_from_target-current_dist
        
        n_remaining_genes = self.genes_length-self.gene_index
        
        genes_percentage = (float(n_remaining_genes)/self.genes_length)*100
        distance_percentage = (walked_distance/self.dist_from_target)*100

        fitness_value = distance_percentage
        
        # give it the bouns only if it has reached the target
        if self.reached_target:
            fitness_value += genes_percentage
        
        # give it a negative bouns if it has died based on the number of steps it has walked (the more the less)
        if self.dead:
            fitness_value -= (genes_percentage/4.0)
        
        fitness_value = (fitness_value/200)
        
        return max(fitness_value, 0)

    def random_gene(self):
        # genes here are represented as forces
        force = PVector.random2D()
        force.setMag(self.max_force)
        return force
    
    def apply_force(self, force):
        # F = m*a; m = 1; F = a
        self.acc.add(force)

    def update(self):
        if self.reached_target or self.dead:
            return
        
        if (self.gene_index == self.genes_length):
            self.dead = True
            return

        d = self.pos.dist(self.target)
        
        self.genes_fitness[self.gene_index] = self.last_distance-d
        self.last_distance = d

        if (d < 10):
            self.reached_target = True
            self.pos = self.target.copy()

        elif self.dead == False:
            # Ant has hit left or right of window
            if (self.pos.x > width or self.pos.x < 0):
                self.dead = True

            # Ant has hit top or bottom of window
            if (self.pos.y > height or self.pos.y < 0):
                self.dead = True
            
            # Ant has touched one of the barriers
            for barrier in shared.BARRIERS:
                if barrier.collision(self.pos):
                    self.dead = True
            
            # if it has crashed from this gene, give the gene a bad fitness
            if self.dead == True:
                self.genes_fitness[self.gene_index] = -1
                        
        self.apply_force(self.genes[self.gene_index])
        if ((not self.dead) and (not self.reached_target)):
            self.vel.add(self.acc)
            self.pos.add(self.vel)
            self.acc.mult(0)
            self.vel.limit(self.max_velosity)

        self.gene_index += 1

    def show(self):
        # Dot animation
        # noStroke()
        # fill(BLACK)
        # ellipse(self.pos.x, self.pos.y, DOT_RADIUS, DOT_RADIUS)
        
        # Ant animation
        push()
        translate(self.pos.x, self.pos.y)
        rotate(self.vel.heading()+HALF_PI)
        
        # showing at (0, 0), since i translated the coordinates to (self.pos.x, self.pos.y)
        self.animation.show(0, 0)
        if ((self.dead == False) and (self.reached_target == False)):
            self.animation.update()

        pop()
    
    def crossover(self, mother):
        """A custom crossover function. """
        
        # copy father genes at first
        child_genes = list(self.genes)
        
        for i in range(self.genes_length):
    
            # choose the best genes according to the gene fitness
            # the gene fitness is calculated in the update method
            # when a force(gene) makes the distance larger between the ant and the target then it was before
            # it's fitness becomes 0, otherwise it's fitness becomes how much that force(gene) made the ant more close to the target
            if self.genes_fitness[i] < mother.genes_fitness[i]:
                child_genes[i] = mother.genes[i]
        
        # return a new ant instance with the new child genes
        return self.__class__(genes_length=self.genes_length, genes=child_genes)
    
    def mutate(self):
        """A custom mutation function. I added mutation to the mutation rate itself :'D """
        
        # mutate the object using the normal mutation method from the chromosome class
        Chromosome.mutate(self)
        
        # the chance of the mutation of the mutation rate of the object xD
        chance = random.uniform(0, 1)
        
        # the change value, [-ve current mutation rate, +ve current mutation rate]
        change = random.uniform(-self.mutation_rate, self.mutation_rate)
        
        # then mutate the mutation rate of the object :'D
        if chance < self.mutation_rate:
            self.mutation_rate = max(self.mutation_rate+change, 0)
