from collections import namedtuple
from random import shuffle
from functools import partial
#==============================================================================
""" Render a calendar. - [EPI:13.6]. """

# Event is a tuple (start_time, end_time)
Event = namedtuple('Event', ('start', 'finish'))

# Endpoint is a tuple (start_time, 0) or (end_time, 1) so that if times
# are equal, start_time comes first
point = namedtuple('point', ('time', 'is_start'))


def find_max_simultaneous_events(A):

    # Builds an array of all endpoints.
    E = [
        p for event in A
        for p in (point(event.start, True), point(event.finish, False))
    ]

    # Sorts the endpoint array according to the time, breaking ties by putting
    # start times before end times.
    E.sort(key=lambda e: (e.time, not e.is_start))

    # Track the number of simultaneous events, record the maximum number of
    # simultaneous events.
    max_num_simultaneous_events, num_simultaneous_events = 0, 0
    for e in E:
        if e.is_start:
            num_simultaneous_events += 1
            largest = max(num_simultaneous_events, max_num_simultaneous_events)
            max_num_simultaneous_events = largest
        else:
            num_simultaneous_events -= 1
    return max_num_simultaneous_events


def main():
    events = [[1, 5], [2, 7], [4, 5], [6, 10], [8, 9], [9, 17], [11, 13], [12, 15], [14, 15]]
    events = [[1, 5], [5, 9], [9, 10]]

    A = [Event(*x) for x in events]
    # E = [
    #     p for event in A
    #     for p in (point(event.start, True), point(event.finish, False))
    # ]
    # E.sort(key=lambda e: (e.time, not e.is_start))
    # E = [[p.time, p.is_start] for p in E]
    # print(E)

    print(find_max_simultaneous_events(A))


if __name__ == '__main__':
    main()
