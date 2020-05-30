# import all necessary objects and methods for quantum circuits
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer

# define a quantum register with one qubit
q =  QuantumRegister(1,"qreg")

# define a classical register with one bit
# it stores the measurement result of the quantum part
c = ClassicalRegister(1,"creg")

# define our quantum circuit
qc = QuantumCircuit(q,c)

# apply x-gate to the first qubit
qc.x(q[0])

# apply h-gate (Hadamard: quantum coin-flipping) to the first qubit
qc.h(q[0])

# measure the first qubit, and store the result in the first classical bit
qc.measure(q,c)

# draw the circuit by using matplotlib
qc.draw(output='mpl') # re-run the cell if the figure is not displayed

# execute the circuit and read the results
job = execute(qc,Aer.get_backend('qasm_simulator'),shots=10000)

counts = job.result().get_counts(qc)
print(counts)

# import all necessary objects and methods for quantum circuits
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer

# define a quantum register with one qubit
q2 =  QuantumRegister(1,"qreg2")

# define a classical register with one bit
# it stores the measurement result of the quantum part
c2 = ClassicalRegister(1,"creg2")

# define our quantum circuit
qc2 = QuantumCircuit(q2,c2)

# apply x-gate to the first qubit
qc2.x(q2[0])

# apply h-gate (Hadamard: quantum coin-flipping) to the first qubit twice
qc2.h(q2[0])
qc2.h(q2[0])

# measure the first qubit, and store the result in the first classical bit
qc2.measure(q2,c2)


# draw the circuit by using matplotlib
qc2.draw(output='mpl') # re-run the cell if the figure is not displayed

# execute the circuit and read the results
job = execute(qc2,Aer.get_backend('qasm_simulator'),shots=10000)

counts2 = job.result().get_counts(qc2)
print(counts2)
