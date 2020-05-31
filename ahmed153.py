# import all necessary objects and methods for quantum circuits
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer

# define a quantum register with a single qubit
q = QuantumRegister(1)
# define a classical register with a single bit
c = ClassicalRegister(1,"c")
# define a quantum circuit
qc = QuantumCircuit(q,c)

# start in state |1>
qc.x(q[0])

# apply the first Hadamard
qc.h(q[0])

# the first measurement
qc.measure(q,c)

# apply the second Hadamard if the measurement outcome is 1
qc.h(q[0]).c_if(c,1)

# the second measurement
qc.measure(q[0],c)

# draw the circuit
qc.draw(output="mpl")

# execute the circuit 1000 times in the local simulator

job = execute(qc,Aer.get_backend('qasm_simulator'),shots=1000)
counts = job.result().get_counts(qc)   
print(counts)
