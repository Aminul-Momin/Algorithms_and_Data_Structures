"""
Consider a collection of electrical pins on a printed circuit board (PCB). For each pair of pins, theremay or may not be a wire joining them. This is shown in Figure 18.8, where vertices correspondto pins, and edges indicate the presence of a wire between pins. (The significance of the colors isexplained later.)

Design an algorithm that takes a set of pins and a set of wires connecting pairs of pins, anddetermines if it is possible to place some pins on the left half of a PCB, and the remainder on theright half, such that each wire is between left and right halves. Retum such a division, if one exists.For example, the light vertices and dark vertices in Figure 18.8 are such division.Hint: Model as a graph and think about the implication of an odd length cycle.
"""