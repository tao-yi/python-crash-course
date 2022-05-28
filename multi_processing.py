import multiprocessing
from typing import List


def fib(n: int):
    if n == 0 or n == 1:
        return n
    return fib(n-1)+fib(n-2)


def main():
    processes: List[multiprocessing.Process] = []
    for _ in range(5):
        p = multiprocessing.Process(target=fib, args=(40,))
        p.start()

    for p in processes:
        p.join()


if __name__ == "__main__":
    main()
