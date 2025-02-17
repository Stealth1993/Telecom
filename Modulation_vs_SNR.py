import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def adaptive_mod(snr_db):
    if snr_db < 5:
        return 'QPSK'
    elif 5 <= snr_db < 20:
        return '16QAM'
    else:
        return '64QAM'
    
snr_values = np.linspace(0,20,10)
mod_values = [adaptive_mod(snr) for snr in snr_values]

plt.figure(figsize=(10,6))
plt.plot(snr_values, mod_values, marker='o', color='r', linestyle='-')
plt.xlabel('SNR (dB)')
plt.ylabel('Modulation Scheme')
plt.title('Adaptive Modulation Scheme Selection')
plt.grid()
plt.show()