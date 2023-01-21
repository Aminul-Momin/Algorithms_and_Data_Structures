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