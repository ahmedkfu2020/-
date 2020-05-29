# we import all necessary methods and objects
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer
from random import randrange

# we use 8 qubits and 8 classical bits
q = QuantumRegister(8)
c = ClassicalRegister(8)

qc = QuantumCircuit(q,c)

# we store the index of each qubit to which x-gate is applied
picked_qubits=[] 

for i in range(8):
    if randrange(2) == 0: # Assume that 0 is Head and 1 is Tail
        qc.x(q[i]) # apply x-gate
        print("x-gate is applied to the qubit with index",i)
        picked_qubits.append(i) # i is picked

# define a barrier
qc.barrier()

# measurement 
qc.measure(q,c)  

# draw the circuit

#mycircuit.draw(reverse_bits=True)
qc.draw(output='mpl',reverse_bits=True)

# execute the circuit and read the results
job = execute(qc,Aer.get_backend('qasm_simulator'),shots=256)

counts = job.result().get_counts(qc)
        
print(counts)
