# import all necessary objects and methods for quantum circuits
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer

# define a quantum register with one qubit
q2 =  QuantumRegister(1,"qreg2")

# define a classical register with one bit
# it stores the measurement result of the quantum part
c2 = ClassicalRegister(1,"creg2")

# define our quantum circuit
qc2 = QuantumCircuit(q2,c2)

# apply h-gate (Hadamard: quantum coin-flipping) to the first qubit
qc2.h(q2[0])

# apply h-gate (Hadamard: quantum coin-flipping) to the first qubit once more
qc2.h(q2[0])

# measure the first qubit, and store the result in the first classical bit
qc2.measure(q2,c2)

# draw the circuit by using matplotlib
qc2.draw(output='mpl') # re-run the cell if the figure is not displayed

# execute the circuit 10000 times in the local simulator

job = execute(qc2,Aer.get_backend('qasm_simulator'),shots=10000)
counts2 = job.result().get_counts(qc2)
print(counts2) # print the outcomes
