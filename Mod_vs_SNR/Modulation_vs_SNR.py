import numpy as np
import matplotlib.pyplot as plt

# Function to simulate adaptive modulation scheme selection based on SNR
def adaptive_mod(snr):
    if snr < 5:
        return 'BPSK'
    elif snr < 10:
        return 'QPSK'
    elif snr < 15:
        return '16QAM'
    else:
        return '64QAM'

# generate SNR values
snr_values = np.linspace(0, 20, 10)
mod_values = [adaptive_mod(snr) for snr in snr_values]

# dynamic color map based on values
colors = plt.cm.RdYlGn(np.linspace(0, 1, len(snr_values)))

plt.figure(figsize=(10, 6))
for i in range(len(snr_values) - 1):
    plt.plot(snr_values[i:i+2], mod_values[i:i+2], marker='o', color=colors[i], linestyle='-')

plt.xlabel('SNR (dB)')
plt.ylabel('Modulation Scheme')
plt.title('Adaptive Modulation Scheme Selection')
plt.grid()
plt.show()
