#state - the state of control qubits, between 0 and 15.
def control(circuit,quantum_reg,state):
    if(state%2 == 0):
        circuit.x(quantum_reg[3])
    if(state%4 < 2):
        circuit.x(quantum_reg[4])
    if(state%8 < 4):
        circuit.x(quantum_reg[5])
    if(state < 8):
        circuit.x(quantum_reg[6])
    circuit.ccx(quantum_reg[6],quantum_reg[5],quantum_reg[2])
    circuit.ccx(quantum_reg[4],quantum_reg[3],quantum_reg[1])
    circuit.ccx(quantum_reg[2],quantum_reg[1],quantum_reg[0])
    circuit.ccx(quantum_reg[4],quantum_reg[3],quantum_reg[1])
    circuit.ccx(quantum_reg[6],quantum_reg[5],quantum_reg[2])
    if(state < 8):
        circuit.x(quantum_reg[6])
    if(state%8 < 4):
        circuit.x(quantum_reg[5])
    if(state%4 < 2):
        circuit.x(quantum_reg[4])
    if(state%2 == 0):
        circuit.x(quantum_reg[3])
        
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer

qreg6 =  QuantumRegister(7)
creg6 = ClassicalRegister(7)

mycircuit6 = QuantumCircuit(qreg6,creg6)

mycircuit6.x(qreg6[5])
mycircuit6.x(qreg6[3])
control(mycircuit6,qreg6,5)
mycircuit6.measure(qreg6,creg6)

job = execute(mycircuit6,Aer.get_backend('qasm_simulator'),shots=10000)
counts6 = job.result().get_counts(mycircuit6)
print(counts6)

