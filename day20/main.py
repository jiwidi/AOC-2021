import numpy as np
from itertools import product
from functools import lru_cache


DICE_ROLLS = list(range(1, 101)) * 200


def part_one(player_one, player_two, score_one, score_two):
    global DICE_ROLLS
    dice_counter = 0
    while score_one < 1000 and score_two < 1000:
        # Play one turn
        player_one_roll = DICE_ROLLS[dice_counter : dice_counter + 3]
        player_one = (player_one + sum(player_one_roll)) % 10
        player_one = player_one if player_one != 0 else 10
        score_one += player_one
        # print(
        #     f"Player 1 rolls {player_one_roll} and moves to space {player_one} for a total score of {score_one}."
        # )
        dice_counter += 3

        if score_one >= 1000:
            break
        # Player two turn
        player_two_roll = DICE_ROLLS[dice_counter : dice_counter + 3]
        player_two = (player_two + sum(player_two_roll)) % 10
        player_two = player_two if player_two != 0 else 10
        score_two += player_two
        # print(
        #     f"Player 2 rolls {player_two_roll} and moves to space {player_two} for a total score of {score_two}."
        # )
        dice_counter += 3
    return min([score_two, score_one]) * dice_counter


# Part 2
@lru_cache(maxsize=None)
def part_two(p1, s1, p2, s2):
    w1, w2 = 0, 0
    p1_initial = p1
    s1_initial = s1
    for s in [i + j + k for i in (1, 2, 3) for j in (1, 2, 3) for k in (1, 2, 3)]:
        p1 = (p1_initial + s - 1) % 10 + 1
        s1 = s1_initial + p1
        if s1 >= 21:
            w1 += 1
        else:
            r2, r1 = part_two(p2, s2, p1, s1)
            w1, w2 = w1 + r1, w2 + r2
    return w1, w2


#####


def main():
    part1 = part_one(7, 5, 0, 0)
    part2 = max(part_two(7, 0, 5, 0))
    print("Solutions:", part1, part2)


if __name__ == "__main__":
    main()
