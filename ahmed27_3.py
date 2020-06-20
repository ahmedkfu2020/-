# include our predefined functions
%run qlatvia.py

# import all necessary objects and methods for quantum circuits
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer
from math import acos, pi
# after Hadamard operators
u = [(13/16)**0.5,(3/16)**0.5]

def angle_between_two_states(u1,u2):
    dot_product = u1[0]*u2[0]+u1[1]*u2[1]
    return acos(dot_product)

theta = angle_between_two_states(u,[1,0])

all_visited_quantum_states =[]


qreg2 = QuantumRegister(1) # quantum register with 1 qubit
creg2 = ClassicalRegister(1) # classical register with 1 bit
mycircuit2 = QuantumCircuit(qreg2,creg2) # quantum circuit with quantum and classical registers


# set the qubit to |u> by rotating it by theta
mycircuit2.ry(2*theta,qreg2[0])

# read and store the current quantum state
current_state = execute(mycircuit2,Aer.get_backend('statevector_simulator')).result().get_statevector(mycircuit2)
[x,y] = [current_state[0].real,current_state[1].real]
all_visited_quantum_states.append([x,y,'u'])


# the first reflection
theta = angle_between_two_states([x,y],[1,0])
mycircuit2.ry(2*(-2*theta),qreg2[0])

# read and store the current quantum state
current_state = execute(mycircuit2,Aer.get_backend('statevector_simulator')).result().get_statevector(mycircuit2)
[x,y] = [current_state[0].real,current_state[1].real]
all_visited_quantum_states.append([x,y,'r'])



# the second reflection 
theta = angle_between_two_states(u,[x,y])
mycircuit2.ry(2*(2*theta),qreg2[0])

# read and store the current quantum state
current_state = execute(mycircuit2,Aer.get_backend('statevector_simulator')).result().get_statevector(mycircuit2)
[x,y] = [current_state[0].real,current_state[1].real]
all_visited_quantum_states.append([x,y,'n'])    
    
# measure the qubit
mycircuit2.measure(qreg2,creg2)
    
    
# execute the circuit 100 times, and print the outcomes
job = execute(mycircuit2,Aer.get_backend('qasm_simulator'),shots=100)
counts2 = job.result().get_counts(mycircuit2)
print(counts2)

# visualization
draw_qubit()
for quantum_state in all_visited_quantum_states:
    draw_quantum_state(quantum_state[0],quantum_state[1],quantum_state[2])
