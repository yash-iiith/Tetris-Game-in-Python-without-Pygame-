from __future__ import print_function
import signal,copy,sys,time
from random import randint
from board import *

class Block(Board):

	def rotate(self,sc,bl):
		rs=[]
		cs=[]
		for i in bl:
			rs.append(i[0])
			cs.append(i[1])
		mnr=40
		mnc=40
		mxr=0
		mxc=0
		for i in rs:
			mnr= i if i<mnr else mnr
			mxr= i if mxr<i else mxr
		for i in cs:
			mnc= i if mnc>i else mnc
			mxc= i if mxc<i else mxc
		tmp = [[0 for x in range(mxc-mnc +1)] for y in range(mxr-mnr+1)]
		for i in bl:
			xc=i[0]-mnr
			yc=i[1]-mnc
			tmp[xc][yc]=1
		nbl=zip(*tmp[::-1])
		ch=0
		for i in range(mxr-mnr+1):
			for j in range(mxc - mnc +1):
				if(nbl[j][i]==1):
					ch= ch + self.checkPiecePos(mnr+j,mnc+i,sc)
	
		ret=[]			

		if (ch!=0):
			return ret
	
		for i in range(mxr-mnr+1):
			for j in range(mxc - mnc +1):
				if(nbl[j][i]==1):
					ret.append([mnr+j,mnc+i])
	
		return ret
		
	def moveRight(self,sc,bl):

   		ch = 0

   		for p in bl:
        		ch = ch + self.checkPiecePos(p[0],p[1]+1,sc)

    		if (ch==0):
        		for p in bl:
        	    		p[1]=p[1]+1

    		return 0

	def Down(self,sc,bl):

	    	ch = 0
	
	    	for p in bl:
 		       	ch = ch + self.checkPiecePos(p[0]+1,p[1],sc)

    		if (ch!=0):
        		for p in bl:
        	 	   sc[p[0]][p[1]]=1
       			return 1

    		for p in bl:
        		p[0]=p[0]+1

    		return 0
	def moveLeft(self,sc,bl):
  		ch = 0
    		for p in bl:
        		ch = ch + self.checkPiecePos(p[0],p[1]-1,sc)

    		if (ch==0):
        		for p in bl:
	            		p[1]=p[1]-1

    		return 0

	def draw(self,sc,bl):

    		while(1):
        		a = self.Down(sc,bl)
        		if (a==1):
            			return 1


