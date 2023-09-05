import os

import pandas as pd
from autogluon.tabular import TabularPredictor

from databases import *


def autogluon_classifier(code_csv):
    verbosity=4 # More training log. TESTAR NO TREINAMENTO, AQUI NÃO É RELEVANTE
    # os.environ['CUDA_VISIBLE_DEVICES'] = ''  # elimina uso da gpu no test
    # eval_metrics = ['accuracy', 'precision', 'f1', 'recall'] TESTAR NO TREINAMENTO
    test_data = code_csv
    # 'f1' (for binary classification), 'roc_auc' (for binary classification),
    predictor_efficiency = TabularPredictor.load("AutogluonModels/ag-efficiency_training", require_py_version_match=False)
    predictor_efficiency.plot_ensemble_model(filename = "efficiency_ensemble_model.png")# mostra pesos de cada modelo no emsemble
    # Make predictions
    predictions_efficiency = predictor_efficiency.predict(test_data)
    # results_efficiency = predictor_efficiency.fit_summary(show_plot=True)
    
    test_data['efficiency'] = predictions_efficiency[0]
    predictor_efficiency.leaderboard(test_data, silent=False) #extra_info = true

    
    predictor_class = TabularPredictor.load("AutogluonModels/ag-class_training", require_py_version_match=False)
    # Make predictions
    predictions_class = predictor_class.predict(test_data)
    # results_class = predictor_class.fit_summary(show_plot=True)
    predictor_class.plot_ensemble_model(filename = "complexity_classensemble_model.png")# mostra pesos de cada modelo no emsemble
    
    test_data['complexity_class'] = predictions_class[0]
    predictor_class.leaderboard(test_data, silent=False) #extra_info = true

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

    


