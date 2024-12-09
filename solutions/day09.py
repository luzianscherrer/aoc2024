line = open("day09input.txt").read()


def chksum(arr):
    output = [0 if i == "." else i for i in arr]
    pos = list(range(len(output)))
    return sum([i[0] * i[1] for i in zip(output, pos)])


space, pos, input1 = False, 0, []
for digit in line:
    input1 += (["."] if space else [pos]) * int(digit)
    pos += not space
    space = not space
input2 = input1.copy()

# part 1
to = int(line[0])
frm = len(input1) - 1
while to < frm:
    if input1[frm] != ".":
        input1[to] = input1[frm]
        input1[frm] = "."
        to += 1
        while input1[to] != ".":
            to += 1
        frm -= 1
        while input1[frm] == ".":
            frm -= 1
print(chksum(input1))

# part 2
frm_s = len(input2) - 1
while frm_s > int(line[0]):
    if input2[frm_s] == ".":
        frm_s -= 1
        continue
    frm_e = frm_s
    while input2[frm_s] == input2[frm_e]:
        frm_s -= 1
    frm_s += 1
    to_s = int(line[0])
    while to_s < frm_s:
        if input2[to_s] != ".":
            to_s += 1
            continue
        to_e = to_s
        while input2[to_e] == input2[to_s]:
            to_e += 1
        to_e -= 1
        if to_e - to_s >= frm_e - frm_s:
            input2[to_s : to_s + (frm_e - frm_s) + 1] = input2[frm_s : frm_e + 1]
            input2[frm_s : frm_e + 1] = ["."] * (frm_e - frm_s + 1)
            break
        to_s = to_e + 1
    frm_s -= 1
print(chksum(input2))
