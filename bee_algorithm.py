
import numpy as np
import math
from catboost import CatBoostRegressor

class Bee:
    def __init__(self, Position, Cost):
        self.Position = Position
        self.Cost = Cost

dataset_filtered = dataset[dataset['Final UAV Speed'] >= 0]
x = dataset_filtered[['UAV Speed', 'UAV Payload','windspeed','windgust','cos(gap angle)']]
y = dataset_filtered['Final UAV Speed']

# -----

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

# -----

train_dataset = cb.Pool(x_train, y_train) 
test_dataset = cb.Pool(x_test, y_test)

# -----

tuned_cat_model=CatBoostRegressor(iterations=500, max_depth=5, learning_rate=0.05) #hyperparameter tuned model

# -----

tuned_cat_model.fit(x_train,y_train,logging_level='Silent')


# -----

def cosgapangle(DirectionVector,WindVector):
  vector_1=DirectionVector
  vector_2=WindVector
  unit_vector_1 = vector_1 / np.linalg.norm(vector_1)
  unit_vector_2 = vector_2 / np.linalg.norm(vector_2)
  dot_product = np.dot(unit_vector_1, unit_vector_2)
  angle = np.arccos(dot_product)
  return(math.cos(angle))

# -----

# UAVspeed=float(input("Enter UAV Speed : "))
# UAVPayload=float(input("Enter UAV Payload : "))
# windspeed=float(input("Enter windspeed : "))
# windgust=float(input("Enter Wind Gust : "))
# winddir=float(input("Enter wind direction(angle in degrees) : "))

UAVspeed = 10
UAVPayload = 5
windspeed = 5
windgust =5
winddir = 60

# -----

Vwind=[windspeed*np.cos(np.radians(winddir)),windspeed*np.sin(np.radians(winddir))]

# -----

class Model:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.n = len(x)
    def Dis (self):
        n = self.n
        D = []
        for i in range (n):
          for j in range (n):
              inputparametersUAV=[UAVspeed, UAVPayload,windspeed,windgust,cosgapangle([x[j]-x[i],y[j]-y[i]],Vwind)] 
              ans=round(np.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2))
              ans=ans/tuned_cat_model.predict(inputparametersUAV)#Route-Time matrix is predicted and stored as an 2-D array [D]
              D.append(ans)
        D=np.array(D)
        D=D.reshape(n,n)
        return D

def run_bee_algorithm(parameters):
    # Logic for the main loop of the bee algorithm from the notebook
    # This can be extracted and organized from the above sections
    pass
