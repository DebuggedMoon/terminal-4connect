"""This module contains the game board class"""

from typing import List

class Board():
	"""
	A class to represent a game board.
	Allows modification to the board state.
	"""
 
	width: int
	heigth: int
	colums: List[List[str]]

	def __init__(self, width: int, heigth: int):
		self.width = width
		self.heigth = heigth
		self.columns = [["⬜"]*width]*heigth
