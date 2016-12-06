# permutations
from itertools import permutations
def nqueens(n):
    cols = range(n)
    res = []
    for p in permutations(cols):
        if (n == len(set(p[i]+i for i in cols))
              == len(set(p[i]-i for i in cols))):
            res.append(p)
    return res

# recursion
def rqueens(n, col=0, rows=[]):
    cols = range(len(rows))
    res = []
    if (len(rows) == len(set(rows[i]+i for i in cols))
          == len(set(rows[i]-i for i in cols))):
        if col == n:
            return [rows]
        for row in set(range(n)) - set(rows):
            res += rqueens(n, col+1, rows+[row])
    return res

# backtracking
def valid(row, rows):
    return row not in rows and all(abs(row - x) != len(rows) - i
        for i, x in enumerate(rows))

def bqueens(n):
    res = [[]]
    for col in range(n):
        res = [rows+[row] for rows in res
            for row in range(n)
            if valid(row, rows)]
    return res
