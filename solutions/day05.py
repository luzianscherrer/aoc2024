import re

rules, result = [], []
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
                result.append(int(res[len(res) // 2]))
print(sum(result))
