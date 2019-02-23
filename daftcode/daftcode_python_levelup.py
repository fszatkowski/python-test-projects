import numpy as np


def is_prime(x):
    if x < 2:
        return False
    return all(x % i for i in range(2, x))


def generate_primes(n, start = 2):
    """
    Generates n prime numbers starting from min
    """
    prime_count = 0
    current_number = start
    primes = []
    while prime_count != n:
        if is_prime(current_number):
            primes.append(current_number)
            prime_count += 1
        current_number += 1
    return primes


def return_primes(n):
    primes = []
    for i in range(0, n):
        if is_prime(i):
            primes.append(i)
    return primes


def ulam(R):
    mat = np.ones((2*R-1, 2*R-1), dtype=int)

    for N in range(0, R):
        corner_idx = 2*N+1
        steps = 2*N + 1

        """
        Fills matrix with numbers starting from corners and descending in square pattern
        """

        mat[R+N-1][R+N-1] = corner_idx*corner_idx

        for step in range(1, steps):
            mat[R+N-1][R+N-1-step] = mat[R+N-1][R+N-step] - 1
        for step in range(1, steps):
            mat[R+N-1-step][R-N-1] = mat[R+N-step][R-N-1] - 1
        for step in range(1, steps):
            mat[R-N-1][R-N+step-1] = mat[R-N-1][R-N+step-2] - 1
        for step in range(1, steps-1):
            mat[R-N+step-1][R+N-1] = mat[R-N+step-2][R+N-1] - 1

    return mat


def on_diagonals(mat):
    N = mat.shape[0]
    numbers = set()
    for i in range(0, N):
        numbers.add(mat[i][i])
        numbers.add(mat[N-i-1][i])
    return numbers


def primes_on_diagonals(mat):
    primes = []
    for i in on_diagonals(mat):
        if is_prime(i):
            primes.append(i)
    return primes


print("12. Sum = " + str(sum(generate_primes(100))))

s = sum(on_diagonals(ulam(5)))
print("13. Sum = " + str(s))

s = sum(primes_on_diagonals(ulam(10)))
print("14. Sum = " + str(s))

full = len(return_primes(39*39))
diag = len(primes_on_diagonals(ulam(20)))
p = int(round(diag/full * 100, 0))
print("15. Percentage = " + str(p))

R = 2
while True:
    n = 2*R-1
    n = n*n

    full = len(return_primes(n))
    diag = len(primes_on_diagonals(ulam(R)))

    perc = diag/full * 100
    perc = int(perc)

    if perc < 10:
        print("16. N = " + str(2*R-1))
        break
    R += 1
