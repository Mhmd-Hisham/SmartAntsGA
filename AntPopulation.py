#!/usr/bin/env python2
"""
    The ant population class.

"""

from GA.Population import Population

from Ant import Ant
import config

class AntPopulation(Population):
    """ The ant population class implmentation. """

    # counts how many ants have reached the goal/died per frame
    finished_count = 0
    
    # tournament selection sample percentage
    tournament_sample_percentage = config.TOURNAMENT_SAMPLE_PERCENTAGE
   
    def random_individual(self):
        """ return a new individual ant for the initialization of the first population. """
        return Ant()
        
    def update(self):
        """ Update the values of each individual in the population. """
        for ant in self.population:
            ant.update()

            self.finished_count += (ant.reached_target or ant.dead)
    
        # there is no point in continuing if all the ants have finished
        # so, evolve the population to the next generation        
        if (self.finished_count == self.population_size):
            self.evolve()
        
        # reset counter to zero each time
        self.finished_count = 0
    
    def show(self):
        """ Draw each individual in the population"""
        for ant in self.population:
            ant.show()
