from API_keys import *
import enum

class state(enum.Enum):
	BUY = 1
	SELL = 2
	POSITIONS = 3

while True :
	print("what do you want to do?\n" "1. BUY\n" "2. SELL\n" "3. POSITIONS")
	state = input()

	if state == 1:
		print("BUY")

	elif state ==2:
		print("SELL")

	elif state ==3:
		print("POSITIONS")