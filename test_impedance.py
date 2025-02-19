import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from impedance import preprocessing
from impedance.models.circuits import CustomCircuit
from impedance.visualization import plot_nyquist


def load_data(file_path):
    """Carica i dati dal file CSV in un formato compatibile e ordina le frequenze."""
    df = pd.read_csv(file_path)

    if "FREQUENCY(Hz)" in df.columns and "R(ohm)" in df.columns and "X(ohm)" in df.columns:
        frequencies = df["FREQUENCY(Hz)"].values
        ReZ = df["R(ohm)"].values
        ImZ = df["X(ohm)"].values

        Z = ReZ + 1j * ImZ

        # Ordina le frequenze in ordine crescente
        sorted_indices = np.argsort(frequencies)
        return frequencies[sorted_indices], Z[sorted_indices]
    else:
        raise ValueError("Errore: Il file CSV non contiene le colonne attese!")


def filter_data(frequencies, Z):
    """Filtra i dati per mantenere solo il primo quadrante."""
    return preprocessing.ignoreBelowX(frequencies, Z)


def define_circuit():
    """Definisce il modello del circuito equivalente."""
    circuit_string = 'R0-p(R1,C1)-p(R2-Wo1,C2)'
    initial_guess = [0.01, 0.001, 10, 0.001, 0.001, 10, 1]
    return CustomCircuit(circuit_string, initial_guess=initial_guess)


def visualize_data(frequencies_list, Z_list, Z_fit_list, circuit_list, file_names):
    """Visualizza il diagramma di Nyquist e il diagramma di Bode per più dataset."""

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    ax_nyquist = axes[0, 0]
    ax_bode_mag = axes[0, 1]
    ax_bode_phase = axes[1, 0]

    colors = ['b', 'g', 'r', 'c', 'm', 'y']  # Palette di colori per differenziare dataset
    handles_nyquist = []  # Per la legenda di Nyquist
    handles_bode_mag = []  # Per la legenda di Bode Magnitudine
    handles_bode_phase = []  # Per la legenda di Bode Fase

    for i, (frequencies, Z, Z_fit, circuit, file_name) in enumerate(zip(frequencies_list, Z_list, Z_fit_list, circuit_list, file_names)):
        color = colors[i % len(colors)]  # Assegna un colore diverso per ogni dataset

        # **DIAGRAMMA DI NYQUIST**
        plot_nyquist(Z, ax=ax_nyquist, fmt='o', color=color, label=f'Data {file_name}')
        plot_nyquist(Z_fit, ax=ax_nyquist, fmt='-', color=color, label=f'Fit {file_name}')

        # **DIAGRAMMA DI BODE**
        circuit.plot(f_data=frequencies, Z_data=Z, kind='bode', ax=[ax_bode_mag, ax_bode_phase])

    # **Titoli e legende**
    ax_nyquist.set_title("Nyquist Diagram")
    ax_nyquist.set_xlabel("Re(Z) [Ohm]")
    ax_nyquist.set_ylabel("-Im(Z) [Ohm]")
    ax_nyquist.legend()
    ax_nyquist.grid()

    ax_bode_mag.set_title("Bode Diagram - Magnitude")
    ax_bode_phase.set_title("Bode Diagram - Phase")

    ax_bode_mag.legend()
    ax_bode_phase.legend()

    ax_bode_mag.grid()
    ax_bode_phase.grid()

    plt.tight_layout()
    plt.show()


def main():
    """Main function per la selezione e l'analisi di più file."""
    root = tk.Tk()
    root.withdraw()

    # Seleziona più file CSV
    file_paths = filedialog.askopenfilenames(title="Seleziona i file CSV",
                                             filetypes=[("CSV files", "*.csv")])

    if not file_paths:
        print("Nessun file selezionato. Uscita dal programma.")
        return

    frequencies_list, Z_list, Z_fit_list, circuit_list, file_names = [], [], [], [], []

    for file_path in file_paths:
        print(f"\nAnalizzando: {file_path.split('/')[-1]}")

        # Carica e filtra i dati
        frequencies, Z = load_data(file_path)
        frequencies, Z = filter_data(frequencies, Z)

        # Definisci e adatta il modello del circuito
        circuit = define_circuit()
        circuit.fit(frequencies, Z)
        Z_fit = circuit.predict(frequencies)

        # Stampa i parametri stimati
        print(f"Estimated parameters for {file_path.split('/')[-1]}:", circuit.parameters_)

        # Memorizza i dati per la visualizzazione
        frequencies_list.append(frequencies)
        Z_list.append(Z)
        Z_fit_list.append(Z_fit)
        circuit_list.append(circuit)
        file_names.append(file_path.split("/")[-1])

    # Visualizza i dati e i modelli adattati
    visualize_data(frequencies_list, Z_list, Z_fit_list, circuit_list, file_names)


if __name__ == "__main__":
    main()
