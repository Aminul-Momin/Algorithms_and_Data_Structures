import collections
import itertools
import functools
from random import randint, randrange

from ads.fundamentals import SLLNode as Node
from ads.utils import *
#==============================================================================
""" Compute the intersection of two sorted arrays. - [EPI:13.1]. """


def A_intersection_B(A, B):
    a, b, aAndB = 0, 0, []

    while a < len(A) and b < len(B):
        if A[a] < B[b]: a += 1
        elif A[a] > B[b]: b += 1
        elif (a == 0 or A[a - 1] != A[a]):  # A[a] == B[b] and A[a-1] != A[a]
            aAndB.append(A[a])
            a, b = a + 1, b + 1
        else:
            b += 1  # A[a] == B[b] and A[a-1] == A[a]

    return aAndB


# Returns the intersection of this set and that set.
def intersects(this, that):
    if that is None:
        raise ValueError("called intersects() with a null argument")
    c = set()
    if len(this) < len(that):
        for x in this:
            if x in that:
                c.add(x)
    else:
        for x in that:
            if x in this:
                c.add(x)
    return c


def intersect_two_sorted_arrays(A, B):
    return [a for i, a in enumerate(A) if (i == 0 or a != A[i - 1]) and a in B]


def _test_A_intersectios_B():
    for _ in range(1000):
        N, M = randrange(0, 50), randrange(0, 50)
        A = sorted([randint(-10, 10) for _ in range(N)])
        B = sorted([randint(-10, 10) for _ in range(M)])
        L1, L2 = intersect_two_sorted_arrays(A, B), A_intersection_B(A, B)
        assert L1 == L2


""" Given three ascending order sorted arrays of inte­gers, find out all the com­mon ele­ments in them. - [18]. """


def A_intersect_B_intersect_C(A, B, C):
    pass


def _test_A_intersect_B_intersect_C(A, B, C):
    pass


""" Find intersection-POINT between Two Sorted Arrays. """


def intersecttion_point(A, B):
    pass


def _test_intersecttion_point(A, B):
    pass


"""
You are given two sorted arrays, A and B, where A has a large enough
buffer at the end to hold B. Write a method to merge B into A in sorted
order - [EPI:13.2, CtCI: 11.1].
"""


def merge_two_sorted_arrays(A, m, B, n):

    a, b, write_idx = m - 1, n - 1, m + n - 1

    while a >= 0 and b >= 0:
        if A[a] > B[b]:
            A[write_idx] = A[a]
            a -= 1
        else:
            A[write_idx] = B[b]
            b -= 1
        write_idx -= 1

    while b >= 0:
        A[write_idx] = B[b]
        write_idx, b = write_idx - 1, b - 1


def _test_merge_two_sorted_arrays(verbose=False):
    #     seed(0)
    r1 = randrange(10)
    r2 = randrange(r1, 20)
    L1 = sorted([randrange(-5, 6) for _ in range(r1)])
    L2 = sorted([randrange(-5, 6) for _ in range(r2)])

    L1 = L1 + [None] * (len(L2))
    if verbose:
        print(f'Before Merge: (r1 = {r1}, r2 = {r2}) \n\t {L1} \n\t {L2}')
    merge_two_sorted_arrays(L1, r1, L2, r2)
    if is_sorted(L1) and verbose: print(f'After Merge: \n\t {L1} \n\t {L2}')


""" Computing the h-index.- [EPI:13.3]. """


def h_index(citations):

    citations.sort()
    n = len(citations)
    for i, c in enumerate(citations):
        if c >= n - i:
            return n - i
    return 0


""" Remove first-name duplicates. - [EPI:13.4]. """


class Name:
    def __init__(self, first_name, last_name):
        self.first_name, self.last_name = first_name, last_name

    def __eq__(self, other):
        return self.first_name == other.first_name

    def __lt__(self, other):
        return (self.first_name < other.first_name
                if self.first_name != other.first_name else
                self.last_name < other.last_name)

    def __repr__(self):
        return '%s %s' % (self.first_name, self.last_name)


def eliminate_duplicate(A):

    A.sort()  # Makes identical elements become neighbors.
    write_idx = 1
    for cand in A[1:]:
        if cand != A[write_idx - 1]:
            A[write_idx] = cand
            write_idx += 1
    del A[write_idx:]


def eliminate_duplicate_pythonic(A):
    A.sort()
    write_idx = 0
    for cand, _ in itertools.groupby(A):
        A[write_idx] = cand
        write_idx += 1
    del A[write_idx:]


""" Smallest nonconstructible value. - [EPI:13.5]. """


def smallest_nonconstructible_value(A):

    max_constructible_value = 0
    for a in sorted(A):
        if a > max_constructible_value + 1: break
        max_constructible_value += a
    return max_constructible_value + 1


def smallest_nonconstructible_value_pythonic(A):
    func = lambda max_val, a: max_val + (0 if a > max_val + 1 else a)
    return functools.reduce(func, sorted(A), 0) + 1


""" Render a calendar. - [EPI:13.6]. """

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))

# Endpoint is a tuple (start_time, 0) or (end_time, 1) so that if times
# are equal, start_time comes first
Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))


def find_max_simultaneous_events(A):

    # Builds an array of all endpoints.
    E = [
        p for event in A
        for p in (Endpoint(event.start, True), Endpoint(event.finish, False))
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
            max_num_simultaneous_events = max(num_simultaneous_events,
                                              max_num_simultaneous_events)
        else:
            num_simultaneous_events -= 1
    return max_num_simultaneous_events


""" Merging intervals. - [EPI:13.7]. """

Interval = collections.namedtuple('Interval', ('left', 'right'))


def add_interval(intervals, new_interval):

    i, result, N = 0, [], len(intervals)

    # Processes intervals in disjoint-intervals which come before new_interval.
    while (i < N and intervals[i].right < new_interval.left):
        result.append(intervals[i])
        i += 1

    # Processes intervals in disjoint-intervals which overlap with new_interval.
    while (i < N and intervals[i].left <= new_interval.right):
        # If [a, b] and [c, d] overlap, union is [min(a, c), max(b, d)].
        lower_bound = min(new_interval.left, intervals[i].left)
        upper_bound = max(new_interval.right, intervals[i].right)
        new_interval = Interval(lower_bound, upper_bound)
        i += 1

    # Processes intervals in disjoint-intervals which come after new_interval.
    return result + [new_interval] + intervals[i:]


""" Compute the union of intervals. - [EPI:13.8]. """

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))
Interval = collections.namedtuple('Interval', ('left', 'right'))


def union_of_intervals(intervals):

    # Empty input.
    if not intervals: return []

    # Sort intervals according to left endpoints of intervals.
    intervals.sort(key=lambda i: (i.left.val, not i.left.is_closed))
    result = [intervals[0]]
    for i in intervals:
        if intervals and (i.left.val < result[-1].right.val or
                          (i.left.val == result[-1].right.val and
                           (i.left.is_closed or result[-1].right.is_closed))):
            if (i.right.val > result[-1].right.val or
                (i.right.val == result[-1].right.val and i.right.is_closed)):
                result[-1] = Interval(result[-1].left, i.right)
        else:
            result.append(i)
    return result


""" Partitioning and sorting an array with many repeated entries. - [EPI:13.9]. """

Person = collections.namedtuple('Person', ('age', 'name'))


def group_by_age(people):

    age_to_count = collections.Counter((person.age for person in people))
    age_to_offset, offset = {}, 0
    for age, count in age_to_count.items():
        age_to_offset[age] = offset
        offset += count

    while age_to_offset:
        from_age = next(iter(age_to_offset))
        from_idx = age_to_offset[from_age]
        to_age = people[from_idx].age
        to_idx = age_to_offset[people[from_idx].age]
        people[from_idx], people[to_idx] = people[to_idx], people[from_idx]

        # Use age_to_count to see when we are finished with a particular age.
        age_to_count[to_age] -= 1
        if age_to_count[to_age]: age_to_offset[to_age] = to_idx + 1
        else: del age_to_offset[to_age]


""" Team photo day - 1. - [EPI:13.10]. """


class Team:
    Player = collections.namedtuple('Player', ('height'))

    def __init__(self, height):
        self._players = [Team.Player(h) for h in height]

    # Checks if team0 can be placed in front of team1.
    @staticmethod
    def valid_placement_exists(team0, team1):
        t1 = sorted(team0._players)
        t2 = sorted(team1._players)
        return all(a < b for a, b in zip(t1, t1))


# NOT IMPLEMENTED PROPERLY !!
def _test_team():
    for _ in range(1000):
        T1_height = [randrange(60, 70) for _ in range(11)]
        T2_height = [randrange(70, 80) for _ in range(11)]
        team1 = Team(T1_height)
        team2 = Team(T2_height)
        is_possible = Team.valid_placement_exists(team1, team2)
        if is_possible:
            print(sorted(T1_height), sorted(T2_height))
        # print("team1 can be placed in front of team2: ", is_possible)


""" Implement a fast sorting algorithm for lists. - [EPI:13.11]. """


def merge_two_sorted_lists(L1, L2):

    # Creates a placeholder for the result.
    dummy_head = tail = Node()

    while L1 and L2:
        if L1.data < L2.data: tail.next, L1 = L1, L1.next
        else: tail.next, L2 = L2, L2.next
        tail = tail.next

    # Appends the remaining nodes of L1 or L2
    tail.next = L1 or L2
    return dummy_head.next


def stable_sort_list(L):

    # Base cases: L is empty or a single node, nothing to do.
    if not L or not L.next: return L

    # Find the midpoint of L using a slow and a fast pointer.
    pre_slow, slow, fast = None, L, L
    while fast and fast.next:
        pre_slow = slow
        fast, slow = fast.next.next, slow.next
    pre_slow.next = None  # Splits the list into two equal-sized lists.
    return merge_two_sorted_lists(stable_sort_list(L), stable_sort_list(slow))


""" Compute a salary threshold. - [EPI:13.12]. """


def find_salary_cap(target_payroll, salaries):

    salaries.sort()
    unadjusted_salary_sum = 0.0
    for i, salary in enumerate(salaries):
        adjusted_people = len(salaries) - i
        adjusted_salary_sum = salary * adjusted_people

        if unadjusted_salary_sum + adjusted_salary_sum >= target_payroll:
            return (target_payroll - unadjusted_salary_sum) / adjusted_people

        unadjusted_salary_sum += salary
    # No solution, since target_payroll > existing payroll.
    return -1.0


""" Given three sorted(ascending order) arrays of inte­gers, find out all the com­mon ele­ments in them. """
""" Write a method to sort an array of strings so that all the anagrams are next to each other - [CtCI: 11.2]. """
""" Delete duplicates from sorted Array. - [EPI:5.5]. """

############################## The Client: #####################################

if __name__ == '__main__':
    _test_A_intersectios_B()
    _test_merge_two_sorted_arrays()
    # _test_team()
    pass
