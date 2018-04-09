from AlphaBeta import *
from BoardLogic import *
from heuristics import *
import time

alpha = float('-inf')
beta = float('inf')
depth = 3
ai_depth = 4
ai2_depth = 5

def boardOutput(board): 

		print(board[0]+"---------------------------"+board[1]+"---------------------------"+board[2]+"    ");
		print("|                           |                           |");
		print("|       "+board[3]+"-------------------"+board[4]+"--------------------"+board[5]+"      |");
		print("|       |                   |                    |      |");
		print("|       |                   |                    |      |");
		print("|       |         "+board[6]+"---------"+board[7]+"---------"+board[8]+"          |      |");
		print("|       |         |                   |          |      |");
		print("|       |         |                   |          |      |");
		print(board[9]+"-------"+board[10]+"---------"+board[11]+"                   "+board[12]+"----------"+board[13]+"------"+board[14]+"    ");
		print("|       |         |                   |          |      |");
		print("|       |         |                   |          |      |");
		print("|       |         "+board[15]+"---------"+board[16]+"---------"+board[17]+"          |      |");
		print("|       |                   |                    |      |");
		print("|       |                   |                    |      |");
		print("|       "+board[18]+"-------------------"+board[19]+"--------------------"+board[20]+"      |");
		print("|                           |                           |");
		print("|                           |                           |");
		print(board[21]+"---------------------------"+board[22]+"---------------------------"+board[23]+"");



def AI_VS_AI(window, heuristic1, heuristic2):

	board = []
	for i in range(24):
		board.append("X")

	evaluation = evaluator()

	doNotEnterStage2 = False
	print("Stage 1")
	for i in range(9):
	
		boardOutput(board)
		evalBoard = alphaBetaPruning(board, ai_depth, True, alpha, beta, True, heuristic1)

		if evalBoard.evaluator == float('inf'):
			print("AI Bot 1 has won!")
			doNotEnterStage2 = True
			break
		else:
			board = evalBoard.board

		boardOutput(board)
		evalBoard = alphaBetaPruning(board, ai2_depth, False, alpha, beta, True, heuristic2)

		if evalBoard.evaluator == float('-inf'):
			print("AI Bot 2 has won!")
			doNotEnterStage2 = True
			break
		else:
			board = evalBoard.board


	if doNotEnterStage2:
		return None

	print("Stage 2")
	while True:

		boardOutput(board)
		evalBoard = alphaBetaPruning(board, ai_depth, True, alpha, beta, False, heuristic1)

		if evalBoard.evaluator == float('inf'):
			print("AI Bot 1 has won!")
			break
		else:
			board = evalBoard.board

		boardOutput(board)
		evaluation = alphaBetaPruning(board, ai2_depth, False, alpha, beta, False, heuristic2)

		if evaluation.evaluator == float('-inf'):
			print("AI Bot 2 has won")
			break
		else:
			board = evaluation.board


if __name__ == "__main__":

	print("Welcome to Nine Mens Morris")
	print("==========================")
	gametype = input("Please enter '1' to start")

	while gametype != 1:
		gametype = input("Enter '1' to start! ")

	if gametype == 1:
		ai_depth = int(input("Enter first AI level: "))
		ai2_depth= int(input("Enter second AI level: "))
		AI_VS_AI(None, potentialMillsHeuristic, numberOfPiecesHeuristic)

