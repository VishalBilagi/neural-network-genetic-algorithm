"""
Called from `main.py`. Ties everything together.
"""
from operator import attrgetter
from optimizer import Optimizer
from random import shuffle
from statistics import mean
import random
import sys
import timeit

def train_networks(networks):
    """Train each network.
    
    Args:
        networks (list): Current population of networks.
    
    """
    for network in networks:
        network.train_network()

def get_average_accuracy(networks):
    """Get the average accuracy for a group of networks.
    
    Args:
        networks (list): List of networks.
    
    Returns:
        float: The average accuracy of a population of networks.
    
    """
    total_accuracy = 0
    for network in networks:
        total_accuracy += network.accuracy

    return total_accuracy / len(networks)

def generate(generations, population, neuron_choices):
    """Generate a network with the genetic algorithm.
    
    Args:
        generations (int): Number of times to evole the population.
        population (int): Number of networks in each generation.
        neuron_choices (list): A list of possible layer widths.
    
    """
    choice = None

    optimizer = Optimizer(neuron_choices)
    networks = optimizer.create_population(population)

    # Evolve the generation.
    for i in range(generations):
        print("***Doing generation %d of %d***" %
              (i + 1, generations))

        # Train and get accuracy for networks.
        train_networks(networks)

        # Get the average accuracy for this generation.
        average_accuracy = get_average_accuracy(networks)

        # Print out the average accuracy each generation.
        print('-'*80)
        print("Generation average: %.2f%%" % (average_accuracy * 100))
        print('-'*80)

        # Evolve, except on the last iteration.
        if i != generations - 1:
            # Do the evolution.
            networks = optimizer.evolve(networks)
        
    # Sort our final population.
    networks = sorted(networks, key=lambda x: x.accuracy, reverse=True)

    # Print out which ones did best.
    print_networks(networks)

def print_networks(networks):
    """Print a list of networks.

    Args:
        networks (list of lists): A list of networks.

    """
    for network in networks:
        print('-'*80)
        network.print_network()
