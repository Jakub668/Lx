import time
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Tworzymy 8 kubitów - każdy będzie jednym bitem znaku ASCII
qc = QuantumCircuit(800)

# Wprowadzamy wszystkie kubity w stan totalnego chaosu (superpozycji)
for i in range(800):
    qc.h(i)

qc.measure_all()

# Symulujemy pomiar - to tutaj "wszechświat" wybiera konkretny znak
sim = AerSimulator()
counts = sim.run(qc, shots=1).result().get_counts()
binary_result = list(counts.keys())[0]

# Zamieniamy kwantowy wynik na znak tekstowy
char_code = int(binary_result, 2)
quantum_char = chr(char_code)

print("Łączenie z polem kwantowym...")
time.sleep(2)
print(f"Cząstka wybrała bitowy ciąg: {binary_result}")
print(f"Zmaterializowany znak z nicości: {quantum_char}")

