import collections
import operator


#==============================================================================
"""
We consider the problem of assigning tasks to workers. Each worker must be
assigned exactly two tasks. Each task takes a fixed amount of time. Tasks are
independent, i.e., there are no constraints ofthe form "Task 4 cannot start
before Task 3 is completed ." Any task can be assigned to any worker.We want
to assign tasks to workers so as to minimize how long it takes before all
tasks arecompleted. For example, if there are 6 tasks whose durations ate
5,2,1,6,4,4 hours, then anoptimum assignment is to give the first two tasks
(i.e., the tasks with duration 5 and 2) to oneworker, the next two (1 and 6)
to another worke1 and the last two tasks (4 and 4) to the last worker.For this
assignment, all tasks will finish after max(5 + 2,1 + 6,4 + 4) = 8 hours.
Design an algorithm that takes as input a set of tasks and retums an optimum
assignment.Hint: What additional task should be assigned to the worker who is
assigned the longest task?
"""
#==============================================================================

PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))


def optimum_task_assignment(task_durations):

    task_durations.sort()
    return [
        PairedTasks(task_durations[i], task_durations[~i])
        for i in range(len(task_durations) // 2)
    ]


#==============================================================================
"""
A database has to respond to a set of client SQL queries. The service time
required for each queryis known in advance. For this application, the queries
must be processed by the database one at atime, but can be done in any order.
The time a query waits before its tum comes is called its waitingtime.Given
service times for a setof queries, compute a schedule forprocessingthe queries
thatminimizesthe total waiting time. Retum the minimum waiting time.
For example, if the service times are<2,5,1.,3),if we schedule in the given
order,the total waiting timeis 0+(2)+(2+5)+(2+5 +1) =17.
If however, we schedule queries in order of decreasing service times, the total
 waiting time is0+(5)+(5+3)+(5+3+2)=23.As we will see,for this example,the
 minimum waiting time is l0.
 Hint: Focus on extreme values.
"""
#==============================================================================


def minimum_total_waiting_time(service_times):

    # Sort the service times in increasing order.
    service_times.sort()
    total_waiting_time = 0
    for i, service_time in enumerate(service_times):
        num_remaining_queries = len(service_times) - (i + 1)
        total_waiting_time += service_time * num_remaining_queries
    return total_waiting_time


#==============================================================================
"""
Consider a foreman responsible for a number of tasks on the factory floor. Each
task starts at a fixedtime and ends at a fixed time. The foreman wants to visit
the floor to check on the tasks. Your jobis to help him minimize the number of
visits he makes. In each visit, he can check on all the taskstaking place at
the time of the visit. A visit takes place at a fixed time, and he can only
check ontasks taking place at exactly that time. For example, if there are
tasks at times 10,3f,12,61,13,41,16,9),then visit times 0,2,3,6 cover all tasks.
A smaller set of visit times that also cover all tasks is 3,6. Inthe abstract,
you are to solve the following problem.You are given a set of closed intervals.
Design an efficient algorithm for finding a minimum sizedset of numbers that
covers all the intervals.Hint: Think about extremal points.
"""
#==============================================================================
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




#==============================================================================
"""
Design an algorithm that takes as input an array and a number, and determines
if there are three entries in the array (not necessarily distinct) which add up
to the specified number. For example, if the array is <11,2,5,7,3> then there are
three entries in the array which add up to 21 (3, 7, 11, and 5, 5, 11) (note that
 we can use 5 twice, since the problem statement said we c an use the same entry
  more than once). However, no three entries add up to 22.

Hint: How would you check if a given array entry can be added to two more entries
to get the specified number?
"""
#==============================================================================


def has_three_sum(A, v):
    for a in A:
        j = 0
        k = len(A) - 1
        while j < k:
            _v = a + A[j] + A[k]
            if _v < v:
                j += 1
            elif _v > v:
                k -= 1
            else:
                return True
    return False


#==============================================================================
"""
Several applications require identification of elements in a sequence which
occur more than aspecified fraction of the total number of elements in the
sequence. For example, we may wantto identify the users using excessive network
bandwidth or IP addresses originating the mostHypertext Transfer Protocol (HTTP)
 requests. Here we consider a simplified version of this problem.

You are reading a sequence of strings. You know a priori that more than half of
the strings are repetitions of a single string but the positions where the
majority element occurs are unknown. Write a program that makes a single pass
over the sequence and identifies the majority element. For example, if the input
is <b,a,c,a,a,b,a,a,c,a>, then a is the majority element (it appears in 6 out
of the 10 places).

Hint: Take advantage of the existence of a majority element to perform elimination.
"""
#==============================================================================
def majority_search(stream):

    candidate, candidate_count = None, 0
    for it in stream:
        if candidate_count == 0:
            candidate, candidate_count = it, candidate_count + 1
        elif candidate == it:
            candidate_count += 1
        else:
            candidate_count -= 1
    return candidate

#==============================================================================
"""
A number of cities are arranged on a circular road. You need to visit all the
cities and come back to the starting city. A certain amount of gas is available
at each city. The amount of gas summed up over all cities is equal to the amount
of gas required to go around the road once. Your gas tank has unlimited capacity.
Call a city ample if you can begin at that city with an empty tank, refill at it,
then travel through all the remaining cities, refilling at each, and return to
the ample city, without running out of gas at any point.

Given an instance of the gasup problem, how would you efficiently compute an
ample city, if one exists?

Hint: Think about starting with more than enough gas to complete the circuit
without gassing up. Track the amount of gas as you perform the circuit, gassing
up at each city.
"""
#==============================================================================

MPG = 20


# gallons[i] is the amount of gas in city i, and distances[i] is the
# distance city i to the next city.
def find_ample_city(gallons, distances):

    remaining_gallons = 0
    CityAndRemainingGas = collections.namedtuple('CityAndRemainingGas',
                                                 ('city', 'remaining_gallons'))
    city_remaining_gallons_pair = CityAndRemainingGas(0, 0)
    num_cities = len(gallons)
    for i in range(1, num_cities):
        remaining_gallons += gallons[i - 1] - distances[i - 1] // MPG
        if remaining_gallons < city_remaining_gallons_pair.remaining_gallons:
            city_remaining_gallons_pair = CityAndRemainingGas(
                i, remaining_gallons)
    return city_remaining_gallons_pair.city



#==============================================================================
"""
An array of integers naturally defines a set of lines parallel to the Y-axis,
starting from x = 0 asillustrated in Figure U.a@). The goal of this problem is
to find the pair of lines that together withthe X-axis "ttap" the most water.
See Figure 17.4b) for an example.

Write a Program which takes as input an integer array and retums the pair of
entries that trap themaximum amount of water.Hint: Slart with 0 and z - 1 and
work your way in.
"""
#==============================================================================


def get_max_trapped_water(heights):

    i, j, max_water = 0, len(heights) - 1, 0
    while i < j:
        width = j - i
        max_water = max(max_water, width * min(heights[i], heights[j]))
        if heights[i] > heights[j]:
            j -= 1
        else:  # heights[i] <= heights[j].
            i += 1
    return max_water

#==============================================================================
"""
You are given a sequence of adjacent buildings. Each has unit width and an
integer height. Thesebuildings form the skyline of a city. An architect wants
to know the area of a largest rectanglecontained in this skyline. See Figure
17.5 on the next page for an example.Let A be an array representing the heights
of adjacent buildings of unit width. Design an algorithmto compute the area of
the largest rectangle contained in this skyline.
Hint: How would you efficiently find the largest rectangle which includes the
i-th building, and has height A[i]?
"""
#==============================================================================


def calculate_largest_rectangle(heights):

    pillar_indices, max_rectangle_area = [], 0
    # By appending [0] to heights, we can uniformly handle the computation for
    # rectangle area here.
    for i, h in enumerate(heights + [0]):
        while pillar_indices and heights[pillar_indices[-1]] >= h:
            height = heights[pillar_indices.pop()]
            width = i if not pillar_indices else i - pillar_indices[-1] - 1
            max_rectangle_area = max(max_rectangle_area, height * width)
        pillar_indices.append(i)
    return max_rectangle_area


def minimum_total_waiting_time_pythonic(service_times):
    return sum(
        remaining_queries * time
        for remaining_queries, time in enumerate(sorted(service_times)[::-1]))
