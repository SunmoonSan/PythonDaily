#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-06-19 15:35
# @site  : https://github.com/SunmoonSan
from random import randint
from time import sleep
from myThread import MyThread
from queue import Queue


def writeQ(queue):
    print('producing object for Q...')
    queue.put('xxx', 1)
    print('size now', queue.qsize())


def readQ(queue):
    val = queue.get(1)
    print('consumed object from Q...size now', queue.qsize())


def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1, 3))


def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(2, 5))


funcs = [writer, reader]
nfuncs = range(len(funcs))


def _main():
    nloops = randint(2, 5)
    q = Queue(32)

    threads = []
    for i in nfuncs:
        t = MyThread(func=funcs[i], args=(q, nloops), name=funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

    print('all DONE')


if __name__ == '__main__':
    _main()








