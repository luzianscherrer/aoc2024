import numpy as np
import skimage.measure

field = np.genfromtxt("day12input.txt", dtype=str, delimiter=1)
numfield = np.zeros(field.shape, dtype=int)
for char in np.unique(field):
    numfield[field == char] = ord(char)

labels = skimage.measure.label(numfield, connectivity=1)
areas = np.unique(labels)
labels = np.pad(labels, 1)
neighbors = np.array([[0, 1], [1, 0], [0, -1], [-1, 0]])

total = 0
for area in areas:
    count = 0
    coords = np.column_stack((labels == area).nonzero())
    for coord in coords:
        for neighbor in neighbors:
            count += labels[tuple(coord)] != labels[tuple(coord + neighbor)]
    total += count * np.sum(labels == area)

print(total)
