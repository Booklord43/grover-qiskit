# grover-qiskit
for acm
This project is implementation of Grover's Algorithm using qiskit(an open source software for writing and simulating quantum programs without a quantum computer). 
This demo is run on a 3-qubit system with answer set as |101>

Grover's algorithm is a quantum searching algorithm , instead of a classical linear search, it uses quantum mechanics to speed up the process. It is a quadratic speedup

Classical search : O(N) 
Grover's search: O(sqrt((N))).
 i.e, if a classic search finds answer in N checks, grovers find it in roughly sqrt(N) checks
For N=8(3 qubits), sqrt(N) is approximately 2 iterations.

The reason Grover's is faster is because it uses Amplitude Amplification.
It repeats two operations:
1.Oracle- Marks the correct answer by flipping its phase, without measuring it.(measuring would lead to collapse of the quantum state)

2.Diffusion-reflects all amplitudes about the average amplitude
the state which has had its phase shifted to negative will have its amplitude amplified. 
how?
apply Hadamard gate-puts all the qubits in superposition
 use X gate(NOT gate) to map |000> to |111> for CCZ(CCZ requires all to be 1)
 CCZ gate is then used- flips the phase to negative 
 Undo X
 Undo H
Repeating these processes sqrt(N) times increases the amplitude of the answer.
On measurement (which collapses the quantum state) , it collapses to the state with the highest probability , which will be our correct answer. 