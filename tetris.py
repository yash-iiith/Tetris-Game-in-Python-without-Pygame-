from __future__ import print_function
import signal,copy,sys,time
from random import randint
from gameplay import *
from block import *
from board import *
from alarmexception import *
from getchunix import *

getch = GetchUnix()

def alarmHandler(signum, frame):
    raise AlarmException

def input_to(timeout=1):
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        text = getch()
        signal.alarm(0)
        return text
    except AlarmException:
        print("\n Prompt timeout. Continuing...")
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''

sc = [[0 for x in range(30)] for y in range(32)]
score=0
blcs = [ [[0,0],[0,1],[0,2],[0,3]] , [[0,0],[0,1],[1,1],[1,2]] , [[0,0],[0,1],[1,0],[1,1]] , [[0,1],[0,2],[1,0],[1,1]] , [[0,1],[1,0],[1,1],[1,2]] ]
f=0
g = Gameplay()
bo= Board()
block=Block()

while (1):
	if(f==0):
		f=1
	else:
		score=g.updateScore(10,score)
		
	bno=g.selectPiece()
	bl=[]
	bl=copy.deepcopy(blcs[bno])
	dropos=randint(2,24)
	for p in bl:
       		p[1]+=dropos

	st = 0
    	while(st == 0):
        	c = input_to()
		if (c=='q'):
			print("your score is", score)
			print("END")
			sys.exit(0)
        	elif(c==' '):	
        	    st = st + block.draw(sc,bl)

        	elif(c=='d'):
            		block.moveRight(sc,bl)

		elif(c=='a'):
            		block.moveLeft(sc,bl)

		elif(c=='s'):
			newc=block.rotate(sc,bl)
			if(len(newc)!=0):	
				bl=[]
				bl=copy.deepcopy(newc)

        	st= st + block.Down(sc,bl)
        	g.printboard(sc,bl,score)
        	if (g.checkRowEmpty(0,sc)==1):
			print("your score is", score)
            		print("END")
            		sys.exit(0)
     	 	for p in bl:
            		if(g.checkRowFull(p[0],sc)==0):
				score=g.updateScore(100,score)
