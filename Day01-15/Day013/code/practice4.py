"""

@Author:jyang
@Date:5/20/2019
"""

from multiprocessing import Process, Queue
from random import randint
from time import time


def sum_handler(cur_list, result_queue):
    sum = 0
    for _ in cur_list:
        sum += _
    result_queue.put(sum)


def main():
    processes = []
    num_list = [x for x in range(1, 100000001)]
    result_queue = Queue()
    index = 0
    for _ in range(8):
        p = Process(target=sum_handler, args=(num_list[index:index+12500000], result_queue))
        index += 12500000
        processes.append(p)
        p.start()

    start = time()
    for p in processes:
        p.join()

    # 合并所有线程的结果
    sum = 0
    while not result_queue.empty():
        sum += result_queue.get()
    print(sum)
    end = time()
    print('Execution time: ', (end - start), 's', sep='')


if __name__ == '__main__':
    main()