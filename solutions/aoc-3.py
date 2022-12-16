print(ord('a'))
# minus 96

def char_to_priority(let):
    prio = ord(let)
    if prio in range(65, 65 + 27):
        prio -= 38
    elif prio in range(97, 97 + 27):
        prio -= 96
    return prio

with open("../input/aoc-3-input.txt", "r") as f:
    sacks = f.readlines()
    priorities = []
    for sack in sacks:
        line_to_add = []
        for let in sack:
            print(let, char_to_priority(let))
            line_to_add.append(char_to_priority(let))
        priorities.append(line_to_add)
    print(sacks[0])
    print(priorities[0])
