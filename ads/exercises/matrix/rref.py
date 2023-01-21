from numpy import *

# Reduce Rechelon Form


def rref(mat, precision=0, GJ=False):
    m, n = mat.shape
    p, t = precision, 1e-1**precision
    A = around(mat.astype(float).copy(), decimals=p)
    if GJ:
        A = hstack((A, identity(n)))
    pcol = -1  #pivot colum
    for i in xrange(m):
        pcol += 1
        if pcol >= n: break
        #pivot index
        pid = argmax(abs(A[i:, pcol]))
        #Row exchange
        A[i, :], A[pid + i, :] = A[pid + i, :].copy(), A[i, :].copy()
        #pivot with given precision
        while pcol < n and abs(A[i, pcol]) < t:
            #pivot index
            pid = argmax(abs(A[i:, pcol]))
            #Row exchange
            A[i, :], A[pid + i, :] = A[pid + i, :].copy(), A[i, :].copy()
            pcol += 1
        if pcol >= n: break
        pivot = float(A[i, pcol])
        for j in xrange(m):
            if j == i: continue
            mul = float(A[j, pcol]) / pivot
            A[j, :] = around(A[j, :] - A[i, :] * mul, decimals=p)
        A[i, :] /= pivot
        A[i, :] = around(A[i, :], decimals=p)

    if GJ:
        return A[:, :n].copy(), A[:, n:].copy()
    else:
        return A


def rref(matrix):
    A = np.array(matrix, dtype=np.float64)

    i = 0  # row
    j = 0  # column
    while True:
        # find next nonzero column
        while all(A.T[j] == 0.0):
            j += 1
            # if reached the end, break
            if j == len(A[0]) - 1: break
        # if a_ij == 0 find first row i_>=i with a
        # nonzero entry in column j and swap rows i and i_
        if A[i][j] == 0:
            i_ = i
            while A[i_][j] == 0:
                i_ += 1
                # if reached the end, break
                if i_ == len(A) - 1: break
            A[[i, i_]] = A[[i_, i]]
        # divide ith row a_ij to make it a_ij == 1
        A[i] = A[i] / A[i][j]
        # eliminate all other entries in the jth column by subtracting
        # multiples of of the ith row from the others
        for i_ in range(len(A)):
            if i_ != i:
                A[i_] = A[i_] - A[i] * A[i_][j] / A[i][j]
        # if reached the end, break
        if (i == len(A) - 1) or (j == len(A[0]) - 1): break
        # otherwise, we continue
        i += 1
        j += 1

    return A


def rref(A, tol=1.0e-12):
    m, n = A.shape
    i, j = 0, 0
    jb = []

    while i < m and j < n:
        # Find value and index of largest element in the remainder of column j
        k = np.argmax(np.abs(A[i:m, j])) + i
        p = np.abs(A[k, j])
        if p <= tol:
            # The column is negligible, zero it out
            A[i:m, j] = 0.0
            j += 1
        else:
            # Remember the column index
            jb.append(j)
            if i != k:
                # Swap the i-th and k-th rows
                A[[i, k], j:n] = A[[k, i], j:n]
            # Divide the pivot row i by the pivot element A[i, j]
            A[i, j:n] = A[i, j:n] / A[i, j]
            # Subtract multiples of the pivot row from all the other rows
            for k in range(m):
                if k != i:
                    A[k, j:n] -= A[k, j] * A[i, j:n]
            i += 1
            j += 1
    # Finished
    return A, jb