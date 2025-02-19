import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from impedance.models.circuits import CustomCircuit
from impedance.visualization import plot_nyquist

def load_data(file_path):
    """Carica i dati dal file CSV in un formato compatibile."""
    df = pd.read_csv(file_path)
    if "FREQUENCY(Hz)" in df.columns and "R(ohm)" in df.columns and "X(ohm)" in df.columns:
        frequencies = df["FREQUENCY(Hz)"].values
        ReZ = df["R(ohm)"].values
        ImZ = df["X(ohm)"].values
        Z = ReZ + 1j * ImZ
        return frequencies, Z
    else:
        raise ValueError("Errore: Il file CSV non contiene le colonne attese!")

def define_circuit():
    """Definisce il modello del circuito equivalente."""
    circuit_string = 'R0-p(R1,C1)-p(R2-Wo1,C2)'
    initial_guess = [0.01, 0.001, 10, 0.001, 0.001, 10, 1]
    circuit = CustomCircuit(circuit_string, initial_guess=initial_guess)
    return circuit

def visualize_data(frequencies_list, Z_list, Z_fit_list, circuit_list, file_names):
    """Visualizza il diagramma di Nyquist e il diagramma di Bode per più dataset."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    ax_nyquist = axes[0, 0]
    ax_bode_mag = axes[0, 1]
    ax_bode_phase = axes[1, 0]

    colors = ['b', 'g', 'r', 'c', 'm', 'y']  # Palette di colori

    for i, (frequencies, Z, Z_fit, circuit, file_name) in enumerate(zip(frequencies_list, Z_list, Z_fit_list, circuit_list, file_names)):
        color = colors[i % len(colors)]

        # **DIAGRAMMA DI NYQUIST**
        plot_nyquist(Z, ax=ax_nyquist, marker='o', linestyle='', color=color, label=f'Dati {file_name}')
        plot_nyquist(Z_fit, ax=ax_nyquist, linestyle='-', color=color, label=f'Fit {file_name}')

        # **DIAGRAMMA DI BODE**
        circuit.plot(f_data=frequencies, Z_data=Z, kind='bode', ax=[ax_bode_mag, ax_bode_phase], color=color, label=f'{file_name}')

    # **Aggiunta legende corrette**
    ax_nyquist.legend(loc="best")
    ax_nyquist.set_title("Nyquist Diagram")
    ax_nyquist.set_xlabel("Re(Z) [Ohm]")
    ax_nyquist.set_ylabel("-Im(Z) [Ohm]")
    ax_nyquist.grid()

    ax_bode_mag.set_title("Bode Diagram - Magnitude")
    ax_bode_mag.set_xlabel("f [Hz]")
    ax_bode_mag.set_ylabel("|Z(ω)| [Ohms]")
    ax_bode_mag.grid()
    ax_bode_mag.legend(['Data', 'Fit'], loc="best")

    ax_bode_phase.set_title("Bode Diagram - Phase")
    ax_bode_phase.set_xlabel("f [Hz]")
    ax_bode_phase.set_ylabel("-ϕZ(ω) [°]")
    ax_bode_phase.grid()
    ax_bode_phase.legend(["Phase"], loc="best")

    plt.tight_layout()
    plt.show()

def main():
    root = tk.Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames(title="Seleziona i file CSV",
                                             filetypes=[("CSV files", "*.csv")])

    if not file_paths:
        print("Nessun file selezionato. Uscita dal programma.")
        return

    frequencies_list, Z_list, Z_fit_list, circuit_list, file_names = [], [], [], [], []

    for file_path in file_paths:
        print(f"\nAnalizzando: {file_path.split('/')[-1]}")
        frequencies, Z = load_data(file_path)
        
        circuit = define_circuit()
        circuit.fit(frequencies, Z)
        Z_fit = circuit.predict(frequencies)

        print(f"Estimated parameters for {file_path.split('/')[-1]}:", circuit.parameters_)

        frequencies_list.append(frequencies)
        Z_list.append(Z)
        Z_fit_list.append(Z_fit)
        circuit_list.append(circuit)
        file_names.append(file_path.split('/')[-1])

    visualize_data(frequencies_list, Z_list, Z_fit_list, circuit_list, file_names)

if __name__ == "__main__":
    main()
