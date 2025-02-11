from impedance import preprocessing
import matplotlib.pyplot as plt

# Importa i dati dal file CSV
frequencies, Z = preprocessing.readCSV('./dati.csv')

# Filtra i dati per mantenere solo il primo quadrante
frequencies, Z = preprocessing.ignoreBelowX(frequencies, Z)

# Mostra i dati filtrati
print("Frequenze filtrate (Hz):", frequencies)
print("Impedenza complessa filtrata:", Z)

# Diagramma di Nyquist
plt.plot(Z.real, -Z.imag, 'o', label='Dati filtrati (primo quadrante)')
plt.xlabel('Re(Z) [Ohm]')
plt.ylabel('-Im(Z) [Ohm]')
plt.legend()
plt.grid()
plt.show()
