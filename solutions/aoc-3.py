print(ord('a'))
# minus 96

with open("../input/aoc-3-input.txt", "r") as f:
    sacks = f.readlines()
    priorities = []
    for sack in sacks:
        line_to_add = []
        for let in sack:
            line_to_add.append(ord(let) - 96)
        priorities.append(line_to_add)
    print(priorities[0])
