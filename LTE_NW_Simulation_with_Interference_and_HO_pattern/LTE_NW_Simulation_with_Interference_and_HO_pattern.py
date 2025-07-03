import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.spatial import distance

# Constants
NUM_ENODEBS = 10 # Number of eNodeBs
NUM_UES = 100 # Number of User Equipments
AREA_SIZE = 1000 # Size of the area (1000m x 1000m)
TX_POWER = 52 # Transmission power in dBm
NOISE_POWER = -174 # Noise power in dBm/Hz
BANDWIDTH = 20e6 # Bandwidth in Hz


def generate_positions(num_points, area_size):
    """Generate random positions for eNodeBs or UEs within the simulation area."""
    np.random.seed(42)
    x = np.random.uniform(0, area_size, num_points)
    y = np.random.uniform(0, area_size, num_points)
    return np.column_stack((x, y))

def calculate_path_loss(distance, frequency=2600e6):
    """Calculate path loss using the COST-231 Hata model (urban area)."""
    # Frequency in MHz, distance in meters
    return 128.1 + 37.6 * np.log10(distance / 1000)

def calculate_shadowing(num_points):
    """Generate log-normal shadowing with 8 dB standard deviation."""
    return np.random.lognormal(0, 8, num_points)

def calculate_sinr(enodeb_positions, ue_positions, tx_power, noise_power, bandwidth):
    """Calculate SINR for each UE based on distances and interference."""
    sinr_values = []
    received_powers = []
    
    for ue_pos in ue_positions:
        distances = [distance.euclidean(ue_pos, enodeb_pos) for enodeb_pos in enodeb_positions]
        path_losses = np.array([calculate_path_loss(d) for d in distances], dtype=int)
        shadowing = calculate_shadowing(len(enodeb_positions))
        
        # Received power from each eNodeB
        rx_powers = tx_power - path_losses + shadowing
        strongest_signal_idx = np.argmax(rx_powers)
        signal = rx_powers[strongest_signal_idx]
        
        # Interference from other eNodeBs
        interference = np.sum(10**(np.array(rx_powers) / 10)) - 10**(signal / 10)
        noise = noise_power + 10 * np.log10(bandwidth)
        
        # SINR calculation
        sinr = 10 * np.log10(10**(signal / 10) / (interference + 10**(noise / 10)))
        sinr_values.append(sinr)
        received_powers.append(signal)
    
    return np.array(sinr_values), np.array(received_powers)

def perform_handovers(sinr_values, threshold=-10):
    """Determine handover decisions based on SINR threshold."""
    handover_attempts = (sinr_values < threshold).astype(int)
    handover_success = handover_attempts * np.random.binomial(1, 0.95, len(handover_attempts))
    return handover_attempts, handover_success

def plot_results(enodeb_positions, ue_positions, sinr_values, handover_success):
    """Visualize SINR distribution and handover success rate."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # SINR Distribution
    sns.histplot(sinr_values, bins=20, kde=True, ax=ax1, color='skyblue')
    ax1.set_title('SINR Distribution Across UEs')
    ax1.set_xlabel('SINR (dB)')
    ax1.set_ylabel('Frequency')
    
    # Network Layout with Handover Success
    ax2.scatter(enodeb_positions[:, 0], enodeb_positions[:, 1], c='red', label='eNodeBs', s=100)
    ax2.scatter(ue_positions[:, 0], ue_positions[:, 1], c=handover_success, cmap='coolwarm', label='UEs', s=50)
    ax2.set_title('Network Layout with Handover Success')
    ax2.set_xlabel('X (meters)')
    ax2.set_ylabel('Y (meters)')
    ax2.legend()
    
    plt.tight_layout()
    plt.show()

def main():
    """Main function to run the LTE network simulation."""
    # Generate positions
    enodeb_positions = generate_positions(NUM_ENODEBS, AREA_SIZE)
    ue_positions = generate_positions(NUM_UES, AREA_SIZE)
    
    # Calculate SINR and received powers
    sinr_values, received_powers = calculate_sinr(enodeb_positions, ue_positions, TX_POWER, NOISE_POWER, BANDWIDTH)
    
    # Perform handover analysis
    handover_attempts, handover_success = perform_handovers(sinr_values)
    
    # Output key statistics
    print(f"Average SINR: {np.mean(sinr_values):.2f} dB")
    print(f"Handover Success Rate: {np.mean(handover_success/handover_attempts)*100:.2f}%")
    
    # Plot results
    plot_results(enodeb_positions, ue_positions, sinr_values, handover_success)

if __name__ == "__main__":
    main()