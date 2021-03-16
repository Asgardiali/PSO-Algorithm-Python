import numpy as np
import random

"""
ssize: Swarm büyüklüğüdür. Yani toplam parçacık sayısıdır.
d: Problemin boyutudur. Yani bir parçacıktaki toplam parametre sayısıdır.

"""
altSinir = -10
ustSinir = 10
ssize = 1000
d = 3
w = 0.8
c1 = 2
c2 = 2
r1 = random.uniform(0, 1)
r2 = random.uniform(0, 1)

swarm = np.random.uniform(altSinir, ustSinir, [ssize, d])
obj = np.zeros([ssize, 1])

for x in range(0, ssize, 1):
    for y in range(0, d, 1):
        obj[x] += (swarm[x][y]) ** 2

velocity = np.zeros([ssize, d])
pbestpos = swarm
pbestvalue = obj
sbestvalue = np.amin(obj)
sbestpos = np.zeros([1, d])

for x in range(0, ssize, 1):
    if sbestvalue == obj[x, :]:
        idx = x
        sbestpos = swarm[x, :]

iterasyon = 1
while iterasyon <= 10000 and np.amin(obj) <= 0.00001:
    for x in range(0, ssize, 1):
        velocity[x, :] = (w * velocity[x, :]) + (c1 * r1 * (pbestpos[x, :] - swarm[x, :])) + (
                    c2 * r2 * (sbestpos - swarm[x, :]))

    vmax = (abs(altSinir) + abs(ustSinir)) / 2
    for x in range(0, ssize, 1):
        for y in range(0, d, 1):
            if velocity[x, y] > vmax:
                velocity[x, y] = vmax
            elif velocity[x, y] < -vmax:
                velocity[x, y] = vmax

    swarm = swarm + velocity

    for x in range(0, ssize, 1):
        for y in range(0, d):
            if swarm[x, y] > ustSinir:
                swarm[x, y] = ustSinir
            elif swarm[x, y] < altSinir:
                swarm[x, y] = altSinir

    for x in range(0, ssize, 1):
        for y in range(0, d, 1):
            obj[x] += (swarm[x][y]) ** 2

    for x in range(0, ssize, 1):
        if obj[x, :] < pbestvalue[x, :]:
            pbestvalue[x, :] = obj[x, :]
            pbestpos[x, :] = swarm[x, :]

    if np.amin(obj) < sbestvalue:
        sbestvalue = np.amin(obj)
        for x in range(0, ssize, 1):
            if sbestvalue == obj[x, :]:
                idx = x
                sbestpos = swarm[x, :]

    iterasyon = iterasyon + 1

print("Sürünün En iyi Değeri\n{}\n".format(sbestvalue))
print("Sürünün En İyi Parametreleri\n{}".format(sbestpos))
