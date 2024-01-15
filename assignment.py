from __future__ import print_function

import time
from sr.robot import *

a_th = 2.0
""" float: Threshold for the control of the linear distance"""

d_th = 0.4
""" float: Threshold for the control of the orientation"""

R = Robot()
#R.location(300)

dist_silver_area=3.0
rot_y_silver_area=2


dist_golden_area=5.0
rot_y_silver_area=2


def drive(speed, seconds):
    """
    Function for setting a linear velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0
    
    

def turn(speed, seconds):
    """
    Function for setting an angular velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0
    
def cicle(speed,seconds):
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = 2*speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0



def find_golden_token():
    """
    Function to find the closest golden token

    Returns:
	dist (float): distance of the closest golden token (-1 if no golden token is detected)
	rot_y (float): angle between the robot and the golden token (-1 if no golden token is detected)
	codeToken (float): code of the token
    """
    dist=100
    print(len(R.see()))
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD:
            dist=token.dist
	    rot_y=token.rot_y
	    codeToken=token.info.code
	    print(token.dist)
    if dist==100:
	return -1, -1,-1
    else:
   	return dist, rot_y, codeToken


def find_silver_token():
    """
    Function to find the closest golden token

    Returns:
	dist (float): distance of the closest golden token (-1 if no golden token is detected)
	rot_y (float): angle between the robot and the golden token (-1 if no golden token is detected)
	codeToken (float): code of the token
    """
    dist=100
    print(len(R.see()))
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD:
            dist=token.dist
	    rot_y=token.rot_y
	    codeToken=token.info.code
	    print(token.dist)
    if dist==100:
	return -1, -1,-1
    else:
   	return dist, rot_y, codeToken



def init():
	'''
	init phase:
	-the robot go in the center (more or less) 
	-turn around itself and see the available tokens
	-create a list of tokens that has around itself
	
	Returns:
	tokenToApproach (list): list of tokens of boxes that must be moved near the gray area
	tokenToAglinTogether (list): list of tokens of boxes that must be aligned together
	'''
	drive(60,5)

	#inizialize the list of token 
	tokens=[]
	#this for is used to turn around itself and see the available tokens
	for i in range(0,12):
		print(R.see(),'\n')
		turn(-10,1)
		silver_tokens.append(find_silver_tokens)
		golden_tokens.append(find_silver_tokens)
		

	#print('tokens')
	print((tokens))

	
	return silver_tokens, golden_tokens




def alignSilver(silver_tokens):
	
	#this while is used to bring the golden boxes closer to the gray area
	while not len(silver_tokens)==0: #stop the while when there are no tokens anymore 
	    
	    dist, rot_y, codeToken = find_silver_token()
	    if dist==-1: # if no token is detected, we make the robot turn 
		print("I don't see any token!!")
		turn(-10, 1) #turn a little bit on left
	    elif dist <d_th: # if we are close to the token, we try grab it.
		print("Found it!",codeToken)
		if R.grab(): # if we grab the token, we move the robot backward, release the box, and turn a little bit on left to dom't see the same box 
		    print("Gotcha!")
	      	    if dist_silver_area<d_th:
	      	    	tokenToApproach.remove(codeToken)
		    	R.release()
		    elif -a_th<= rot_y_silver_area <= a_th: # if the robot is well aligned with the silver_area, we go forward
			print("Ah, that'll do.")
			drive(20, 0.5)
		    elif rot_y_silver_area < -a_th: # if the robot is not well aligned with the silver_area, we move it on the left or on the right
			print("Left a bit...")
			turn(-2, 0.5)
		    elif rot_y_silver_area > a_th:
			print("Right a bit...")
			turn(+2, 0.5)
		    print('remaining tokens (ToDoList):',tokenToApproach)
		
		    
		else:
		    print("Aww, I'm not close enough.")
	    elif -a_th<= rot_y <= a_th: # if the robot is well aligned with the token, we go forward
		print("Ah, that'll do.")
		drive(20, 0.5)
	    elif rot_y < -a_th: # if the robot is not well aligned with the token, we move it on the left or on the right
		print("Left a bit...")
		turn(-2, 0.5)
	    elif rot_y > a_th:
		print("Right a bit...")
		turn(+2, 0.5)
 
def alignGolden(golden_tokens):
	
	#this while is used to bring the golden boxes closer to the gray area
	while not len(golden_tokens)==0: #stop the while when there are no tokens anymore 
	    
	    dist, rot_y, codeToken = find_golden_token()
	    if dist==-1: # if no token is detected, we make the robot turn 
		print("I don't see any token!!")
		turn(-10, 1) #turn a little bit on left
	    elif dist <d_th: # if we are close to the token, we try grab it.
		print("Found it!",codeToken)
		if R.grab(): # if we grab the token, we move the robot backward, release the box, and turn a little bit on left to dom't see the same box 
		    print("Gotcha!")
	      	    if dist_golden_area<d_th:
	      	    	tokenToApproach.remove(codeToken)
		    	R.release()
		    elif -a_th<= rot_y_golden_area <= a_th: # if the robot is well aligned with the golden_area, we go forward
			print("Ah, that'll do.")
			drive(20, 0.5)
		    elif rot_y_golden_area < -a_th: # if the robot is not well aligned with the golden_area, we move it on the left or on the right
			print("Left a bit...")
			turn(-2, 0.5)
		    elif rot_y_golden_area > a_th:
			print("Right a bit...")
			turn(+2, 0.5)
		    print('remaining tokens (ToDoList):',tokenToApproach)
		
		    
		else:
		    print("Aww, I'm not close enough.")
	    elif -a_th<= rot_y <= a_th: # if the robot is well aligned with the token, we go forward
		print("Ah, that'll do.")
		drive(20, 0.5)
	    elif rot_y < -a_th: # if the robot is not well aligned with the token, we move it on the left or on the right
		print("Left a bit...")
		turn(-2, 0.5)
	    elif rot_y > a_th:
		print("Right a bit...")
		turn(+2, 0.5)






silver_tokens, golden_tokens=init()
alignSilver(silver_tokens)        
alignGolden(golden_tokens)
print("work done!")
    
  
