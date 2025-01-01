# WAP to display prime numbers from 1 to 100

# Using Sieve of Eratosthenes algorithm for finding prime numbers (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
def prime(n):
    A = [True] * n
    n_sqrt = int(n ** 0.5)
    for i in range(2, n_sqrt):
        if A[i]:
            for j in range(i ** 2, n, i):
                A[j] = False
    return [i for i in range(2, n) if A[i]]


def main():
    print(prime(100))

if __name__ == '__main__':
    main()