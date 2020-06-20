# import all necessary objects and methods for quantum circuits
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer

qreg = QuantumRegister(4) # quantum register with 4 qubits
creg = ClassicalRegister(4) # classical register with 4 bits
mycircuit = QuantumCircuit(qreg,creg) # quantum circuit with quantum and classical registers

# apply h-gate (Hadamard) to each qubit
for i in range(4):
    mycircuit.h(qreg[i])

# measure all qubits
mycircuit.measure(qreg,creg)
    
# execute the circuit 1600 times, and print the outcomes
job = execute(mycircuit,Aer.get_backend('qasm_simulator'),shots=1600)
counts = job.result().get_counts(mycircuit)
for outcome in counts:
    reverse_outcome = ''
    for i in outcome:
        reverse_outcome = i + reverse_outcome
    print(reverse_outcome,"is observed",counts[outcome],"times")
