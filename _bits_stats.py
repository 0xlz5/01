#!/usr/bin/env python3

from functools import reduce
from more_itertools import flatten
import numpy as np
import os

class App:
    __instances = []

    def __init__(self):
        App.setUp(self)

    @classmethod
    def setUp(cls, obj):
        cls.__instances.append(obj)

    @classmethod
    def howMany(cls):
        return len(cls.__instances)
        
    @classmethod
    def executeOverInstances(cls):
        r = []
        for obj in cls.__instances:
            r.append((obj, obj.doSomething()))
        return r

    def doSomething(self, n = 10):
        d0 = 0
        d1 = 0
        l = lambda x: [int(n) for n in bin(x)[2:].zfill(8)]
        for x in os.urandom(10):
            for b in l(x):
                match b:
                    case 0: d0 = d0 + 1
                    case 1: d1 = d1 + 1
        return (d0, d1)

    def doSomethingGreat(self, x = 100):
        return reduce(lambda a, b: a+b, flatten([np.random.rand(1, 4) for i in range(x)]))

if __name__ == '__main__':
    a1 = App()
    a2 = App()
    a3 = App()
    a4 = App()
    for obj, r in App.executeOverInstances():
        print(obj.doSomethingGreat())
        print(r)
