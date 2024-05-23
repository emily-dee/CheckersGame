from numpy import random, ndarray, swapaxes, resize


def build_board(size: int) -> ndarray:
    board = random.choice(['Empty', 'Red', 'Black'], (size, size))
    return board


def get_count(counted_board: ndarray, tile_status: str):
    if tile_status == 'Black':
        black_tiles = counted_board == 'Black'
        print(f"There are {black_tiles.sum()} black tiles.")
    if tile_status == 'Red':
        red_tiles = counted_board == 'Red'
        print(f"There are {red_tiles.sum()} red tiles.")
    if tile_status == 'Empty':
        empty_tiles = counted_board == 'Empty'
        print(f"There are {empty_tiles.sum()} empty tiles.")


if __name__ == '__main__':
    print("ERROR: this file is not intended to run as main.")


def flip_flop(pre_flipped_board: ndarray) -> ndarray:
    post_flipped_board = swapaxes(pre_flipped_board, 0, 1)
    return post_flipped_board


def change_size(pre_sized_board: ndarray, new_board_size: int) -> ndarray:
    post_sized_board = resize(pre_sized_board, (new_board_size, new_board_size))
    return post_sized_board
