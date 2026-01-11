import os
import random
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# 1. Tworzymy kwantowy rzut monetą
qc = QuantumCircuit(1)
qc.h(0) # Kubit jest teraz w superpozycji - jednocześnie 0 i 1
qc.measure_all()

# 2. Wykonujemy pomiar (tylko 1 próbę!)
sim = AerSimulator()
result = sim.run(qc, shots=1).result()
final_state = list(result.get_counts().keys())[0]

print(f"Kwantowy pomiar wszechświata: {final_state}")

if final_state == '1':
    print("LOS WYBRANY: CZĄSTKA ZADECYDOWAŁA O ZAMKNIĘCIU!")
    # To polecenie wysyła sygnał zamknięcia do Twojego terminala
    os.system("kill -9 $PPID") 
else:
    print("MIAŁEŚ SZCZĘŚCIE. Cząstka oszczędziła Twój proces.")

