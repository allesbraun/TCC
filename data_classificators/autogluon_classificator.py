import os

import pandas as pd
from autogluon.tabular import TabularPredictor

import AutogluonModels
from databases import *


def autogluon_classifier(code_csv):
        
    test_data = code_csv
    predictor_efficiency = TabularPredictor.load("AutogluonModels/ag-efficiency_training", require_py_version_match=False)
    # predictor_efficiency.leaderboard(test_data, silent=True)
    # Make predictions
    predictions_efficiency = predictor_efficiency.predict(test_data)
    
    efficiency = pd.Series([predictions_efficiency[0]], name='efficiency')

    # Adicione a nova coluna ao DataFrame
    test_data = pd.concat([test_data, efficiency], axis=1)
    
    predictor_class = TabularPredictor.load("AutogluonModels/ag-class_training", require_py_version_match=False)
    # predictor_class.leaderboard(test_data, silent=True)
    # Make predictions
    predictions_class = predictor_class.predict(test_data)
    
    complexity_class = pd.Series([predictions_class[0]], name='complexity_class')

    # Adicione a nova coluna ao DataFrame
    test_data = pd.concat([test_data, complexity_class], axis=1)
    csv_file = str(test_data['filename'])
    csv_file = csv_file.replace('.java', '.csv')
    test_data.to_csv(csv_file, index=False)

    return test_data

    


