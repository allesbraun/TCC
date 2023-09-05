import os

import pandas as pd
from autogluon.tabular import TabularPredictor

import AutogluonModels
from databases import *


def autogluon_classifier(code_csv):
    # os.environ['CUDA_VISIBLE_DEVICES'] = ''  # elimina uso da gpu no test
    test_data = code_csv
    # 'f1' (for binary classification), 'roc_auc' (for binary classification),
    predictor_efficiency = TabularPredictor.load("AutogluonModels/ag-efficiency_training", require_py_version_match=False)
    # predictor_efficiency.leaderboard(test_data, silent=True)
    predictor_efficiency.plot_ensemble_model()# mostra pesos de cada modelo no emsemble
    # Make predictions
    predictions_efficiency = predictor_efficiency.predict(test_data)
    results_efficiency = predictor_efficiency.fit_summary(show_plot=True)
    
    efficiency = pd.Series([predictions_efficiency[0]], name='efficiency')

    # Adicione a nova coluna ao DataFrame
    test_data = pd.concat([test_data, efficiency], axis=1)
    
    predictor_class = TabularPredictor.load("AutogluonModels/ag-class_training", require_py_version_match=False)
    # predictor_class.leaderboard(test_data, silent=True)
    predictor_class.plot_ensemble_model()# mostra pesos de cada modelo no emsemble
    # Make predictions
    predictions_class = predictor_class.predict(test_data)
    results_class = predictor_class.fit_summary(show_plot=True)

    
    complexity_class = pd.Series([predictions_class[0]], name='complexity_class')

    # Adicione a nova coluna ao DataFrame
    test_data = pd.concat([test_data, complexity_class], axis=1)
    csv_file = str(test_data['filename'])
    csv_file = csv_file.replace('.java', '.csv')
    test_data.to_csv(csv_file, index=False)
    
    # Nome da pasta que você deseja criar
    folder_name = 'csv_files'

    # Cria a pasta se ela não existir
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    # Cria o caminho completo para o arquivo CSV dentro da pasta
    csv_file_path = os.path.join(folder_name, csv_file)

    # Salva o DataFrame em um arquivo CSV dentro da pasta
    test_data.to_csv(csv_file_path, index=False)
    
    # import sklearn.metrics
    # sklearn.metrics.accuracy_score(y_true, y_pred)
    # from autogluon.core.metrics import make_scorer
    # ag_accuracy_scorer = make_scorer(name='accuracy',
    #                              score_func=sklearn.metrics.accuracy_score,
    #                              optimum=1,
    #                              greater_is_better=True)
    # ag_accuracy_scorer(y_true, y_pred)
    # predictor.leaderboard(test_data, extra_metrics=[ag_roc_auc_scorer, ag_accuracy_scorer], silent=True)

    return test_data

    


