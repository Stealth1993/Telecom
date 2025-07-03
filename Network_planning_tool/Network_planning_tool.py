import numpy as np
import matplotlib.pyplot as plt


# Plan network size
def plan_network_size(num_enodebs, num_ues, area_size):
    """
    Plan the network size based on the number of eNodeBs and UEs.
    
    Parameters:
    num_enodebs (int): Number of eNodeBs
    num_ues (int): Number of User Equipments
    area_size (float): Size of the area in square meters
    
    Returns:
    float: Density of eNodeBs per square kilometer
    float: Density of UEs per square kilometer
    """
    area_km2 = (area_size / 1000) ** 2  # Convert area size to square kilometers
    enodeb_density = num_enodebs / area_km2
    ue_density = num_ues / area_km2
    
    return enodeb_density, ue_density

# Visualize network size
def visualize_network_size(enodeb_density, ue_density):
    """
    Visualize the network size based on eNodeB and UE densities.
    
    Parameters:
    enodeb_density (float): Density of eNodeBs per square kilometer
    ue_density (float): Density of UEs per square kilometer
    """
    labels = ['eNodeB Density (per km²)', 'UE Density (per km²)']
    densities = [enodeb_density, ue_density]
    
    plt.figure(figsize=(8, 5))
    plt.bar(labels, densities, color=['blue', 'orange'])
    plt.title('Network Size Visualization')
    plt.ylabel('Density')
    plt.grid(axis='y')
    plt.show()

def main():
    # Example parameters
    num_enodebs = 10  # Number of eNodeBs
    num_ues = 100     # Number of User Equipments
    area_size = 1000  # Size of the area in square meters (1000m x 1000m)
    
    # Plan network size
    enodeb_density, ue_density = plan_network_size(num_enodebs, num_ues, area_size)
    
    # Print densities
    print(f"eNodeB Density: {enodeb_density:.2f} per km²")
    print(f"UE Density: {ue_density:.2f} per km²")
    
    # Visualize network size
    visualize_network_size(enodeb_density, ue_density)

if __name__ == "__main__":
    main()