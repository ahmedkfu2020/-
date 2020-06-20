#number - marked element, between 0 and 7.
def big_query(circuit,quantum_reg,number):
    # prepare ancilla qubit
    circuit.x(quantum_reg[4])
    circuit.h(quantum_reg[4])

    if(number%2 == 0):
        circuit.x(quantum_reg[0])
    if(number%4 < 2):
        circuit.x(quantum_reg[1])
    if(number < 4):
        circuit.x(quantum_reg[2])
    circuit.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[3])
    circuit.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[4])
    circuit.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[3])
    if(number < 4):
        circuit.x(quantum_reg[2])
    if(number%4 < 2):
        circuit.x(quantum_reg[1])
    if(number%2 == 0):
        circuit.x(quantum_reg[0])

    # put ancilla qubit back into state |0>
    circuit.h(quantum_reg[4])
    circuit.x(quantum_reg[4])
    
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer

big_qreg =  QuantumRegister(5)
big_creg = ClassicalRegister(5)

big_mycircuit = QuantumCircuit(big_qreg,big_creg)

#Any value between 0 and 7.
big_query(big_mycircuit,big_qreg,5)

job = execute(big_mycircuit,Aer.get_backend('unitary_simulator'))
u=job.result().get_unitary(big_mycircuit,decimals=3)
# print top-left 8x8 entries of the matrix.
for i in range(8):
    s=""
    for j in range(8):
        val = str(u[i][j].real)
        while(len(val)<5): val  = " "+val
        s = s + val
    print(s)
