import re

rules, result1, result2 = [], [], []
with open("day05input.txt") as file:
    for line in file:
        data = line.rstrip()
        if "|" in data:
            rules.append(data.split("|"))
        elif "," in data:
            valid = True
            for rule in rules:
                if re.search(r"" + rule[1] + ".+" + rule[0], data):
                    valid = False
                    break
            if valid:
                res = data.split(",")
                result1.append(int(res[len(res) // 2]))
            else:
                while True:
                    valid = True
                    for rule in rules:
                        match = re.search(
                            r"(" + rule[1] + r").+(" + rule[0] + r")", data
                        )
                        if match:
                            valid = False
                            arr = data.split(",")
                            tmp = arr[match.span(1)[0] // 3]
                            arr[match.span(1)[0] // 3] = arr[match.span(2)[0] // 3]
                            arr[match.span(2)[0] // 3] = tmp
                            data = ",".join(arr)
                    if valid:
                        break
                res = data.split(",")
                result2.append(int(res[len(res) // 2]))
print(sum(result1), sum(result2))
