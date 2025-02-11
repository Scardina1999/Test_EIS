import numpy as np
import matplotlib.pyplot as plt
from impedance import preprocessing
from impedance.models.circuits import CustomCircuit
from impedance.visualization import plot_nyquist


def carica_dati(file_path):
    """Carica i dati dal file CSV."""
    frequencies, Z = preprocessing.readCSV(file_path)
    return frequencies, Z


def filtra_dati(frequencies, Z):
    """Filtra i dati per mantenere solo il primo quadrante."""
    frequencies, Z = preprocessing.ignoreBelowX(frequencies, Z)
    return frequencies, Z


def definisci_circuito():
    """Definisce il modello del circuito equivalente."""
    circuit_string = 'R0-p(R1,C1)-p(R2-Wo1,C2)'
    initial_guess = [0.1, 0.1, 10, 0.1, 0.1, 10, 1]
    circuit = CustomCircuit(circuit_string, initial_guess=initial_guess)
    return circuit


def visualizza_dati(Z, Z_fit, frequencies):
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
    file_path = './dati.csv'

    # Carica i dati
    frequencies, Z = carica_dati(file_path)

    # Filtra i dati
    frequencies, Z = filtra_dati(frequencies, Z)

    # Definisci il circuito e adatta i parametri
    circuit = definisci_circuito()
    circuit.fit(frequencies, Z)
    Z_fit = circuit.predict(frequencies)

    # Stampa i parametri stimati
    print("Parametri stimati:", circuit.parameters_)

    # Calcola l'errore medio
    error = Z - Z_fit
    print("Errore medio:", np.mean(np.abs(error)))

    # Visualizza i dati e il modello adattato
    visualizza_dati(Z, Z_fit, frequencies)


if __name__ == "__main__":
    main()
