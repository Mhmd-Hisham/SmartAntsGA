#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

    Abstract Population class for the GA.

"""

__author__  = "Mohamed Hisham"
__email__   = "Mohamed00Hisham@Gmail.com"
__status__  = "Development"
__license__ = "GPL-3.0"
__version__ = "1.0.1"

import random

class Population:
    """
        Abstract Population class for the GA.
    """
    
    generation_number = 0
    tournament_sample_percentage = 50
    
    def __init__(self, population_size, population=[]):
        """ Initializing the population object. """
        # set the population size
        self.population_size = population_size
        
        # create a random population if no population was given
        self.population = population if population else [self.random_individual() for _ in range(population_size)]
    
    def tournament_selection(self):
        """ Tournament selection. """
        
        # calculate the sample size
        sample_size = max(int((self.tournament_sample_percentage*self.population_size)/100.0), 2)
        sample_size = min(self.population_size, sample_size)
        
        # get the sample
        sample = random.sample(self.population, sample_size)
        
        # return the fittest
        return max(sample, key=lambda individual: individual.fitness)

    def evolve(self, selection_func=tournament_selection):
        """Evolve the current population. (Select two random parents, apply crossover & mutaiton between them.) """
        # copy the current population
        new_population = list(self.population)

        for i in range(self.population_size):
            # select random parents
            father = selection_func(self)
            mother = selection_func(self)
            
            # apply crossover between the parents
            child = father.crossover(mother)
            
            # apply mutation to the child
            child.mutate()
            
            # add to the new population
            new_population[i] = child
        
        # update the current population
        self.population = list(new_population)
        
        # increment generation number
        self.generation_number += 1

    def get_best_individual(self):
        """ Returns the best individual in current population. """
        return max(self.population, key=lambda individual: individual.fitness)

    def get_worst_individual(self):
        """ Returns the worst individual in current population. """
        return min(self.population, key=lambda individual: individual.fitness)

    def run(self, no_generations):
        """ Runs & evolves the population multiple times. """
        for _ in range(no_generations):
            self.evolve()
    
    def random_individual(self):
        """ Overload this method when you inherit from this class."""
        pass
