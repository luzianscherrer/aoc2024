import re
import numpy as np
from scipy import optimize

parts = np.zeros(2, dtype=int)
with open("day13input.txt") as file:
    for line in file:
        if "Button" in line:
            match = re.search(r"(.): X\+(\d+), Y\+(\d+)", line)
            if match.group(1) == "A":
                a = np.array([[match.group(2), 0], [match.group(3), 0]], dtype=int)
            else:
                a[:, 1] = [match.group(2), match.group(3)]
        elif "Prize" in line:
            match = re.search(r"X=(\d+), Y=(\d+)", line)
            b = np.array([match.group(1), match.group(2)], dtype=int)
            a = np.vstack((a, -a))
            for i in range(2):
                b += int(1e13) * i
                b2 = np.hstack((b, -b))
                ret = optimize.linprog(
                    np.array([-1, -1]), A_ub=a, b_ub=b2, integrality=[True, True]
                )
                if ret.success:
                    parts[i] += ret.x @ [3, 1]

print(f"{parts[0]} {parts[1]}")
