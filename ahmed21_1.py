# import all necessary objects and methods for quantum circuits
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer

qreg1 =  QuantumRegister(2) # quantum register with 2 qubits
creg1 = ClassicalRegister(2) # classical register with 2 bits

mycircuit1 = QuantumCircuit(qreg1,creg1) # quantum circuit with quantum and classical registers

# the first qubit is in |0>

# set the second qubit to |1>
mycircuit1.x(qreg1[1]) # apply x-gate (NOT operator)

# apply Hadamard to both qubits.
mycircuit1.h(qreg1[0])
mycircuit1.h(qreg1[1])

# apply CNOT operator, where the controller qubit is the first qubit and the target qubit is the second qubit.
mycircuit1.cx(qreg1[0],qreg1[1])

# apply Hadamard to both qubits.
mycircuit1.h(qreg1[0])
mycircuit1.h(qreg1[1])

# measure both qubits
mycircuit1.measure(qreg1,creg1)

# execute the circuit 100 times in the local simulator

job = execute(mycircuit1,Aer.get_backend('qasm_simulator'),shots=100)
counts = job.result().get_counts(mycircuit1)

# print the reverse of the outcome
for outcome in counts:
    reverse_outcome = ''
    for i in outcome:
        reverse_outcome = i + reverse_outcome
    print("We start in quantum state 01, and",reverse_outcome,"is observed",counts[outcome],"times")
