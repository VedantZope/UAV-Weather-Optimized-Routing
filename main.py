
import numpy as np
from data_module import load_dataset, preprocess_data, split_data, create_data_pool
from bee_algorithm import run_bee_algorithm
from visualization import visualize_route
from utilities import cosgapangle

def main():
    # Load and preprocess the data
    dataset_filename = "UAV_DATA.csv"  # Modify this to the path of your dataset
    dataset = load_dataset(dataset_filename)
    x, y = preprocess_data(dataset)
    x_train, x_test, y_train, y_test = split_data(x, y)
    train_dataset = create_data_pool(x_train, y_train)
    test_dataset = create_data_pool(x_test, y_test)
    
    # Parameters for Bee Algorithm and other initializations
    # Setting Parameters of Bees Algorithm
VarSize = [1, n]  # Decision Variables Matrix Size
nSelectedSite = round(0.5 * nScoutBee)  # m = Number of Selected Sites
nEliteSite = round(0.4 * nSelectedSite)  # e = Number of Selected Elite Sites
nSelectedSiteBee = round(0.5 * nScoutBee)  # nsp = Number of Selected Recruited Bees for Selected (m-e) Sites
nEliteSiteBee = 2 * nSelectedSiteBee  # nep = Number of Recruited Bees for Elite Sites

# -----

# Initialization
bee=[]
for i in range(nScoutBee):
    bee.append([])
    tour = GlobalSearch (GS,n,pl)
    tour = np.array(tour)
    bee[i]=Bee(tour,Cost(tour,D))

bee.sort(key=lambda bee: bee.Cost, reverse=False)

BestSol = ([],math.inf)
BestSol = bee[0]

BestCost = np.zeros([maxIt,1])
BestPos = []
for i in range(maxIt):
    BestPos.append([])

newbee=Bee([],[])

# -----

# Main Loop
for it in range(maxIt):
    # Elite Sites
    for i in range(nEliteSite):

        bestnewbee=Bee([],math.inf)

        for j in range(nEliteSiteBee):
            newbee.Position = LocalSearch(bee[i].Position, LS)
            newbee.Cost = Cost(newbee.Position,D)
            if newbee.Cost < bestnewbee.Cost:
                bestnewbee.Cost = newbee.Cost
                bestnewbee.Position = newbee.Position

        if bestnewbee.Cost < bee[i].Cost:
            bee[i].Cost = bestnewbee.Cost
            bee[i].Position = bestnewbee.Position

    # Selected Non-Elite Sites
    for i in range(nEliteSite,nSelectedSite):

        bestnewbee=Bee([],math.inf)

        for j in range(nSelectedSiteBee):
            newbee.Position = LocalSearch(bee[i].Position, LS)
            newbee.Cost = Cost(newbee.Position,D)
            if newbee.Cost < bestnewbee.Cost:
                bestnewbee.Cost = newbee.Cost
                bestnewbee.Position = newbee.Position

        if bestnewbee.Cost < bee[i].Cost:
            bee[i].Cost = bestnewbee.Cost
            bee[i].Position = bestnewbee.Position

    # Non - Selected Sites
    for i in range(nSelectedSite,nScoutBee):
        tour = GlobalSearch (GS,n,pl)
        tour = np.array(tour)
        bee[i]=Bee(tour,Cost(tour,D))

    # Sort
    bee.sort(key=lambda bee: bee.Cost, reverse=False)

    # Update
    BestSol.Cost = bee[0].Cost
    BestSol.Position = bee[0].Position

    # Store Best Cost ever found
    BestCost[it] = BestSol.Cost
    BestPos [it] = BestSol.Position
    # Display Iteration Information
    print(['Iteration ' + str(it) + ': Best Cost = ' + str(BestCost[it])])
   ## Drawing the solutions 
    # x and y axis values 
    tour = BestSol.Position
    tour = list(tour)
    tour.append(tour[0])
    tx=[]
    ty=[]
    for i in tour:
        tx.append(Probx[i])
        ty.append(Proby[i])
    x = tx
    y = ty  
    # # plotting the points  
    # plt.plot(x, y, color='green', linestyle='dashed', linewidth = 1, 
    # marker='o', markerfacecolor='blue', markersize=5) 
    # # naming the x axis 
    # plt.xlabel('x - axis') 
    # # naming the y axis 
    # plt.ylabel('y - axis') 
    # # giving a title to my graph 
    # plt.title("Iteration " + str(it)) 
    # # function to show the plot 
    # plt.show() 

# -----

print("Final Routing")
print('->'.join(str(x) for x in BestPos [it]))

# -----

import matplotlib.pyplot as plt

# ... your data initialization ...

fig, ax = plt.subplots(figsize=(10, 7))  # Creating a figure with specified dimensions

# Plotting the route with nodes
ax.plot(x, y, color='green',linestyle='dashed', linewidth=1, marker='o', markerfacecolor='blue', markersize=5)

# Labeling each point in the route
for i in range(len(x)):
    if i == len(x) - 1:
        ax.text(x[0], y[0], "0/" + str(i), fontsize=12)
    else:
        ax.text(x[i], y[i], str(i), fontsize=12)


plt.title(f"Optimized Route with Wind Vector for {problem} Dataset")  # Setting a title for the plot
# plt.grid(True)  # Displaying a grid for better readability
plt.show()


# -----

Vwind

# -----

# import matplotlib.pyplot as plt

# # Define data
# iterations = list(range(len(BestCost)))
# costs = BestCost

# # Initialize the figure
# fig, ax = plt.subplots(figsize=(10, 7))

# # Plot the data
# ax.semilogy(iterations, costs, 'g-', linewidth=1.5, label='Convergence Curve')

# # Set grid, both minor and major
# ax.grid(True, which="both", linestyle="--", linewidth=0.5)

# # Limiting the display range
# ax.set_xlim([0, 1.5*maxIt])
# # ax.set_ylim([0, BestCost[0]])  # Uncomment if you need to set y limits

# # Set titles, labels, and legend
# ax.set_title('Convergence of the Optimization Algorithm for ' + Prob, fontsize=15)
# ax.set_xlabel('Iteration', fontsize=13)
# ax.set_ylabel('Best Cost', fontsize=13)
# ax.legend(fontsize=12)

# # Show the plot
# plt.tight_layout()
# plt.show()


# -----

print("BestCost:",BestCost[it])


# -----

time=0
for i in range(0,len(x)-1):
  if(i==len(x)-2):
    time+=D[0][len(x)-2]
  else:
    time+=D[BestPos[it][i+1]][BestPos[it][i]]
print(time,"hr")


# -----

print("Route Time Matrix:","\n",D)

if __name__ == "__main__":
    main()
