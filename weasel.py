#!/usr/bin/env python

"""
weasel.py

Copyright (C) 2012 Peter Somerville

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

-------------------------------------------------

The weasel program, Dawkins' weasel, or the Dawkins weasel is a thought 
experiment and a variety of computer simulations illustrating it. Their aim 
is to demonstrate that the process that drives evolutionary systems -- random 
variation combined with non-random cumulative selection -- is different from 
pure chance.

The thought experiment was formulated by Richard Dawkins, and the first 
simulation written by him; various other implementations of the program have 
been written by others.

http://en.wikipedia.org/wiki/Weasel_program

"""


__author__ = "Peter Somerville"
__email__ = "peterwsomerville@gmail.com"
__version__ = "1.0.0"
__date__ = "28/5/12"

import random
import sys

TARGET = "METHINKS IT IS LIKE A WEASEL"
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

def generate_offspring(num=1):
    pool = []
    for i in xrange(num):
        offspring = [random.choice(ALPHABET) for i in xrange(28)]
        pool.append(offspring)
    return pool

def clone_fittest(fittest, num=50):
    return [fittest for i in xrange(num)]

def get_fitness(child):
    fitness = 0
    for i, char in enumerate(child):
        if char == TARGET[i]:
            fitness += 1
    return fitness

def get_fittest(pool):
    fitnesses = [get_fitness(child) for child in pool]
    return pool[fitnesses.index(max(fitnesses))]

def do_mutation(offspring, locking, mut_prob):
    #offspring = list(offspring)
    for i,char in enumerate(offspring):
        if random.randint(1, mut_prob) == 1:
            if  (locking and offspring[i] != TARGET[i]) or not locking:
                offspring[i] = random.choice(ALPHABET)
    return offspring
            
        
def main():
    print "A Weasel Program in python\n"
    print "http://en.wikipedia.org/wiki/Weasel_program"
    print "*" * 66
    print "Hamlet: Do you see yonder cloud that's almost in shape of a camel?"
    print "Polonius: By the mass, and 'tis like a camel, indeed."
    print "Hamlet: Methinks it is like a weasel."
    print "*" * 66
    print
    
    if len(sys.argv) == 1:
        mut_prob = 2000
    else:
        try:
            mut_prob = int(sys.argv[1])
        except ValueError:
            print "cannot convert argument to integer. exiting"
            print "usage: python weasel.py <mutation probability> (default 2000)"
            sys.exit(1)
    
    evolve(raw_input("Use locking? ").lower().startswith("y"), mut_prob)

def evolve(locking, mut_prob):
    num_generations = 0
    pool = generate_offspring()
    fittest = get_fittest(pool)
    while get_fitness(fittest) != 28:
        num_generations += 1
        pool = clone_fittest(fittest,1)
        pool = [do_mutation(offspring, locking, mut_prob) for offspring in pool]
        fittest = get_fittest(pool)
        print num_generations, "".join(fittest), get_fitness(fittest)


if __name__=="__main__":
    main()