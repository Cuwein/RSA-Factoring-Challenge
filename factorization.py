#/usr/bin/env python3
import sys

def factorize(n):
    factors = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            factors.append((i, n // i))
    return factors

def main(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            number = int(line.strip())
            factorizations = factorize(number)
            for factorization in factorizations:
                print(f"{number}={factorization[0]}*{factorization[1]}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file>")
        sys.exit(1)
    file_path = sys.argv[1]
    main(file_path)

