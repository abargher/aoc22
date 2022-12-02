scores = []
move_map = {"A" : 1,
            "B" : 2,
            "C" : 3,
            "X" : 0,
            "Y" : 3,
            "Z" : 6}

lose_map = {1 : 3, 2 : 1, 3 : 2}
win_map = {1 : 2, 2 : 3, 3 : 1}

def find_move(opp, res):
    if res == 3:
        return opp
    elif res == 0:
        return lose_map[opp]
    else:
        return win_map[opp]


def calc_res(m1, m2):
    if m1 == m2:
        return 3
    if (m1 == 1 and m2 == 3 or
        m1 == 2 and m2 == 1 or
        m1 == 3 and m2 == 2):
        return 0
    else:
        return 6

total_score = 0
with open("../input/aoc-2-input.txt", "r") as f:
    for opp, res in [[mv for mv in line.split()] for line in f]:
        print(opp, "space", res)

        score = move_map[res] + find_move(move_map[opp], move_map[res])
        print(score)
        total_score += score

print(total_score)

        


