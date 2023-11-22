from library.input import read


def score(opponent_move, player_move):
    #### R, P, S
    scores = [
        [4, 8, 3],  # rock: 1
        [1, 5, 9],  # paper: 2
        [7, 2, 6],  # scissors: 3
    ]
    return scores[ord(opponent_move) - ord("A")][ord(player_move) - ord("X")]


def solve(lines, score_func):
    return sum(
        score_func(opponent_move, player_move)
        for line in lines
        if line != ""
        for opponent_move, player_move in [line.split(" ")]
    )


def score_2(opponent_shape, want_result):
    #### L0,D3,W6
    scores = [
        [3, 4, 8],  # rock: 1
        [1, 5, 9],  # paper: 2
        [2, 6, 7],  # scissors: 3
    ]
    return scores[ord(opponent_shape) - ord("A")][ord(want_result) - ord("X")]


if __name__ == "__main__":
    data = read()
    print(solve(data, score))
    print(solve(data, score_2))
