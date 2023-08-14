
import matplotlib.pyplot as plt

def visualize_route(x, y, problem, title_suffix=""):
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.plot(x, y, color='green', linestyle='dashed', linewidth=1, marker='o', markerfacecolor='blue', markersize=5)
    
    for i in range(len(x)):
        if i == len(x) - 1:
            ax.text(x[0], y[0], "0/" + str(i), fontsize=12)
        else:
            ax.text(x[i], y[i], str(i), fontsize=12)
    
    plt.title(f"Optimized Route with Wind Vector for {problem} Dataset {title_suffix}")
    plt.show()
