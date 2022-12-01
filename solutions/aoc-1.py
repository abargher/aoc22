max_cals = 0

data_list = []
elf_lst = []
with open("../input/aoc-1-input.txt", "r") as f:
    curr_run = 0
    for line in f:
        if len(line) > 1:
            curr_run += int(line.strip())
        else:
            elf_lst.append(curr_run)
            curr_run = 0

elf1 = 0
max_ind = 0
print(elf_lst)

total = 0
for j in range(3):
    for i, elf in enumerate(elf_lst):
        if elf > elf1:
            elf1 = elf
            max_ind = i
    print(elf1)
    total += elf1
    elf_lst.remove(elf1)
    elf1 = 0
    max_ind = 0

print("total")
print(total)