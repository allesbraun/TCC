import os

import pandas as pd
from autogluon.tabular import TabularPredictor

from databases import *


def autogluon_classifier(code_csv):
        
    test_data = code_csv
    predictor = TabularPredictor.load('first_training')
    predictor.leaderboard(test_data, silent=True)
    # Make predictions
    predictions = predictor.predict(test_data)
    return predictions

def autogluon_trainer():
    #x_class, y_class, x_efficiency, y_efficiency = smote()
    # Caminho para a pasta que contém o arquivo datasets
    path_datasets = os.path.dirname(os.path.abspath(__file__))
    path_databases = os.path.join(path_datasets, '..', 'databases')
    path_database = os.path.join(path_databases, 'merged_database.csv')
    # Load and prepare your data
    train_data = pd.read_csv(path_database, sep=",", header=0, decimal=",", dtype=str)
    

    train_data = train_data.drop(['complexity'], axis=1)
    
    # which allows AutoGluon to automatically construct powerful model ensembles based on stacking/bagging, 
    # and will greatly improve the resulting predictions if granted sufficient training time. 
    # The default value of presets is 'medium_quality', which produces less accurate models but 
    # facilitates faster prototyping. With presets, you can flexibly prioritize predictive 
    # accuracy vs. training/inference speed. For example, if you care less about predictive performance and 
    # want to quickly deploy a basic model, consider using: presets=['good_quality', 'optimize_for_deployment']
    # Define the task (classification) and label column
    
    # Definir as colunas alvo (targets)
    target_columns = ['efficiency', 'complexity_class']
    predictor = TabularPredictor(label=target_columns, path = 'first_training').fit(train_data, presets=['good_quality', 'optimize_for_deployment'])
    results = predictor.fit_summary(show_plot=True)
    print(results)
    return predictor


