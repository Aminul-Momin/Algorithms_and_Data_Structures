from itertools import islice
from random import randrange

#==============================================================================
"""
Design a program that takes as input a size k, and reads packets,
continuously maintaining a uniform random subset of size k of the read packets.
- [EPI: 5.13]. """

# Assumption: there are at least k elements in the stream.
#==============================================================================


def online_random_sample(stream, k):

    # Stores the first k elements.
    running_sample = list(islice(stream, k))

    # Have read the first k elements.
    num_seen_so_far = k
    for x in stream:
        num_seen_so_far += 1
        # Generate a random number in [0, num_seen_so_far - 1], and if this
        # number is in [0, k - 1], we replace that element from the sample with
        # x.
        idx_to_replace = randrange(num_seen_so_far)
        if idx_to_replace < k:
            running_sample[idx_to_replace] = x
    return running_sample
