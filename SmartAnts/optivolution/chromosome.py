#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

    Abstract Chromosome class for the GA.

"""

__author__  = "Mohamed Hisham"
__email__   = "Mohamed00Hisham@Gmail.com"
__status__  = "Development"
__license__ = "GPL-3.0"
__version__ = "1.0.1"

import functools
import random

class Chromosome:
    """
        Abstract Chromosome class for the GA.
    """
    
    mutation_rate = 0.01
    
    def __init__(self, genes_length, genes=None):
        """ Initializing the Chromosome object. """
        self.genes_length = genes_length
        self.genes = genes if genes else [self.random_gene() for _ in range(genes_length)]

        # leave these as is
        self.fitness_updated = False
        self.fitness_value  = 0.0
    
    def crossover(self, mother):
        """ 
            One point crossover. 
            Performs a crossover operation between two parents, returns a new child object.
        """
        
        # copy father genes
        child_genes = list(self.genes)
        
        # choose a random mid point
        mid = random.randrange(self.genes_length)
        
        # apply crossover
        child_genes[mid:] = mother.genes[mid:]
        
        # return a new child object from the same parent class
        return self.__class__(genes_length=self.genes_length, genes=child_genes)
    
    def mutate(self):
        """
            Apply mutation to object genes.
            Returns a mutated genes list.
        """
        
        # a lambda function to check whether to apply mutation or not
        apply_mutation = lambda: random.uniform(0, 1) < self.mutation_rate
            
        # mutate genes
        mutated_genes = [self.random_gene() if apply_mutation() else self.genes[i] for i in range(self.genes_length)]
        
        # update object genes with the new mutated genes
        self.genes = mutated_genes
    
    def random_gene(self):
        """
            Returns a random gene.
            Overload this method when you inherit from this class.
            It is used to create an initial random DNA.
            It is also used used in the mutation function.
        """

        pass

    def fitness_property(fn):
        """A decorator to wrap the fitness method. """
        @property
        @functools.wraps(fn)
        def inner(self, *args, **kwargs):
            if self.fitness_updated == False:
                self.fitness_value = fn(self, *args, **kwargs)

            self.fitness_updated = True
            return self.fitness_value
        
        return inner

    @fitness_property
    def fitness(self):
        """ 
            The fitness function. 
            Overload this method when you inherit from this class.
            Wrap the method after overloading it with the '@Chromosome.fitness_property' decorator,
            After that, you can access the fitness value of the individual as a property 'individual.fitness'.
            The fitness function is called only once per individual. the second time you try to access 'individual.fitness',
            It would return the same value as the first without recalling the fitness function.
            This can be useful if your fitness function is heavy to compute.
            
            If you wish to calculate your fitness value each time you access it, just wrap the method with '@property'
            python built-in decorator, you can still access the fitness using 'individual.fitness'.
            
            Check the example projects for how to overload this method properly.
        """

        pass

