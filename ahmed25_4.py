from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer
from math import pi, sin, cos
from random import randrange

# the angle of rotation
k1 = randrange(1,31)
theta1 = k1*2*pi/31
k2 = randrange(1,31)
theta2 = k2*2*pi/31
k3 = randrange(1,31)
theta3 = k3*2*pi/31

max_percentange = 0
    
# for each stream of length from 1 to 31
for i in range(1,32):    
    # initialize the circuit
    qreg = QuantumRegister(3) 
    creg = ClassicalRegister(3) 
    circuit = QuantumCircuit(qreg,creg)
    
    # Hadamard operators before reading the stream
    for m in range(3):
        circuit.h(qreg[m])   
        
    # read the stream of length i
    print("stream of length",i,"is being read")
    for j in range(i):    
        # controlled rotation when the third qubit is |1>
        circuit.cu3(2*theta1,0,0,qreg[2],qreg[0])

        # controlled rotation when the second qubit is |1>
        circuit.cu3(2*theta2,0,0,qreg[1],qreg[0])

        # controlled rotation when the third qubit is |0>
        circuit.x(qreg[2])
        circuit.cu3(2*theta3,0,0,qreg[2],qreg[0])
        circuit.x(qreg[2])
        
    # Hadamard operators after reading the stream
    for m in range(3):
        circuit.h(qreg[m])  
    # we measure after reading the whole stream
    circuit.measure(qreg,creg)
    # execute the circuit N times
    N = 1000
    job = execute(circuit,Aer.get_backend('qasm_simulator'),shots=N)
    counts = job.result().get_counts(circuit)
    print(counts)
    if '000' in counts.keys():
        c = counts['000']
    else:
        c = 0
    print('000 is observed',c,'times out of',N)
    percentange = round(c/N*100,1)
    if max_percentange < percentange and i != 31: max_percentange = percentange
    print("the ration of 000 is ",percentange,"%")
    print()  
print("maximum percentage of observing unwanted '000' is",max_percentange)
