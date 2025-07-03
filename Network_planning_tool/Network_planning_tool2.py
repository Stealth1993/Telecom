import numpy as np
import matplotlib.pyplot as plt

def plan_network(area_size=100, num_bs=3):
    x = np.random.uniform(0, area_size, num_bs)
    y = np.random.uniform(0, area_size, num_bs)
    return list(zip(x, y))

def plot_plan(bs_positions):
    fig, ax = plt.subplots()
    ax.scatter([pos[0] for pos in bs_positions], [pos[1] for pos in bs_positions], c="blue", label="Base Stations")
    ax.set_xlabel("X Position (m)")
    ax.set_ylabel("Y Position (m)")
    ax.set_title("Base Station Placement")
    ax.legend()
    plt.show()

def main():
    bs_positions = plan_network()
    print("Base Station Positions:", bs_positions)
    plot_plan(bs_positions)

if __name__ == "__main__":
    main()