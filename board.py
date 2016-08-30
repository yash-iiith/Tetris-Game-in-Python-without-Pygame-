from __future__ import print_function
import signal,copy,sys,time
from random import randint

class Board:

	def checkPiecePos(self,x,y,sc):

    		if(x>31 or x<0 or y<0 or y>29):
        		return 1
    		return sc[x][y]

