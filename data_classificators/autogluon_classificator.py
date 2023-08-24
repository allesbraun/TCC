import os

import pandas as pd
from autogluon.tabular import TabularPredictor

from data_preprocessor.datasets import smote
from databases import *


def autogluon_classifier(code_csv):
    #x_class, y_class, x_efficiency, y_efficiency = smote()
    # Caminho para a pasta que contém o arquivo datasets
    path_datasets = os.path.dirname(os.path.abspath(__file__))
    path_databases = os.path.join(path_datasets, '..', 'databases')
    path_database = os.path.join(path_databases, 'merged_database.csv')
    # Load and prepare your data
    train_data = pd.read_csv(path_database, sep=",", header=0, decimal=",", dtype=str)
    test_data = code_csv

    # Define the task (classification) and label column
    predictor = TabularPredictor(label='complexity_class')

    # Train the model
    predictor.fit(train_data)

    # Make predictions
    predictions = predictor.predict(test_data)
    return predictions


