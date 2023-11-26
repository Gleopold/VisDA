# Import necessary libraries
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

class CSVCorrelationFinder:
    def __init__(self, csv_file_path, field1, field2):
        self.csv_file_path = csv_file_path
        self.field1 = field1
        self.field2 = field2

    def load_data(self):
        # Load the CSV file into a Pandas DataFrame
        df = pd.read_csv(self.csv_file_path)

        # Extract the specified fields as NumPy arrays
        x = df[self.field1].values
        y = df[self.field2].values

        return x, y

    def build_model(self):
        # Create a simple neural network model with one layer
        model = keras.Sequential([
            layers.Dense(1, input_shape=(1,))
        ])

        # Compile the model
        model.compile(optimizer='adam', loss='mean_squared_error')

        return model

    def train_model(self, x, y):
        # Build the neural network model
        model = self.build_model()

        # Train the model
        model.fit(x, y, epochs=100)

        return model

    def find_correlation(self):
        # Load the data
        x, y = self.load_data()

        # Normalize the data (optional)
        x = (x - np.mean(x)) / np.std(x)
        y = (y - np.mean(y)) / np.std(y)

        # Train the model
        model = self.train_model(x, y)

        # Get the correlation coefficient
        correlation_coefficient = np.corrcoef(x, y)[0, 1]

        return correlation_coefficient

if __name__ == "__main__":
    # Replace 'your_data.csv' with the path to your CSV file and specify the fields of interest
    csv_file_path = 'your_data.csv'
    field1 = 'field1'  # Replace with the actual name of the first field
    field2 = 'field2'  # Replace with the actual name of the second field

    # Create an instance of the CSVCorrelationFinder class
    correlation_finder = CSVCorrelationFinder(csv_file_path, field1, field2)

    # Find and print the correlation coefficient
    correlation_coefficient = correlation_finder.find_correlation()
    print(f"Correlation coefficient between {field1} and {field2}: {correlation_coefficient}")

