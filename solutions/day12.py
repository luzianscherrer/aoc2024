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

total1, total2 = 0, 0
for area in areas:
    strides = 0
    fences = 0
    for i in range(4):
        coords = np.column_stack((labels == area).nonzero())
        if i == 0:
            for coord in coords:
                for neighbor in neighbors:
                    fences += labels[tuple(coord)] != labels[tuple(coord + neighbor)]
            total1 += fences * np.sum(labels == area)

        for coord in coords:
            strides += labels[tuple(coord)] != labels[tuple(coord + [0, 1])] and (
                labels[tuple(coord + [-1, 0])] != labels[tuple(coord)]
                or (
                    labels[tuple(coord + [-1, 0])] == labels[tuple(coord)]
                    and labels[tuple(coord + [-1, 1])] == labels[tuple(coord)]
                )
            )
        labels = np.rot90(labels)
    total2 += strides * np.sum(labels == area)

print(total1, total2)
