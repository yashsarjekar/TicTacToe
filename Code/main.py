from Modules.game import Game

number_player = int(input("Enter how many player will play the game: "))
size_board = int(input("Enter size of board: "))

game_obj = Game(size_board)
game_obj.initialize_game(size_board, number_player)
game_obj.start_game()