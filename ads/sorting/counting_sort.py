from typing import List

def counting_sort(a: List[chr]):

    RADIX = 256                      # Extended ASCII alphabet size


    def sort(a):
        N = len(a)
        count = [0]*(RADIX + 1)
        aux = [0]*N

        for i in range(N):           # computes frequency-count
            r = ord(a[i])
            count[r+1] += 1
        for i in range(RADIX):       # transform counts into indices
            count[i+1] += count[i]
        for i in range(N):           # distributes
            r = ord(a[i])
            aux[count[r]] = a[i]
            count[r] += 1
        for i in range(N):           # copy back
            a[i] = aux[i]
    sort(a)
