import re
import numpy as np

result = 0
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
            ret = np.linalg.solve(a, b)
            if np.isclose(ret, np.round(ret)).all():
                result += ret @ [3, 1]
print(int(result))
