from qiskit import QuantumCircuit
from qiskit_aer import Aer
import numpy as np


# Number of qubits
n = 3
qc = QuantumCircuit(n, n)

# Step 1: create uniform superposition
for qubit in range(n):
    qc.h(qubit)

# Step 2: Oracle marking |101>
qc.x(1)        # flip bit 1 (because target is 101 -> bit1 = 0)

qc.h(2)
qc.ccx(0, 1, 2)  # h+ccx+h is the equivalent of ccz bit flip is converted to phase flip
qc.h(2) 

qc.x(1)

# Step 3: Diffusion operator
def diffusion(qc, n):
    # Apply H
    for qubit in range(n):
        qc.h(qubit)          #here, H is used to change basis from computational to phase basis
    # Apply X
    for qubit in range(n):
        qc.x(qubit)
    # Apply CCZ using h-ccx-h to phase flip bit number 2 
    qc.h(n-1)
    qc.ccx(0, 1, 2)
    qc.h(n-1)
    # Undo X
    for qubit in range(n):
        qc.x(qubit)
    # Undo H 
    for qubit in range(n):
        qc.h(qubit)

# Step 4: Apply Grover iterations
N = 2**n
k = int(np.floor((np.pi/4)*np.sqrt(N)))    

for _ in range(k):
    # Oracle again
    qc.x(1)
    qc.h(2)
    qc.ccx(0, 1, 2)
    qc.h(2)
    qc.x(1)

    # Diffusion
    diffusion(qc, n)

# Step 5: Measurement + simulation
qc.measure(range(n), range(n))

backend = Aer.get_backend('qasm_simulator')

job = backend.run(qc, shots=1000)
result = job.result()
counts = result.get_counts()
print(counts)

