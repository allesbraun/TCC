import os

import pandas as pd
import polars as pl
# import matplotlib.pyplot as plt 
# import seaborn as sn 
# %matplotlib inline 
#used for class balancing
from imblearn.over_sampling import SMOTE


def create_merged_database():

    # Caminho para a pasta que contém o arquivo datasets
    path_datasets = os.path.dirname(os.path.abspath(__file__))

    # Caminho para a pasta que contém os arquivos CSV
    path_databases = os.path.join(path_datasets, '..', 'databases')
    # Caminho completo para cada arquivo CSV
    path_crawled_database = os.path.join(path_databases, 'crawled_database.csv')
    path_paper_database = os.path.join(path_databases, 'paper_database.csv')

    # Carregar os arquivos CSV em DataFrames
    #crawled_database = pd.read_csv(path_crawled_database, dtype={'complexity': str}).T
    crawled_database = pd.read_csv(path_crawled_database, sep=",", header=0, decimal=",", dtype=str)

    
    #paper_database = pd.read_csv(path_paper_database, dtype={'complexity': str}).T
    paper_database = pd.read_csv(path_paper_database, sep=",", header=0, decimal=",", dtype=str)
    
    merged_database = pd.merge(crawled_database, paper_database, how='outer')
    # Remove linhas com valores ausentes (NA) do dataframe
    merged_database = merged_database.dropna()
    # Caminho completo para o arquivo CSV de saída
    output_file = os.path.join(path_databases, 'merged_database.csv')
    
    #VERIFICAÇÃO SE HÁ NOVO CÓDIGO APROVADO PARA ENTRAR NO DATABASE

    # Salvar o dataframe como um arquivo CSV
    merged_database.to_csv(output_file)
    
def smote(database):
    
    # #complexity class for merged
    x_class = database.drop(['complexity', 'complexity_class', 'efficiency','filename','num_switch'], axis = 1) 
    y_class = database['complexity_class']

    # #efficiency for merged
    x_efficiency = database.drop(['complexity', 'complexity_class', 'efficiency','filename','num_switch','num_break', 'num_Priority','num_hash_set'], axis = 1) 
    y_efficiency = database['efficiency']
    
    # #applying SMOTE for class balancing   

    sm = SMOTE(random_state=42, k_neighbors=1)
    
    # complexity class for merged
    x_class, y_class = sm.fit_resample(x_class, y_class)
    #efficiency for merged
    x_efficiency, y_efficiency = sm.fit_resample(x_efficiency, y_efficiency)
    return x_class, y_class, x_efficiency, y_efficiency
    
        



