line = open("day09input.txt").read()

space, pos, input = False, 0, []
for digit in line:
    input += (["."] if space else [pos]) * int(digit)
    pos += not space
    space = not space

to = int(line[0])
frm = len(input) - 1
while to < frm:
    if input[frm] != ".":
        input[to] = input[frm]
        input[frm] = "."
        to += 1
        while input[to] != ".":
            to += 1
        frm -= 1
        while input[frm] == ".":
            frm -= 1

output = list(filter(lambda x: x != ".", input))
pos = list(range(len(output)))
print(sum([i[0] * i[1] for i in zip(output, pos)]))
