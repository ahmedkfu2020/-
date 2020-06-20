# import all necessary objects and methods for quantum circuits
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer

all_pairs = ['00','01','10','11']

for pair in all_pairs:

    # create a quantum curcuit with two qubits: Asja's and Balvis' qubits.
    # both are initially set to |0>.
    qreg = QuantumRegister(2) # quantum register with 2 qubits
    creg = ClassicalRegister(2) # classical register with 2 bits
    mycircuit = QuantumCircuit(qreg,creg) # quantum circuit with quantum and classical registers

    # apply h-gate (Hadamard) to the first qubit.
    mycircuit.h(qreg[0])

    # apply cx-gate (CNOT) with parameters first-qubit and second-qubit.
    mycircuit.cx(qreg[0],qreg[1])

    # they are separated now.

    # if a is 1, then apply z-gate to the first qubit.
    if pair[0]=='1': 
        mycircuit.z(qreg[0])
    
    # if b is 1, then apply x-gate (NOT) to the first qubit.
    if pair[1]=='1': 
        mycircuit.x(qreg[0])
    
    # Asja sends her qubit to Balvis.
    
    #  apply cx-gate (CNOT) with parameters first-qubit and second-qubit.
    mycircuit.cx(qreg[0],qreg[1])
    
    # apply h-gate (Hadamard) to the first qubit.
    mycircuit.h(qreg[0])
    
    # measure both qubits
    mycircuit.measure(qreg,creg)
    
    # compare the results with pair (a,b)
    job = execute(mycircuit,Aer.get_backend('qasm_simulator'),shots=100)
    counts = job.result().get_counts(mycircuit)
    for outcome in counts:
        reverse_outcome = ''
        for i in outcome:
            reverse_outcome = i + reverse_outcome
        print("(a,b) is",pair,": ",reverse_outcome,"is observed",counts[outcome],"times")
