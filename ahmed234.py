from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer
from math import pi
from random import randrange

# for each stream of length from 1 to 10
for i in range(1,11):
    # we try each angle of the form k*2*pi/11 for k=1,...,10
    # we try to find the best k for which we observe 1 the most
    number_of_one_state = 0
    best_k = 1
    all_outcomes_for_i = "length "+str(i)+"-> "
    for k in range(1,11):
        theta = k*2*pi/11
        # quantum circuit with one qubit and one bit
        qreg =  QuantumRegister(1) 
        creg = ClassicalRegister(1) 
        mycircuit = QuantumCircuit(qreg,creg)
        # the stream of length i
        for j in range(i):
            mycircuit.ry(2*theta,qreg[0]) # apply one rotation for each symbol
            # we measure after reading the whole stream
        mycircuit.measure(qreg[0],creg[0])
        # execute the circuit 10000 times
        job = execute(mycircuit,Aer.get_backend('qasm_simulator'),shots=10000)
        counts = job.result().get_counts(mycircuit)
        all_outcomes_for_i = all_outcomes_for_i + str(k)+ ":" + str(counts['1']) + "  "
        if int(counts['1']) > number_of_one_state:
            number_of_one_state = counts['1']
            best_k = k
    print(all_outcomes_for_i)
    print("for length",i,", the best k is",best_k)
    print()
