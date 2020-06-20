%run ../include/quantum.py

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer

qreg12 =  QuantumRegister(19)
creg12 = ClassicalRegister(19)

mycircuit12 = QuantumCircuit(qreg12,creg12)

for i in range(10):
    mycircuit12.h(qreg12[i])

mycircuit12.x(qreg12[18])
mycircuit12.h(qreg12[18])

#number of iterations - change this value
iteration_count = 0
for i in range(iteration_count):
    giant_oracle(mycircuit12,qreg12,0)
    giant_diffusion(mycircuit12,qreg12)
    
mycircuit12.h(qreg12[18])
mycircuit12.x(qreg12[18])

mycircuit12.measure(qreg12,creg12)

job = execute(mycircuit12,Aer.get_backend('qasm_simulator'),shots=10000)
counts12 = job.result().get_counts(mycircuit12)
print(counts12)
