# import all necessary objects and methods for quantum circuits
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer
# import randrange for random choices
from random import randrange

n = 5
m = 4

states_of_qubits = [] # we trace the state of each qubit also by ourselves

qreg1 =  QuantumRegister(n) # quantum register with n qubits
creg1 = ClassicalRegister(n) # classical register with n bits

mycircuit1 = QuantumCircuit(qreg1,creg1) # quantum circuit with quantum and classical registers

# set each qubit to |1>
for i in range(n):
    mycircuit1.x(qreg1[i]) # apply x-gate (NOT operator)
    states_of_qubits.append(1) # the state of each qubit is set to 1
    
# randomly pick m pairs of qubits
for i in range(m):
    controller_qubit = randrange(n)
    target_qubit = randrange(n)
    # controller and target qubits should be different
    while controller_qubit == target_qubit: # if they are the same, we pick the target_qubit again
        target_qubit = randrange(n)
    # print our picked qubits
    print("the indices of the controller and target qubits are",controller_qubit,target_qubit)
    # apply cx-gate (CNOT operator)
    mycircuit1.cx(qreg1[controller_qubit],qreg1[target_qubit])
    # we also trace the results
    if states_of_qubits[controller_qubit] == 1: # if the value of the controller qubit is 1,
        states_of_qubits[target_qubit] = 1 - states_of_qubits[target_qubit] # then flips the value of the target qubit 
        # remark that 1-x gives the negation of x
    

# measure the quantum register
mycircuit1.measure(qreg1,creg1)

print("Everything looks fine, let's continue ...")

# draw the circuit

mycircuit1.draw(output='mpl')
# re-execute this cell if you DO NOT see the circuit diagram

# execute the circuit 100 times in the local simulator

job = execute(mycircuit1,Aer.get_backend('qasm_simulator'),shots=100)
counts = job.result().get_counts(mycircuit1)

# print the reverse of the outcome
for outcome in counts:
    reverse_outcome = ''
    for i in outcome:
        reverse_outcome = i + reverse_outcome
    print(reverse_outcome,"is observed",counts[outcome],"times")

# the states of the qubits should be as follows based on our own calculation
print(states_of_qubits)


