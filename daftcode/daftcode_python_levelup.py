import numpy as np
import sympy as sp


def generate_primes(n, start = 2):
    """
    Generates n prime numbers starting from min
    """
    prime_count = 0
    current_number = start
    primes = []
    while prime_count != n:
        if sp.isprime(current_number):
            primes.append(current_number)
            prime_count += 1
        current_number += 1
    return primes


def return_primes(n):
    primes = []
    for i in range(0, n):
        if sp.isprime(i):
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


def on_diagonals(N):
    numbers = []
    for R in range(1, N+1):
        base = (2*R - 1)*(2*R - 1)
        diff = 2*R - 2
        numbers.append(base)
        numbers.append(base - diff)
        numbers.append(base - 2*diff)
        numbers.append(base - 3*diff)
    return set(numbers)


def new_on_diagonals(N):
    len = 0
    for R in range(N, N+1):
        base = (2*R - 1)*(2*R - 1)
        diff = 2*R - 2
        if sp.isprime(base):
            len+=1
        if sp.isprime(base - diff):
            len+=1
        if sp.isprime(base - 2*diff):
            len+=1
        if sp.isprime(base - 3*diff):
            len+=1
    return len


def primes(list):
    ret = []
    for i in list:
        if sp.isprime(i):
            ret.append(i)
    return ret


def primes_on_diagonals(R):
    primes = []
    for i in on_diagonals(R):
        if sp.isprime(i):
            primes.append(i)
    return primes


print("12. Sum = " + str(sum(generate_primes(100))))

s = sum(on_diagonals(5))
print("13. Sum = " + str(s))

s = sum(primes_on_diagonals(10))
print("14. Sum = " + str(s))

full = len(on_diagonals(20))
diag = len(primes_on_diagonals(20))
p = int(round(diag/full * 100, 0))
print("15. Percentage = " + str(p))

R = 1

all_numbers = 0
prime_numbers = 0
perc = 100

while True:
    all_numbers += 4
    prime_numbers += new_on_diagonals(R)

    if prime_numbers != 0:
        perc = prime_numbers/all_numbers

    if R == 1:
        all_numbers -= 3
        R += 1
        continue

    if perc < 0.1:
        print("16. N = " + str(2*R-1))
        break
    R += 1
