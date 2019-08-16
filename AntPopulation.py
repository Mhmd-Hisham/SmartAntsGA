#!/usr/bin/env python2
"""
    The ant population class.

"""

from Ant import Ant
from GA.Population import Population

class AntPopulation(Population):
    """ The ant population class implmentation. """

    # keeps count of how many ants have reached the goal and/or died
    finished_count = 0
    
    # tournament selection sample percentage
    tournament_sample_percentage = 25
   
    def random_individual(self):
        """ return a new individual ant for the initialization of the first population. """
        return Ant()
    
    def update_and_show(self):
        for ant in self.population:
            ant.update()
            ant.show()

            self.finished_count += (ant.reached_target or ant.dead)
    
        # there is no point in continuing if all the ants have finished
        # so, evolve the population to the next generation        
        if (self.finished_count == self.population_size):
            self.evolve()
        
        # reset counter to zero each time
        self.finished_count = 0
