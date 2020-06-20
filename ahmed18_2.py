# randomly create a 2-dimensional quantum state
from math import cos, sin, pi
from random import randrange
def random_quantum_state2():
    angle_degree = randrange(360)
    angle_radian = 2*pi*angle_degree/360
    return [cos(angle_radian),sin(angle_radian)]
    
    %run qlatvia.py

draw_qubit()

# line of reflection for Hadamard
from matplotlib.pyplot import arrow
arrow(-1.109,-0.459,2.218,0.918,linestyle='dotted',color='red')

[x1,y1] = random_quantum_state2()

print(x1,y1)

sqrttwo=2**0.5
oversqrttwo = 1/sqrttwo

[x2,y2] = [ oversqrttwo*x1 + oversqrttwo*y1 , oversqrttwo*x1 - oversqrttwo*y1 ]

print(x2,y2)

draw_quantum_state(x1,y1,"main")

draw_quantum_state(x2,y2,"ref")

