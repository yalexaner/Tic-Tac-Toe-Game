import os # system("clear")
import random # randrange

'''
For input used next table:
 ____________________
|      |      |      |
|      |      |      |
|  0   |  1   |  2   |
|      |      |      |
|______|______|______|
|      |      |      |
|      |      |      |
|  3   |  4   |  5   |
|      |      |      |
|______|______|______|
|      |      |      |
|      |      |      |
|  6   |  7   |  8   |
|      |      |      |
|______|______|______|

And next symbols:
 ____	 ____
|    |  |	 |
|\  /|	| __ |
| \/ |	||	||
| /\ |	||  ||
|/  \|	||__||
|____|	|____|
'''

class UsedFieldError(Exception):
    pass

class gameOver(Exception):
    def __init__(self, char):
        global player_char
        global comp_char

        if char == player_char:
            self.message = "You won!"
        elif char == comp_char:
            self.message = "You lost :("
        else:
            self.message = "It's Draw"

# function for class 'Table' (draw)
def get_3items(lst):
	i = 0
	length = len(lst)

	while i < length:
		try:
			yield lst[i], lst[i + 1], lst[i + 2]
			i += 3
		except IndexError:
			return

class Table():
	def __init__(self):
		self.matrix = [str(i) for i in range(1, 10)]
		self.cross = [
			'      |',
			' \  / |',
			'  \/  |',
			'  /\  |',
			'_/__\_|'
		]
		self.zero = [
			'  __  |',
			' |  | |',
			' |  | |',
			' |__| |',
			'______|'
		]

	def add(self, char, field_num):
		if not 0 < field_num < 10:
			raise IndexError

		if self.matrix[field_num - 1] == 'O' or self.matrix[field_num - 1] == 'X':
			raise UsedFieldError

		self.matrix[field_num - 1] = char

	def draw(self):
		fields = []

		for i in range(9):
			if self.matrix[i] == 'X':
				fields.append(self.cross)
			elif self.matrix[i] == 'O':
				fields.append(self.zero)
			else:
				fields.append([
					'      |',
					'      |',
					'  {}   |'.format(i + 1),
					'      |',
					'______|'
				])

		# output
		print(' ____________________ ')

		for field1, field2, field3 in get_3items(fields):
			for i in range(5):
				print('|' + field1[i] + field2[i] + field3[i])

	def win(self):
		# if someone is winner
		if self.matrix[0] == self.matrix[1] == self.matrix[2]:
			raise gameOver(self.matrix[0])
		elif self.matrix[3] == self.matrix[4] == self.matrix[5]:
			raise gameOver(self.matrix[3])
		elif self.matrix[6] == self.matrix[7] == self.matrix[8]:
			raise gameOver(self.matrix[6])
		elif self.matrix[0] == self.matrix[3] == self.matrix[6]:
			raise gameOver(self.matrix[0])
		elif self.matrix[1] == self.matrix[4] == self.matrix[7]:
			raise gameOver(self.matrix[1])
		elif self.matrix[2] == self.matrix[5] == self.matrix[8]:
			raise gameOver(self.matrix[2])
		elif self.matrix[0] == self.matrix[4] == self.matrix[8]:
			raise gameOver(self.matrix[0])
		elif self.matrix[2] == self.matrix[4] == self.matrix[6]:
			raise gameOver(self.matrix[2])

		# if it's draw
		for raw in self.matrix:
			for field in raw:
				if field != 'O' and field != 'X':
					return
		raise gameOver("draw")

os.system("clear")

print("Hello in Tic Tac Toe Game!")
player_char = str(input("Enter character you want (X/O): ")).upper()

while player_char != 'O' and player_char != 'X':
    os.system("clear")

    print("Wrong symbol! You can use only 'X' or 'O'")
    player_char = str(input("Try again: "))

os.system("clear")

comp_char = 'X' if player_char == 'O' else 'O'

gameTable = Table()

while True:
	try:
		gameTable.draw()
		gameTable.add(player_char, int(input("Enter the number of the field: ")))

		os.system("clear")

		gameTable.draw()
		gameTable.win()

		# Logic
		while True:
			try:
				gameTable.add(comp_char, int(random.randrange(1, 10)))
			except UsedFieldError:
				continue
			else:
				break

		os.system("clear")

		gameTable.draw()
		gameTable.win()

		os.system("clear")
	except gameOver as g:
		print(g.message)
		break
	except UsedFieldError:
		os.system("clear")
		print("This field already used! Try another field", end='\n\n')
	except (IndexError, ValueError):
		os.system("clear")
		print("Wrong symbol! Try again.", end='\n\n')
