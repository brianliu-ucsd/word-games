from flask_games import createTrie
from flask_games import trie

def solve(grid: list[list[str]]) -> dict[str: list[tuple[int, int]]]:
    words = []
    dictionary = createTrie.get_dictionary()
    BOARD_DIMENSION = 4
    for i in range(BOARD_DIMENSION):
        for j in range(BOARD_DIMENSION):
            traverse(grid, i, j, "", words, dictionary)
    return words

def neighbors(i: int, j: int) -> None:
    BOARD_DIMENSION = 4
    for row in range(-1, 2):
        for col in range(-1, 2):
            if row == col == 0:
                continue
            next_i = i + row
            next_j = j + col
            if 0 <= next_i < BOARD_DIMENSION and 0 <= next_j < BOARD_DIMENSION:
                yield (next_i, next_j)

def traverse(
    grid: list[list[str]],
    i: int,
    j: int,
    word: str,
    # order: list[tuple[int, int]],
    words: list[str],
    dictionary: trie.Trie,
):  
    char = grid[i][j]
    word += char
    if dictionary.starts(word):
        pass
    else:
        return
    if dictionary.contains(word) and len(word) >= 3:
        words.append(word)
    grid[i][j] = None
    for next_i, next_j in neighbors(i, j):
        if grid[next_i][next_j] is not None:
            traverse(grid, next_i, next_j, word, words, dictionary)
    grid[i][j] = char
