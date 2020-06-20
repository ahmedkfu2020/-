%run qlatvia.py

draw_qubit()

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer
from math import pi

# we define a quantum circuit with one qubit and one bit
q =  QuantumRegister(1) # quantum register with a single qubit
c = ClassicalRegister(1) # classical register with a single bit
qc = QuantumCircuit(q,c) # quantum circuit with quantum and classical registers

rotation_angle = 3*pi/8

for i in range(1,17):
    # rotate the qubit with angle pi/4
    qc.ry(2*rotation_angle,q[0]) 
    
    # read the current quantum state
    job = execute(qc,Aer.get_backend('statevector_simulator'),optimization_level=0)
    current_quantum_state=job.result().get_statevector(qc) 
    
    # print the current quantum state    
    x_value = current_quantum_state[0].real # get the amplitude of |0>
    y_value = current_quantum_state[1].real # get the amplitude of |1>
    print("iteration",i,": the quantum state is (",round(x_value,3),") |0>","+(",round(y_value,3),") |1>")
    
    # draw the current quantum state
    draw_quantum_state(x_value,y_value,"|v"+str(i)+">")
