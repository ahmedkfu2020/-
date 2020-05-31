# import all necessary objects and methods for quantum circuits
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer
# import randrange for random choices
from random import randrange

# define a quantum register with a single qubit
q = QuantumRegister(1)
# define a classical register with a single bit
c = ClassicalRegister(1,"c")
# define a quantum circuit
qc = QuantumCircuit(q,c)

shot = 10000

observe = [0,0]

qc.h(q[0])
qc.measure(q,c)
observe = [shot/2,shot/2]

for i in range(4):
    x = randrange(2)
    if x==0:
        observe[0] = observe[0] / 2 
        observe[1] = observe[1] + observe[0]
    else:
        observe[1] = observe[1] / 2 
        observe[0] = observe[0] + observe[1]
    qc.h(q[0]).c_if(c,x)
    qc.measure(q,c)

# draw the circuit
qc.draw(output="mpl")

print('0:',round(observe[0]),'1:',round(observe[1]))

# execute the circuit 10000 times in the local simulator
job = execute(qc,Aer.get_backend('qasm_simulator'),shots=shot)
counts = job.result().get_counts(qc)   
print(counts)
