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

    # Salvar o dataframe como um arquivo CSV
    merged_database.to_csv(output_file)
    return merged_database

# #definition of the features applied for each database based on BORUTA

# #complexity class for crawled
# x_crawled_class = crawled_database.drop(['complexity', 'complexity_class', 'efficiency','filename','num_switch','num_break', 'num_Priority','num_hash_map','num_sort'], axis = 1) 
# y_crawled_class = crawled_database['complexity_class']

# #efficiency for crawled
# x_crawled_efficiency = crawled_database.drop(['complexity', 'complexity_class', 'efficiency','filename','num_else','num_binSearch','num_switch','num_hash_set','num_break', 'num_Priority','num_hash_map','num_sort'], axis = 1) 
# y_crawled_efficiency = crawled_database['efficiency']


# ############################################################################################

# #complexity class for reference
# x_paper_class = paper_database.drop(['complexity', 'complexity_class', 'efficiency','filename','num_switch','num_hash_set'], axis = 1) 
# y_paper_class = paper_database['complexity_class']

# #efficiency for reference
# x_paper_efficiency = paper_database.drop(['complexity', 'complexity_class', 'efficiency','filename','num_switch','num_hash_set','num_binSearch'], axis = 1) 
# y_paper_efficiency = paper_database['efficiency']

# ############################################################################################

# #complexity class for merged
# x_merged_class = merged_database.drop(['complexity', 'complexity_class', 'efficiency','filename','num_switch'], axis = 1) 
# y_merged_class = merged_database['complexity_class']

# #efficiency for merged
# x_merged_efficiency = merged_database.drop(['complexity', 'complexity_class', 'efficiency','filename','num_switch','num_break', 'num_Priority','num_hash_set'], axis = 1) 
# y_merged_efficiency = merged_database['efficiency']

# ############################################################################################

# #complexity class for testing with reference data and trained with the crawled data
# x_paper_crawled_class = paper_database.drop(['complexity', 'complexity_class', 'efficiency','filename','num_switch','num_break', 'num_Priority','num_hash_map','num_sort'], axis = 1) 
# y_paper_crawled_class = paper_database['complexity_class']

# #efficiency for testing with reference data and trained with the crawled data
# x_paper_crawled_efficiency = paper_database.drop(['complexity', 'complexity_class', 'efficiency','filename','num_else','num_binSearch','num_switch','num_hash_set','num_break', 'num_Priority','num_hash_map','num_sort'], axis = 1) 
# y_paper_crawled_efficiency = paper_database['efficiency']


# ############################################################################################
                   

# #applying SMOTE for class balancing

# sm = SMOTE(random_state=42, k_neighbors=1)

# #complexity class for crawled
# x_crawled_class, y_crawled_class = sm.fit_resample(x_crawled_class, y_crawled_class)
# #efficiency for crawled
# x_crawled_efficiency, y_crawled_efficiency = sm.fit_resample(x_crawled_efficiency, y_crawled_efficiency)
# #complexity class for reference
# x_paper_class, y_paper_class = sm.fit_resample(x_paper_class, y_paper_class)
# #efficiency for reference
# x_paper_efficiency, y_paper_efficiency = sm.fit_resample(x_paper_efficiency, y_paper_efficiency)
# #complexity class for merged
# x_merged_class, y_merged_class = sm.fit_resample(x_merged_class, y_merged_class)
# #efficiency for merged
# x_merged_efficiency, y_merged_efficiency = sm.fit_resample(x_merged_efficiency, y_merged_efficiency)