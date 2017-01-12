#! /usr/bin/env python3

"""
This script will test the solutions to the project euler problems. It will also time the solutions.
"""

import importlib
import time
from operator import itemgetter
import os

solutions = {1: '233168',
             2: '4613732',
             3: '6857',
             4: '906609',
             5: '232792560',
             6: '25164150',
             7: '104743',
             8: '23514624000',
             9: '31875000',
             10: '142913828922',
             11: '70600674',
             12: '76576500',
             13: '5537376230',
             14: '837799',
             15: '137846528820',
             16: '1366',
             17: '21124',
             18: '1074',
             20: '648',
             21: '31626',
             22: '871198282',
             24: '2783915460',
             25: '4782',
             29: '9183',
             30: '443839',
             35: '55',
             36: '872187',
             39: '840',
             50: '997651',
             54: '376',
             67: '7273'}


def print_progress_bar(percentage, time_remaining=0, width=50, symbol='='):
    """
    Print a progress bar.

    :param percentage: percentage of task(s) complete.
    :param time_remaining: time until task completion in seconds.
    :param width: How many symbols represent 100% completion.
    :param symbol: The symbol that is used in the progress bar.
    :raises ValueError:
    """

    if percentage > 100 or percentage < 0:
        raise ValueError

    if time_remaining < 0:
        raise ValueError

    percentage = int(percentage)
    no_of_symbols = int(percentage / 100 * width)
    time_remaining = int(time_remaining)

    # the \r will move the cursor back to start of line, which allows the progress bar to be overwritten
    bar = '[{symbols:' + str(width) + '}] {percentage:3d}% Time Remaining(s): {time:<10d}\r'
    bar = bar.format(symbols=symbol * no_of_symbols, percentage=percentage, time=time_remaining)

    # need end='' so that the print function doesn't print a \n at the end of the line
    print(bar, end='', flush=True)


def test():
    problems = []

    # get list of euler problems that are solved
    euler_dir = os.path.join(os.path.dirname(__file__), "euler")
    for f in os.listdir(euler_dir):
        if os.path.isfile(os.path.join(euler_dir, f)):
            try:
                name_without_extension = os.path.splitext(f)[0]
                problems.append(int(name_without_extension))
            except ValueError:
                continue

    number_of_problems = len(problems)
    test_start_time = time.time()

    # list of tuples of format (problem, time_taken, solution)
    data = []

    # solve the problems, time them, and test the solutions
    for index, problem in enumerate(problems):
        problem_module = importlib.import_module("euler.{}".format(problem))
        start_time = time.time()
        solution = problem_module.solve()
        end_time = time.time()
        time_taken = (end_time - start_time) * 1000
        assert solutions[problem] == str(solution)
        data.append((problem, time_taken, solution))

        problems_complete = index + 1
        problems_remaining = number_of_problems - problems_complete
        percentage_complete = int(problems_complete / number_of_problems * 100)
        average_time = (end_time - test_start_time) / problems_complete
        time_remaining = int(average_time * problems_remaining)
        print_progress_bar(percentage_complete, time_remaining)

    # sort by decreasing time
    data.sort(key=itemgetter(1), reverse=True)

    # print the results
    header = '{:10} {:10} {}'.format('Problem', 'Time(ms)', 'Solution')
    print('\n')
    print(header)
    for problem, time_taken, solution in data:
        row = '{:<10d} {:<10.3f} {}'.format(problem, time_taken, solution)
        print(row)


if __name__ == '__main__':
    test()
