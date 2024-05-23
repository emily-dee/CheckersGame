import checkers

if __name__ == '__main__':
    user_board_size = int(input("Welcome to Python Checkers, enter the size of the board you'd like to use. >> "))
    user_board = checkers.build_board(user_board_size)
    print()
    print(user_board)
    print()
    checkers.get_count(user_board, 'Empty')
    checkers.get_count(user_board, 'Red')
    checkers.get_count(user_board, 'Black')
    print()

    flipped_user_board = checkers.flip_flop(user_board)
    print("The board but with the x and y axes swapped:")
    print(flipped_user_board)
    print()

    change_size_yn = input("Would you like to change the size of the board? y or n >> ")
    if change_size_yn == 'y':
        new_board_size = int(input('Please enter the new size >> '))
        print()
        print(checkers.change_size(user_board, new_board_size))

    print()
    print('Thanks for playing checkers!')
