import concurrent.futures
import threading
import time
from typing import List

start = time.perf_counter()


def test(l: List[int], i: int):

    # print(f'Sleeping {seconds} second...')
    time.sleep(1)
    l[0] = i
    print(l)
    # return f'Done Sleeping {seconds} second...'


l = [1]

with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(test, l, 2)
    f2 = executor.submit(test, l, 3)
    print(f1.result(), f2.result())

finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} second(s)')
