
import itertools
import bisect
import random


""" [EPI: 5.16] . """


def nonuniform_random_number_generation(values, probabilities):

    prefix_sum_of_probabilities = list(itertools.accumulate(probabilities))
    interval_idx = bisect.bisect(prefix_sum_of_probabilities, random())
    return values[interval_idx]
