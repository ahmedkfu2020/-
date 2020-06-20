from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer
from math import pi, cos, sin
from random import randrange

# quantum circuit with three qubits and three bits
qreg =  QuantumRegister(3) 
creg = ClassicalRegister(3) 
mycircuit = QuantumCircuit(qreg,creg)

# rotate the first qubit by random angle
r = randrange(100)
theta = 2*pi*(r/100) # radians
print("the picked angle is",r*3.6,"degrees and",theta,"radians")
a = cos(theta)
b = sin(theta)
print("a=",round(a,3),"b=",round(b,3))
print("a*a=",round(a**2,3),"b*b=",round(b**2,3))
print()
mycircuit.ry(2*theta,qreg[2])

# creating an entanglement between the second and third qubits
mycircuit.h(qreg[1])
mycircuit.cx(qreg[1],qreg[0])

# CNOT operator by Asja on her qubits where the first qubit is the control qubit 
mycircuit.cx(qreg[2],qreg[1])

# Hadamard operator by Asja on the first qubit
mycircuit.h(qreg[2])

# measurement done by Asja
mycircuit.measure(qreg[2],creg[2])
mycircuit.measure(qreg[1],creg[1])

# read the state vector
job = execute(mycircuit,Aer.get_backend('statevector_simulator'),optimization_level=0)
current_quantum_state=job.result().get_statevector(mycircuit)
print("the state vector is")
for i in range(len(current_quantum_state)):
    print(current_quantum_state[i].real)
print()

classical_outcomes = ['00','01','10','11']

for i in range(4):
    if (current_quantum_state[2*i].real != 0) or (current_quantum_state[2*i+1].real != 0):
        print("the classical outcome is",classical_outcomes[i])
        classical_outcome = classical_outcomes[i]
        balvis_state = [ current_quantum_state[2*i].real,current_quantum_state[2*i+1].real ]
print()
        
readable_quantum_state = "|"+classical_outcome+">"
readable_quantum_state += "("+str(round(balvis_state[0],3))+"|0>+"+str(round(balvis_state[1],3))+"|1>)"
print("the new quantum state is",readable_quantum_state)


all_states = ['000','001','010','011','100','101','110','111']

        
balvis_state_str = "|"+classical_outcome+">("
for i in range(len(current_quantum_state)):
    if abs(current_quantum_state[i].real-a)<0.000001: 
        balvis_state_str += "+a|"+ all_states[i][2]+">"
    elif abs(current_quantum_state[i].real+a)<0.000001:
        balvis_state_str += "-a|"+ all_states[i][2]+">"
    elif abs(current_quantum_state[i].real-b)<0.000001: 
        balvis_state_str += "+b|"+ all_states[i][2]+">"
    elif abs(current_quantum_state[i].real+b)<0.000001: 
        balvis_state_str += "-b|"+ all_states[i][2]+">"
balvis_state_str += ")"        
print("the new quantum state is",balvis_state_str)
print()

mycircuit.draw()
