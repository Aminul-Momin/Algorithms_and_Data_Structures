
import collections
"""
Consider a foreman responsible for a number of tasks on the factory floor. Each task starts at a fixedtime and ends at a fixed time. The foreman wants to visit the floor to check on the tasks. Your jobis to help him minimize the number of visits he makes. In each visit, he can check on all the taskstaking place at the time of the visit. A visit takes place at a fixed time, and he can only check ontasks taking place at exactly that time. For example, if there are tasks at times 10,3f,12,61,13,41,16,9),then visit times 0,2,3,6 cover all tasks. A smaller set of visit times that also cover all tasks is 3,6. Inthe abstract, you are to solve the following problem.You are given a set of closed intervals. Design an efficient algorithm for finding a minimum sizedset of numbers that covers all the intervals.Hint: Think about extremal points.
"""
Interval = collections.namedtuple('Interval', ('left', 'right'))


def find_minimum_visits(intervals):

    # Sort intervals based on the right endpoints.
    intervals.sort(key=operator.attrgetter('right'))
    last_visit_time, num_visits = float('-inf'), 0
    for interval in intervals:
        if interval.left > last_visit_time:
            # The current right endpoint, last_visit_time, will not cover any
            # more intervals.
            last_visit_time = interval.right
            num_visits += 1
    return num_visits
