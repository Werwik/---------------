size = 3
board = list(range(1,10))

def draw_board():
    print("---------------")
    for i in range (size):
        print (f" | {board [0+i*3]} | {board [1+i*3]} | {board [2+i*3]} |") #индексы 0,1,2
    print("---------------")

def check_win():
	win = False

	win_combination = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))

	for i in win_combination:
		if (board[i[0]] == board[i[1]] and board[i[1]] == board[i[2]] and board[i[1]] in ('X','O')):
			win = board[i[0]]
	return win

def game_step(index, char):
	if (index > 10 or index < 1 or board[index-1] in ('X','O')):
		return False
	board[index-1] = char
	return True

def start_game():
	current_player = 'X'
	step = 1
	draw_board()
	while (step < 9) and (check_win() == False):
		index = input(f'Ход игрока  {current_player} . Введите номер поля что бы поставить {current_player} (0 - выход): ')
		if (int(index) == 0):
			break
		if (game_step(int(index), current_player)):
			print(f'Ход номер {step} сделан')
			if current_player == 'X':
				current_player = 'O'
			else:
				current_player = 'X'
			draw_board()
			step += 1
		else:
			print('Номер должен быть от 1 до 9')

	if (step == 9):
		print('Ничья')
	else:
		if current_player == 'X':
			print("Победа O")
		else:
			print("Победа Х")

print('Начало')
start_game()