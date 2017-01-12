#! /usr/bin/env python3

"""
This script will print a solution to one of the project-euler problems.
"""

import importlib
import time

if __name__ == '__main__':
    problem = input("Enter the problem number to solve: ")
    try:
        problem = int(problem)
        problem_module = importlib.import_module('euler.{}'.format(problem))
        print("Solving...")
        start_time = time.time()
        solution = problem_module.solve()
        end_time = time.time()
        time_taken = (end_time - start_time) * 1000
        print("Solution: {}".format(solution))
        print("Time taken: {:.3f} ms".format(time_taken))
    except ValueError:
        print("That is not a valid problem number.")
    except ImportError:
        print("No solution found for the requested problem.")
