# class unknown_qubit
#   available_qubit = 1000 -> you get at most 1000 qubit copies
#   get_qubits(number_of_qubits) -> you get the specified number of qubits for your experiment
#   measure_qubits() -> your qubits are measured and the result is returned as a dictionary variable
#                    -> after measurement, these qubits are destroyed
#   rotate_qubits(angle) -> your qubits are rotated with the specified angle in radian
#   compare_my_guess(my_angle) -> your guess in radian is compared with the real angle

from random import randrange
from math import pi
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer
class unknown_qubit:   
    def __init__(self):
        self.__theta = randrange(18000)/18000*pi        
        self.__available_qubits = 1000
        self.__active_qubits = 0
        print(self.__available_qubits,"qubits are created")
    
    def get_qubits(self,number_of_qubits=None):
        if number_of_qubits is None or isinstance(number_of_qubits,int) is False or number_of_qubits < 1:
            print()
            print("ERROR: the method 'get_qubits' takes the number of qubit(s) as a positive integer, i.e., get_qubits(100)")
        elif number_of_qubits <= self.__available_qubits:
            self.__qc = QuantumCircuit(1,1)
            self.__qc.ry(2 * self.__theta,0)
            self.__active_qubits = number_of_qubits
            self.__available_qubits = self.__available_qubits - self.__active_qubits
            print()
            print("You have",number_of_qubits,"active qubits that are set to (cos(theta),sin(theta))")
            self.available_qubits()
        else:
            print()
            print("WARNING: you requested",number_of_qubits,"qubits, but there is not enough available qubits!")
            self.available_qubits()
            
    def measure_my_qubits(self):    
        if self.__active_qubits > 0:            
            self.__qc.measure(0,0)
            job = execute(self.__qc,Aer.get_backend('qasm_simulator'),shots=self.__active_qubits)
            counts = job.result().get_counts(self.__qc)
            print()
            print("your",self.__active_qubits,"qubits are measured")
            print("counts = ",counts)
            self.__active_qubits = 0
            return counts
        else:
            print()
            print("WARNING: there is no active qubits -- you might first execute 'get_qubits()' method")
            self.available_qubits()
            
    def rotate_qubits(self,angle=None):
        if angle is None or (isinstance(angle,float) is False and isinstance(angle,int) is False):
            print()
            print("ERROR: the method 'rotate_qubits' takes a real-valued angle in radian as its parameter, i.e., rotate_qubits(1.2121)")
        elif self.__active_qubits > 0:
            self.__qc.ry(2 * angle,0)
            print()
            print("your active qubits are rotated by angle",angle,"in radian")
        else:
            print()
            print("WARNING: there is no active qubits -- you might first execute 'get_qubits()' method")
            self.available_qubits()    
    
    def compare_my_guess(self,my_angle):
        if my_angle is None or (isinstance(my_angle,float) is False and isinstance(my_angle,int) is False):
            print("ERROR: the method 'compare_my_guess' takes a real-valued angle in radian as your guessed angle, i.e., compare_my_guess(1.2121)")
        else:
            self.__available_qubits = 0
            diff = abs(my_angle-self.__theta)
            print()
            print(self.__theta,"is the original",)
            print(my_angle,"is your guess")
            print("the angle difference between the original theta and your guess is",diff/pi*180,"degree")
            print("-->the number of available qubits is (set to) zero, and so you cannot make any further experiment")

    def available_qubits(self):
        print("--> the number of available unused qubit(s) is",self.__available_qubits)              
        
from math import pi, cos, sin, acos, asin

my_experiment = unknown_qubit()

# we use 900 copies to determine our two candidates
my_experiment.get_qubits(900)
counts = my_experiment.measure_my_qubits()

number_of_observed_zeros = 0
if '0' in counts:
    number_of_observed_zeros = counts['0']

probability_of_observing_zeros = number_of_observed_zeros/900
cos_theta = probability_of_observing_zeros ** 0.5
theta = acos(cos_theta)

theta_first_candidate = theta
theta_second_candidate = pi-theta

print("the first candidate is",theta_first_candidate,"in radian and",theta_first_candidate*180/pi,"in degree")
print("the second candidate is",theta_second_candidate,"in radian and",theta_second_candidate*180/pi,"in degree")

my_experiment.get_qubits(100)
my_experiment.rotate_qubits(-1 * theta_first_candidate)

counts = my_experiment.measure_my_qubits()
number_of_observed_zeros = 0
if '0' in counts:
    number_of_observed_zeros = counts['0']

if number_of_observed_zeros == 100:
    my_guess = theta_first_candidate
else:
    my_guess = theta_second_candidate
    
my_experiment.compare_my_guess(my_guess)

## Multiple Experiments

for i in range(10):
    print("Experiment",(i+1))
    print("___________")
    print()
    my_experiment = unknown_qubit()
    my_experiment.get_qubits(900)
    counts = my_experiment.measure_my_qubits()

    number_of_observed_zeros = 0
    if '0' in counts:
        number_of_observed_zeros = counts['0']

    probability_of_observing_zeros = number_of_observed_zeros/900
    cos_theta = probability_of_observing_zeros ** 0.5
    theta = acos(cos_theta)

    theta_first_candidate = theta
    theta_second_candidate = pi-theta
    
    my_experiment.get_qubits(100)
    my_experiment.rotate_qubits(-1 * theta_first_candidate)

    counts = my_experiment.measure_my_qubits()
    number_of_observed_zeros = 0
    if '0' in counts:
        number_of_observed_zeros = counts['0']

    if number_of_observed_zeros == 100:
        my_guess = theta_first_candidate
    else:
        my_guess = theta_second_candidate

    my_experiment.compare_my_guess(my_guess)
    print()
    print()
    print()
