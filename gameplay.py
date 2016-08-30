from __future__ import print_function
import signal,copy,sys,time
from random import randint
from block import *

class Gameplay(Block):
	
	def checkRowFull(self,rowno,sc):

    		for i in range(30):
        		if (sc[rowno][i]==0):
        		    return 1

    		for i in range(rowno-1,-1,-1):
        		for j in range(30):
        		    sc[i+1][j]=sc[i][j]

    		return 0


	def checkRowEmpty(self,rowno,sc):

    		for i in range(30):
        		if (sc[rowno][i]==1):
        			return 1
	def updateScore(self,x,score):
		score=score+x
		return score
	
	def selectPiece(self):
		pc= randint(1,200)%5
		return pc
		


	def printboard(self,sc,bl,score):
		print("Your Score is", score)
		print("Press 'q' to quit the game")
		for i in range(33):
			if (i==32):
				print("")
			else:
				print("#",end="")
		for i in range(32):
			print("#",end="")
			for j in range(30):
				if (sc[i][j]==0 and ([i,j] not in bl)) :
        	        		print(" ",end="")
				else:
					print("X",end='')
			print ("#",end='\n')
		for i in range(33):
			if (i==32):
				print("")
			else:
				print("#",end="")
		return

