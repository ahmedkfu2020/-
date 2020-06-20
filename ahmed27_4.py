# include our predefined functions
%run qlatvia.py

# import all necessary objects and methods for quantum circuits
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer
from math import acos, pi
# after Hadamard operators
u = [(63/64)**0.5,(1/64)**0.5]

def angle_between_two_states(u1,u2):
    dot_product = u1[0]*u2[0]+u1[1]*u2[1]
    return acos(dot_product)

theta = angle_between_two_states(u,[1,0])

all_visited_quantum_states =[]


qreg3 = QuantumRegister(1) # quantum register with 1 qubit
creg3 = ClassicalRegister(1) # classical register with 1 bit
mycircuit3 = QuantumCircuit(qreg3,creg3) # quantum circuit with quantum and classical registers


# set the qubit to |u> by rotating it by theta
mycircuit3.ry(2*theta,qreg3[0])

# read and store the current quantum state
current_state = execute(mycircuit3,Aer.get_backend('statevector_simulator')).result().get_statevector(mycircuit3)
[x,y] = [current_state[0].real,current_state[1].real]
all_visited_quantum_states.append([x,y,'u'])


# three iterations
for i in range(3): # 4,5,6,7,8,9,10
    # the first reflection
    theta = angle_between_two_states([x,y],[1,0])
    mycircuit3.ry(2*(-2*theta),qreg3[0])

    # read and store the current quantum state
    current_state = execute(mycircuit3,Aer.get_backend('statevector_simulator')).result().get_statevector(mycircuit3)
    [x,y] = [current_state[0].real,current_state[1].real]
    all_visited_quantum_states.append([x,y,'r'+str(i+1)])

    # the second reflection 
    theta = angle_between_two_states(u,[x,y])
    mycircuit3.ry(2*(2*theta),qreg3[0])

    # read and store the current quantum state
    current_state = execute(mycircuit3,Aer.get_backend('statevector_simulator')).result().get_statevector(mycircuit3)
    [x,y] = [current_state[0].real,current_state[1].real]
    all_visited_quantum_states.append([x,y,'n'+str(i+1)])    
    
# measure the qubit
mycircuit3.measure(qreg3,creg3)
    
    
# execute the circuit 100 times, and print the outcomes
job = execute(mycircuit3,Aer.get_backend('qasm_simulator'),shots=100)
counts3 = job.result().get_counts(mycircuit3)
print(counts3)

# visualization
draw_qubit()
for quantum_state in all_visited_quantum_states:
    draw_quantum_state(quantum_state[0],quantum_state[1],quantum_state[2])
