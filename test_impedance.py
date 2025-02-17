import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from impedance import preprocessing
from impedance.models.circuits import CustomCircuit
from impedance.visualization import plot_nyquist


def load_data(file_path):
    """Carica i dati dal file CSV in un formato compatibile."""
    
    # Carica il CSV
    df = pd.read_csv(file_path)

    # Controlliamo se il file ha le colonne corrette
    if "FREQUENCY(Hz)" in df.columns and "R(ohm)" in df.columns and "X(ohm)" in df.columns:
        # Estraiamo le colonne necessarie
        frequencies = df["FREQUENCY(Hz)"].values
        ReZ = df["R(ohm)"].values
        ImZ = df["X(ohm)"].values

        # Costruzione dell'impedenza complessa

        Z = ReZ + 1j * ImZ

        return frequencies, Z
    else:
        raise ValueError("Errore: Il file CSV non contiene le colonne attese!")


def filter_data(frequencies, Z):
    """Filtra i dati per mantenere solo il primo quadrante."""
    frequencies, Z = preprocessing.ignoreBelowX(frequencies, Z)
    return frequencies, Z


def define_circuit():
    """Definisce il modello del circuito equivalente."""
    circuit_string = 'R0-p(R1,C1)-p(R2-Wo1,C2)'
    initial_guess = [0.1, 0.1, 10, 0.1, 0.1, 10, 1]
    circuit = CustomCircuit(circuit_string, initial_guess=initial_guess)
    return circuit


def visualize_data(Z, Z_fit, frequencies):
    """Visualizza il diagramma di Nyquist."""
    fig, ax = plt.subplots()
    plot_nyquist(Z, fmt='o', scale=10, ax=ax)
    plot_nyquist(Z_fit, fmt='-', scale=10, ax=ax)

    plt.legend(['Data', 'Fit'])
    plt.xlabel('Re(Z) [Ohm]')
    plt.ylabel('-Im(Z) [Ohm]')
    plt.grid()
    plt.show()


def main():
    """Esegue l'analisi completa."""
    # Percorso del file CSV
    file_path = './data_test_eis_pouch_1.csv'

    # Carica i dati
    frequencies, Z = load_data(file_path)

    # Filtra i dati
    frequencies, Z = filter_data(frequencies, Z)

    # Definisci il circuito e adatta i parametri
    circuit = define_circuit()
    circuit.fit(frequencies, Z)
    Z_fit = circuit.predict(frequencies)

    # Stampa i parametri stimati
    print("Estimated parameters:", circuit.parameters_)

    # Calcola l'errore medio
    error = Z - Z_fit
    print("Mean error:", np.mean(np.abs(error)))

    # Visualizza i dati e il modello adattato
    visualize_data(Z, Z_fit, frequencies)


if __name__ == "__main__":
    main()
