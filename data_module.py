
import pandas as pd
from sklearn.model_selection import train_test_split
from catboost import Pool

def load_dataset(filename):
    return pd.read_csv(filename)

def preprocess_data(dataset):
    dataset_filtered = dataset[dataset['Final UAV Speed'] >= 0]
    x = dataset_filtered[['UAV Speed', 'UAV Payload','windspeed','windgust','cos(gap angle)']]
    y = dataset_filtered['Final UAV Speed']
    return x, y

def split_data(x, y, test_size=0.1, random_state=42):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size, random_state=random_state)
    return x_train, x_test, y_train, y_test

def create_data_pool(x, y):
    return Pool(data=x, label=y)
