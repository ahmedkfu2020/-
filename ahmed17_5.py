from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer
from math import pi, cos, sin

# first qubit 
qreg =  QuantumRegister(1) 
creg = ClassicalRegister(1) 
mycircuit = QuantumCircuit(qreg,creg)

theta=pi/4

for i in range(1,9):
    total_theta = i*theta
    mycircuit.ry(2*theta,qreg[0])
    job = execute(mycircuit, Aer.get_backend('unitary_simulator'),optimization_level=0)
    current_unitary = job.result().get_unitary(mycircuit, decimals=3)
    print("after",i,"iteration(s):")
    print(current_unitary[0][0].real,current_unitary[0][1].real)
    print(current_unitary[1][0].real,current_unitary[1][1].real)
    print("calculated by python:")
    print(round(cos(total_theta),3),round(-sin(total_theta),3))
    print(round(sin(total_theta),3),round(cos(total_theta),3))
    print()
