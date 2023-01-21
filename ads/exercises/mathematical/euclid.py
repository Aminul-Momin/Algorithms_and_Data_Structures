#-----------------------------------------------------------------------
# euclid.py
# Taken From: https://introcs.cs.princeton.edu/python/23recursion/euclid.py
#-----------------------------------------------------------------------

import sys
try:
    from ads.stdlib import sdtio
except (ImportError):
    from ece.ads.stdlib import stdio
except (ImportError):
    print('Please install ads (Algorithms and Data Structure)')

#-----------------------------------------------------------------------

# Return the greatest common divisor of p and q.


def gcd(p, q):
    if q == 0:
        return p
    return gcd(q, p % q)


#-----------------------------------------------------------------------

# Accept integers p and q as command-line arguments, compute the
# greatest common divisor of p and q, and write the result to
# standard output.


def main():
    p = int(sys.argv[1])
    q = int(sys.argv[2])
    divisor = gcd(p, q)
    stdio.writeln(divisor)


if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python euclid.py 1440 408
# 24

# python euclid.py 314159 271828
# 1