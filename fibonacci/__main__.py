import sys

from fibonacci.fibonacci import fib

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(f"{fib(n)}")
